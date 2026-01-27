from __future__ import annotations

import json
from datetime import datetime
from typing import Optional

from flask import (
    Flask,
    jsonify,
    request,
    send_from_directory,
    session
)
from flask_cors import CORS

from sqlalchemy import select, func
from sqlalchemy.orm import Session

from dotenv import load_dotenv
load_dotenv()

# ---- Local imports ----
from .db import engine, Base
from .models import User, Map, MapVersion, Feedback
from .auth import init_app as init_auth, login_user, admin_required
from .sanitizer import sanitize_html
from .agrodrishti import init_agrodrishti


# ======================================================
# App setup
# ======================================================
app = Flask(__name__, static_folder="static", static_url_path="/")
CORS(app, resources={r"/api/*": {"origins": "*"}})

init_auth(app)
init_agrodrishti(app)


# ======================================================
# DB bootstrap
# ======================================================
def bootstrap():
    Base.metadata.create_all(bind=engine)

    with Session(engine) as db:
        if not db.scalar(select(User).where(User.username == "admin")):
            db.add_all([
                User.make("admin", "admin123", "admin"),
                User.make("user1", "user123", "user"),
                User.make("user2", "user234", "user"),
            ])
            db.commit()

bootstrap()


# ======================================================
# STATIC PAGES (VERY IMPORTANT)
# ======================================================

# ✅ ROOT = MAPLOOM (ALWAYS)
@app.get("/")
def maploom_root():
    return send_from_directory(app.static_folder, "index.html")


# ✅ LOGIN PAGE (ONLY WHEN USER CLICKS LOGIN)
@app.get("/login")
def login_page():
    return send_from_directory(app.static_folder, "login.html")


# ✅ AGRODRISHTI USER DASHBOARD
@app.get("/agrodrishti/user")
def agrodrishti_user():
    return send_from_directory(app.static_folder, "agrodrishti_user.html")


# ✅ AGRODRISHTI ADMIN DASHBOARD
@app.get("/agrodrishti/admin")
@admin_required
def agrodrishti_admin():
    return send_from_directory(app.static_folder, "agrodrishti_admin.html")


# ======================================================
# AUTH API
# ======================================================
@app.post("/api/login")
def api_login():
    data = request.get_json(silent=True) or {}

    username = (data.get("username") or "").strip()
    password = data.get("password") or ""

    with Session(engine) as db:
        user = db.scalar(select(User).where(User.username == username))

        if user and user.verify(password):
            login_user(user.id, user.role)
            return jsonify({
                "success": True,
                "role": user.role
            })

    return jsonify({"success": False}), 401


@app.post("/api/logout")
def api_logout():
    session.clear()
    return jsonify({"ok": True})


# ======================================================
# ADMIN DASHBOARD STATS
# ======================================================
@app.get("/api/admin/stats")
@admin_required
def admin_stats():
    with Session(engine) as db:
        users = db.scalar(select(func.count()).select_from(User))
        maps = db.scalar(select(func.count()).select_from(Map))
        feedback = db.scalar(select(func.count()).select_from(Feedback))
        versions = db.scalar(select(func.count()).select_from(MapVersion))

        maps_with_feedback = db.scalar(
            select(func.count(func.distinct(Feedback.mapName)))
            .where(Feedback.mapName.isnot(None))
        )

    return jsonify({
        "users": users,
        "maps": maps,
        "feedback": feedback,
        "map_versions": versions,
        "maps_with_feedback": maps_with_feedback
    })


# ======================================================
# MAPLOOM MAP APIs (UNCHANGED LOGIC)
# ======================================================
@app.get("/api/maps/list")
def list_maps():
    with Session(engine) as db:
        rows = db.scalars(select(Map.name)).all()
    return jsonify(rows)


@app.get("/api/maps/<string:name>")
def get_map(name: str):
    with Session(engine) as db:
        m = db.get(Map, name)

        if not m:
            return jsonify({"error": "Not found"}), 404

        return jsonify({
            "geojson": json.loads(m.geojson) if m.geojson else None,
            "areaData": json.loads(m.areaData) if m.areaData else {},
            "imgData": {
                "imgSrc": m.imgSrc,
                "imgW": m.imgW,
                "imgH": m.imgH,
            },
        })


@app.post("/api/maps/save")
@admin_required
def save_map():
    payload = request.get_json(silent=True) or {}
    name = (payload.get("name") or "").strip()

    if not name:
        return jsonify({"error": "name is required"}), 400

    with Session(engine) as db:
        m = db.get(Map, name)

        if m:
            db.add(MapVersion(
                mapName=name,
                geojson=m.geojson,
                areaData=m.areaData,
                imgSrc=m.imgSrc,
                imgW=m.imgW,
                imgH=m.imgH,
            ))
        else:
            m = Map(name=name)
            db.add(m)

        m.geojson = json.dumps(payload.get("geojson"))
        m.areaData = json.dumps(payload.get("areaData", {}))
        img = payload.get("imgData", {})
        m.imgSrc = img.get("imgSrc")
        m.imgW = img.get("imgW")
        m.imgH = img.get("imgH")

        db.commit()

    return jsonify({"ok": True})


# ======================================================
# FEEDBACK
# ======================================================
@app.post("/api/feedback")
def post_feedback():
    data = request.get_json(silent=True) or {}

    fb = Feedback(
        mapName=(data.get("mapName") or "").strip() or None,
        note=sanitize_html(data.get("note") or ""),
        geojson=json.dumps(data.get("geojson")) if data.get("geojson") else None,
    )

    with Session(engine) as db:
        db.add(fb)
        db.commit()

    return jsonify({"ok": True})


# ======================================================
# ENTRY POINT
# ======================================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
