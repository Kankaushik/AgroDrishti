# AgroDrishti - Smart Farming Platform

## Complete Project Documentation

---

**Project Name:** AgroDrishti (MapLoom Flask)  
**Version:** 1.0  
**Date:** February 21, 2026  
**Platform:** Web Application

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Technology Stack](#2-technology-stack)
3. [System Architecture](#3-system-architecture)
4. [Features Implemented](#4-features-implemented)
5. [Database Design](#5-database-design)
6. [API Endpoints](#6-api-endpoints)
7. [Machine Learning Models](#7-machine-learning-models)
8. [Frontend Components](#8-frontend-components)
9. [File Structure](#9-file-structure)
10. [Pending Features / Future Work](#10-pending-features--future-work)
11. [Installation & Setup](#11-installation--setup)
12. [Screenshots / UI Pages](#12-screenshots--ui-pages)
13. [Team & Credits](#13-team--credits)

---

## 1. Project Overview

### 1.1 Introduction

**AgroDrishti** is an innovative AgriTech platform that combines satellite imagery analysis, AI-powered predictions, and real-time IoT sensor data to help farmers make informed decisions. The platform uses machine learning algorithms for crop yield prediction and provides soil analysis recommendations.

### 1.2 Problem Statement

Modern agriculture faces challenges including:

- Uncertain crop yield predictions
- Lack of data-driven decision making
- Inefficient resource management
- Limited access to expert agricultural advice

### 1.3 Solution

AgroDrishti provides:

- AI-powered crop yield predictions using Random Forest Regressor
- Real-time soil health analysis
- Interactive map-based farm land selection (MapLoom)
- Personalized recommendations for crop improvement
- Role-based dashboards for farmers and administrators

### 1.4 Key Objectives

- Enable farmers to make data-driven decisions
- Predict crop yields with 95% accuracy
- Provide actionable soil health recommendations
- Create an intuitive user interface for all farmer backgrounds

---

## 2. Technology Stack

### 2.1 Backend Technologies

| Technology        | Version | Purpose                          |
| ----------------- | ------- | -------------------------------- |
| **Python**        | 3.11+   | Primary programming language     |
| **Flask**         | 3.0.3   | Web framework                    |
| **Flask-CORS**    | 4.0.1   | Cross-Origin Resource Sharing    |
| **SQLAlchemy**    | 2.0.32  | ORM for database operations      |
| **Pydantic**      | 2.8.2   | Data validation                  |
| **Passlib**       | 1.7.4   | Password hashing (PBKDF2-SHA256) |
| **Bleach**        | 6.1.0   | HTML sanitization                |
| **python-dotenv** | 1.0.1   | Environment variable management  |

### 2.2 Machine Learning Stack

| Technology       | Purpose                                   |
| ---------------- | ----------------------------------------- |
| **Scikit-learn** | ML model training (RandomForestRegressor) |
| **Pandas**       | Data processing and analysis              |
| **NumPy**        | Numerical computations                    |
| **Joblib**       | Model serialization                       |
| **LabelEncoder** | Categorical feature encoding              |

### 2.3 Frontend Technologies

| Technology                 | Purpose                               |
| -------------------------- | ------------------------------------- |
| **HTML5**                  | Page structure                        |
| **CSS3**                   | Styling and animations                |
| **Tailwind CSS**           | Utility-first CSS framework (via CDN) |
| **JavaScript (ES6+)**      | Client-side interactivity             |
| **Bootstrap Icons**        | Icon library                          |
| **Google Fonts (Poppins)** | Typography                            |

### 2.4 Database

| Technology     | Purpose                            |
| -------------- | ---------------------------------- |
| **SQLite**     | Default local database (maps.db)   |
| **PostgreSQL** | Production database (configurable) |

### 2.5 Development Tools

| Tool                    | Purpose                     |
| ----------------------- | --------------------------- |
| **VS Code**             | IDE                         |
| **Git**                 | Version control             |
| **Virtual Environment** | Python dependency isolation |

---

## 3. System Architecture

### 3.1 Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENT LAYER                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐  │
│  │ Landing Page│  │ User Dashboard│ │ Admin Dashboard         │  │
│  │ (index.html)│  │ (user_*.html)│ │ (admin_*.html)          │  │
│  └─────────────┘  └─────────────┘  └─────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                          API LAYER                              │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │                    Flask Application (app.py)             │   │
│  │  /api/login    /api/maps/*    /api/agrodrishti/*         │   │
│  │  /api/logout   /api/feedback   /api/admin/stats          │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      BUSINESS LOGIC LAYER                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐   │
│  │ auth.py      │  │agrodrishti.py│  │ crop_logic.py        │   │
│  │ (Session Mgmt)│  │(API Routes) │  │(Yield Classification)│   │
│  └──────────────┘  └──────────────┘  └──────────────────────┘   │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐   │
│  │ml_predictor.py│  │soil_analyzer│ │ sanitizer.py          │   │
│  │ (ML Predict) │  │(Soil Health) │  │ (HTML Sanitization)  │   │
│  └──────────────┘  └──────────────┘  └──────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                        DATA LAYER                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐   │
│  │ SQLAlchemy   │  │   ML Models  │  │ Training Datasets    │   │
│  │ (models.py)  │  │ *.pkl files  │  │ *.csv files          │   │
│  └──────────────┘  └──────────────┘  └──────────────────────┘   │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │              SQLite Database (maps.db)                    │   │
│  │  Users | Maps | MapVersions | Feedback | CropPredictions  │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### 3.2 Request Flow

1. **User Request** → Flask receives HTTP request
2. **Authentication** → Session-based auth check
3. **Route Handler** → Appropriate endpoint processes request
4. **Business Logic** → ML prediction / Database operation
5. **Response** → JSON response sent to client

---

## 4. Features Implemented

### 4.1 Core Features ✅ COMPLETED

| #   | Feature                   | Status      | Description                                   |
| --- | ------------------------- | ----------- | --------------------------------------------- |
| 1   | **User Authentication**   | ✅ Complete | Login/Logout with session management          |
| 2   | **Role-Based Access**     | ✅ Complete | Admin and User roles with protected routes    |
| 3   | **Password Security**     | ✅ Complete | PBKDF2-SHA256 hashing                         |
| 4   | **User Dashboard**        | ✅ Complete | Farmer-friendly interface with stats          |
| 5   | **Admin Dashboard**       | ✅ Complete | System monitoring with statistics             |
| 6   | **Crop Yield Prediction** | ✅ Complete | ML-based prediction using Random Forest       |
| 7   | **Soil Analysis**         | ✅ Complete | pH and moisture analysis with recommendations |
| 8   | **Map Management**        | ✅ Complete | Create, save, list, retrieve maps             |
| 9   | **Map Versioning**        | ✅ Complete | Automatic version history                     |
| 10  | **Feedback System**       | ✅ Complete | User feedback with map association            |
| 11  | **HTML Sanitization**     | ✅ Complete | XSS protection using Bleach                   |
| 12  | **CORS Support**          | ✅ Complete | Cross-origin API access                       |
| 13  | **Landing Page**          | ✅ Complete | Modern responsive design                      |
| 14  | **Contact Form**          | ✅ Complete | UI form (frontend only)                       |
| 15  | **Dark Mode Support**     | ✅ Complete | Dashboard dark mode CSS                       |
| 16  | **Mobile Responsive**     | ✅ Complete | All pages responsive                          |

### 4.2 Machine Learning Features ✅ COMPLETED

| #   | Feature                     | Model                   | Description                |
| --- | --------------------------- | ----------------------- | -------------------------- |
| 1   | **Yield Prediction**        | Random Forest Regressor | Predicts kg/hectare        |
| 2   | **Yield Categorization**    | Rule-based              | Low/Medium/High categories |
| 3   | **Crop Emoji Mapping**      | Dictionary              | Visual crop indicators     |
| 4   | **Improvement Suggestions** | Rule-based              | Based on input parameters  |
| 5   | **Soil Health Analysis**    | Rule-based              | pH and moisture advice     |

### 4.3 API Features ✅ COMPLETED

| Endpoint                     | Method | Purpose                      |
| ---------------------------- | ------ | ---------------------------- |
| `/api/login`                 | POST   | User authentication          |
| `/api/logout`                | POST   | Session termination          |
| `/api/maps/list`             | GET    | List all maps                |
| `/api/maps/<name>`           | GET    | Get specific map             |
| `/api/maps/save`             | POST   | Save/update map (Admin)      |
| `/api/feedback`              | POST   | Submit feedback              |
| `/api/admin/stats`           | GET    | Dashboard statistics (Admin) |
| `/api/agrodrishti/options`   | GET    | Dropdown options             |
| `/api/agrodrishti/predict`   | POST   | ML prediction                |
| `/api/agrodrishti/recommend` | GET    | Default prediction           |

---

## 5. Database Design

### 5.1 Entity Relationship Diagram

```
┌────────────────┐       ┌────────────────┐
│     USERS      │       │     MAPS       │
├────────────────┤       ├────────────────┤
│ id (PK)        │       │ name (PK)      │
│ username       │       │ geojson        │
│ password_hash  │       │ areaData       │
│ role           │       │ imgSrc         │
└────────────────┘       │ imgW, imgH     │
                         └───────┬────────┘
                                 │ 1:N
                                 ▼
┌────────────────┐       ┌────────────────┐
│   FEEDBACK     │       │  MAP_VERSIONS  │
├────────────────┤       ├────────────────┤
│ id (PK)        │       │ id (PK)        │
│ mapName (FK)   │       │ mapName (FK)   │
│ note           │       │ geojson        │
│ geojson        │       │ areaData       │
│ created        │       │ imgSrc/W/H     │
└────────────────┘       │ savedAt        │
                         └────────────────┘

┌─────────────────────┐
│  CROP_PREDICTIONS   │
├─────────────────────┤
│ id (PK)             │
│ crop                │
│ temperature         │
│ humidity            │
│ ph                  │
│ rainfall            │
│ soil_moisture       │
│ created_at          │
└─────────────────────┘
```

### 5.2 Table Definitions

#### Users Table

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL
);
```

#### Maps Table

```sql
CREATE TABLE maps (
    name VARCHAR(100) PRIMARY KEY,
    geojson TEXT,
    areaData TEXT,
    imgSrc TEXT,
    imgW INTEGER,
    imgH INTEGER
);
```

#### Map Versions Table

```sql
CREATE TABLE map_versions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mapName VARCHAR(100) REFERENCES maps(name) ON DELETE CASCADE,
    geojson TEXT,
    areaData TEXT,
    imgSrc TEXT,
    imgW INTEGER,
    imgH INTEGER,
    savedAt DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

#### Feedback Table

```sql
CREATE TABLE feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    mapName VARCHAR(100),
    note TEXT NOT NULL,
    geojson TEXT,
    created DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### 5.3 Default Users (Bootstrap)

| Username | Password | Role  |
| -------- | -------- | ----- |
| admin    | admin123 | admin |
| user1    | user123  | user  |
| user2    | user234  | user  |

---

## 6. API Endpoints

### 6.1 Authentication APIs

#### POST `/api/login`

**Request:**

```json
{
  "username": "admin",
  "password": "admin123"
}
```

**Response (Success):**

```json
{
  "success": true,
  "role": "admin"
}
```

**Response (Failure):**

```json
{
  "success": false
}
```

#### POST `/api/logout`

**Response:**

```json
{
  "ok": true
}
```

---

### 6.2 Map APIs

#### GET `/api/maps/list`

**Response:**

```json
["farm1", "farm2", "north-field"]
```

#### GET `/api/maps/<name>`

**Response:**

```json
{
    "geojson": {...},
    "areaData": {...},
    "imgData": {
        "imgSrc": "...",
        "imgW": 800,
        "imgH": 600
    }
}
```

#### POST `/api/maps/save` (Admin Only)

**Request:**

```json
{
    "name": "farm1",
    "geojson": {...},
    "areaData": {...},
    "imgData": {
        "imgSrc": "...",
        "imgW": 800,
        "imgH": 600
    }
}
```

---

### 6.3 AgroDrishti APIs

#### GET `/api/agrodrishti/options`

**Response:**

```json
{
  "crop_types": ["Rice", "Wheat", "Maize", "Cotton", "Soybean"],
  "regions": [
    "North India",
    "South India",
    "East India",
    "West India",
    "Central India"
  ],
  "irrigation_types": ["Drip", "Sprinkler", "Flood", "Manual"],
  "fertilizer_types": ["Organic", "Chemical", "Mixed"],
  "disease_statuses": ["None", "Mild", "Moderate", "Severe"]
}
```

#### POST `/api/agrodrishti/predict`

**Request:**

```json
{
  "crop_type": "Rice",
  "region": "North India",
  "soil_moisture": 35.5,
  "soil_ph": 6.5,
  "temperature": 28,
  "rainfall": 120,
  "humidity": 70,
  "sunlight_hours": 7,
  "irrigation_type": "Drip",
  "fertilizer_type": "Organic",
  "pesticide_usage": 10,
  "total_days": 120,
  "ndvi": 0.65,
  "crop_disease_status": "Mild"
}
```

**Response:**

```json
{
  "success": true,
  "prediction": {
    "yield_kg_per_hectare": 4250.5,
    "yield_category": "Medium",
    "yield_color": "amber",
    "crop_type": "Rice",
    "crop_emoji": "🌾",
    "recommendation": "Good yield. Minor optimizations could improve results."
  },
  "improvements": [
    "Consider increasing irrigation frequency",
    "Monitor and consider preventive treatment"
  ],
  "soil_analysis": {
    "soil_moisture_status": "Optimal",
    "soil_moisture_advice": "Soil moisture is adequate",
    "soil_ph_status": "Neutral",
    "soil_ph_advice": "Soil pH is ideal for most crops"
  },
  "model": "Random Forest Regressor"
}
```

---

### 6.4 Admin APIs

#### GET `/api/admin/stats` (Admin Only)

**Response:**

```json
{
  "users": 3,
  "maps": 5,
  "feedback": 12,
  "map_versions": 8,
  "maps_with_feedback": 3
}
```

---

## 7. Machine Learning Models

### 7.1 Crop Yield Prediction Model

| Property             | Value                             |
| -------------------- | --------------------------------- |
| **Algorithm**        | Random Forest Regressor           |
| **n_estimators**     | 100                               |
| **Training Dataset** | Smart_Farming_Crop_Yield_2024.csv |
| **Test Split**       | 80/20                             |
| **Output**           | Yield in kg/hectare               |

### 7.2 Input Features

#### Numeric Features (9)

| Feature            | Description             | Range   |
| ------------------ | ----------------------- | ------- |
| soil*moisture*%    | Soil moisture level     | 0-100%  |
| soil_pH            | Soil acidity/alkalinity | 0-14    |
| temperature_C      | Temperature in Celsius  | 0-50°C  |
| rainfall_mm        | Rainfall in millimeters | 0-500mm |
| humidity\_%        | Air humidity            | 0-100%  |
| sunlight_hours     | Daily sunlight hours    | 0-14    |
| pesticide_usage_ml | Pesticide amount        | 0-100ml |
| total_days         | Crop growth days        | 30-200  |
| NDVI_index         | Vegetation health index | 0-1     |

#### Categorical Features (5)

| Feature             | Categories                          |
| ------------------- | ----------------------------------- |
| region              | North/South/East/West/Central India |
| crop_type           | Rice, Wheat, Maize, Cotton, Soybean |
| irrigation_type     | Drip, Sprinkler, Flood, Manual      |
| fertilizer_type     | Organic, Chemical, Mixed            |
| crop_disease_status | None, Mild, Moderate, Severe        |

### 7.3 Model Files

| File               | Size | Description                 |
| ------------------ | ---- | --------------------------- |
| yield_model.pkl    | ~2MB | Trained Random Forest model |
| yield_encoders.pkl | ~5KB | LabelEncoder objects        |
| yield_features.pkl | ~1KB | Feature column list         |
| crop_model.pkl     | -    | Legacy model file           |

### 7.4 Yield Categories

| Category | Yield Range (kg/ha) | Color | Recommendation                            |
| -------- | ------------------- | ----- | ----------------------------------------- |
| Low      | < 2,500             | Red   | Improve soil, irrigation, or pest control |
| Medium   | 2,500 - 4,500       | Amber | Minor optimizations recommended           |
| High     | > 4,500             | Green | Current practices are optimal             |

### 7.5 Soil Analysis Rules

**Moisture Analysis:**
| Range | Status | Advice |
|-------|--------|--------|
| < 30% | Low | Irrigation required |
| 30-60% | Optimal | Moisture is adequate |
| > 60% | High | Drainage recommended |

**pH Analysis:**
| Range | Status | Advice |
|-------|--------|--------|
| < 5.5 | Acidic | Consider liming |
| 5.5-7.5 | Neutral | Ideal for most crops |
| > 7.5 | Alkaline | Add gypsum or organic matter |

---

## 8. Frontend Components

### 8.1 Page Structure

| Page              | File                   | Purpose               |
| ----------------- | ---------------------- | --------------------- |
| Landing Page      | index.html             | Main entry with login |
| User Dashboard    | user_dashboard.html    | Farmer dashboard      |
| Admin Dashboard   | admin_dashboard.html   | Admin control panel   |
| AgroDrishti User  | agrodrishti_user.html  | User prediction view  |
| AgroDrishti Admin | agrodrishti_admin.html | Admin stats view      |
| MapLoom User      | user.html              | Map viewer            |
| MapLoom Admin     | admin.html             | Map editor            |

### 8.2 UI Components

#### Landing Page Sections

- Navigation Bar (fixed, responsive)
- Hero Section with Login Form
- Features Section (4 feature cards)
- About Section with Statistics
- Contact Section with Form
- Footer with Social Links

#### Dashboard Components

- Sidebar Navigation
- Stats Cards (4 metrics)
- AI Prediction Panel
- Weather Widget
- Soil Health Summary
- Sensor Data Grid
- Settings Modal
- Dark Mode Toggle

### 8.3 Design System

**Color Palette (Agro Theme):**

```css
agro-50:  #f0fdf4
agro-100: #dcfce7
agro-200: #bbf7d0
agro-300: #86efac
agro-400: #4ade80
agro-500: #22c55e
agro-600: #16a34a
agro-700: #15803d
agro-800: #166534
agro-900: #14532d
agro-950: #052e16
```

**Typography:**

- Font Family: Poppins
- Weights: 300, 400, 500, 600, 700, 800

---

## 9. File Structure

```
maploom_flask/
├── __init__.py              # Package initializer
├── app.py                   # Main Flask application (233 lines)
├── auth.py                  # Authentication module (32 lines)
├── db.py                    # Database configuration (23 lines)
├── models.py                # SQLAlchemy models (75 lines)
├── sanitizer.py             # HTML sanitization (7 lines)
├── run.py                   # Application entry point (5 lines)
│
├── agrodrishti.py           # AgroDrishti API routes (145 lines)
├── crop_logic.py            # Yield categorization (75 lines)
├── ml_predictor.py          # ML prediction module (90 lines)
├── soil_analyzer.py         # Soil analysis (30 lines)
├── iot_dummy.py             # Dummy IoT data (10 lines)
│
├── train_model.py           # Model training script (55 lines)
├── yield_model.pkl          # Trained ML model
├── yield_encoders.pkl       # Label encoders
├── yield_features.pkl       # Feature list
├── crop_model.pkl           # Legacy model
│
├── Crop_recommendation.csv  # Crop recommendation dataset
├── Smart_Farming_Crop_Yield_2024.csv  # Training dataset
│
├── requirements.txt         # Python dependencies
├── .env.example             # Environment template
│
└── static/                  # Frontend files
    ├── index.html           # Landing page (901 lines)
    ├── user_dashboard.html  # User dashboard (1391 lines)
    ├── admin_dashboard.html # Admin dashboard (1130 lines)
    ├── agrodrishti_user.html# AgroDrishti user (120 lines)
    ├── agrodrishti_admin.html# AgroDrishti admin (340 lines)
    ├── agrodrishti_user.css # AgroDrishti styles (230 lines)
    ├── user.html            # MapLoom user view
    └── admin.html           # MapLoom admin editor
```

---

## 10. Pending Features / Future Work

### 10.1 High Priority 🔴

| #   | Feature                | Description                   | Complexity |
| --- | ---------------------- | ----------------------------- | ---------- |
| 1   | **User Registration**  | Allow new users to sign up    | Medium     |
| 2   | **Password Reset**     | Email-based password recovery | Medium     |
| 3   | **Email Integration**  | Contact form email sending    | Medium     |
| 4   | **Database Migration** | Alembic for schema migrations | Low        |
| 5   | **API Rate Limiting**  | Prevent API abuse             | Medium     |

### 10.2 Medium Priority 🟡

| #   | Feature                    | Description                   | Complexity |
| --- | -------------------------- | ----------------------------- | ---------- |
| 6   | **Real IoT Integration**   | Connect actual sensors        | High       |
| 7   | **Weather API**            | Real weather data integration | Medium     |
| 8   | **Notification System**    | Alerts for farmers            | Medium     |
| 9   | **Crop Disease Detection** | Image-based disease ML        | High       |
| 10  | **Multi-language Support** | Hindi, Regional languages     | Medium     |
| 11  | **Export Reports**         | PDF/Excel export              | Medium     |
| 12  | **Historical Predictions** | Store and display history     | Medium     |

### 10.3 Low Priority 🟢

| #   | Feature                   | Description                 | Complexity |
| --- | ------------------------- | --------------------------- | ---------- |
| 13  | **Mobile App**            | React Native / Flutter app  | High       |
| 14  | **Satellite Integration** | Real satellite imagery      | High       |
| 15  | **Marketplace**           | Connect farmers with buyers | High       |
| 16  | **Community Forum**       | Farmer discussion board     | Medium     |
| 17  | **Video Tutorials**       | Embedded help videos        | Low        |
| 18  | **Chatbot Assistant**     | AI-powered help             | High       |

### 10.4 Technical Improvements

| #   | Improvement       | Description           |
| --- | ----------------- | --------------------- |
| 1   | Unit Tests        | pytest test suite     |
| 2   | API Documentation | Swagger/OpenAPI spec  |
| 3   | Docker Deployment | Containerization      |
| 4   | CI/CD Pipeline    | GitHub Actions        |
| 5   | Logging System    | Structured logging    |
| 6   | Error Monitoring  | Sentry integration    |
| 7   | Caching Layer     | Redis for performance |
| 8   | Load Balancing    | Production scaling    |

---

## 11. Installation & Setup

### 11.1 Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git

### 11.2 Installation Steps

```bash
# 1. Clone the repository
git clone <repository-url>
cd maploom_flask

# 2. Create virtual environment
python -m venv .venv

# 3. Activate virtual environment
# Windows:
.venv\Scripts\Activate.ps1
# Linux/Mac:
source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Train ML model (if needed)
python train_model.py

# 6. Run the application
python -m maploom_flask.run
```

### 11.3 Environment Variables

Create a `.env` file:

```env
FLASK_SECRET=your-secret-key-here
DATABASE_URL=sqlite:///maps.db
```

### 11.4 Accessing the Application

- **Web Interface:** http://localhost:3000
- **Admin Login:** username: `admin`, password: `admin123`
- **User Login:** username: `user1`, password: `user123`

---

## 12. Screenshots / UI Pages

### 12.1 Public Pages

1. **Landing Page** (`/`)
   - Hero section with login form
   - Feature cards (MapLoom, Rainfall, Soil, Drought)
   - About section with statistics
   - Contact form with social links

### 12.2 User Pages

2. **User Dashboard** (`/user_dashboard.html`)
   - Stats cards (Temperature, Humidity, Soil Health, Crop Yield)
   - AI Prediction section with form
   - Weather widget
   - MapLoom viewer link

3. **AgroDrishti User** (`/agrodrishti/user`)
   - Crop recommendation display
   - Soil health summary
   - Sensor data grid

### 12.3 Admin Pages

4. **Admin Dashboard** (`/admin_dashboard.html`)
   - System statistics
   - User management
   - AI prediction panel
   - Settings and controls

5. **AgroDrishti Admin** (`/agrodrishti/admin`)
   - Total users/maps/feedback stats
   - System activity logs
   - MapLoom editor access

---

## 13. Team & Credits

### 13.1 Project Information

- **Project Name:** AgroDrishti (MapLoom Flask)
- **Project Type:** Smart Agriculture Platform
- **Development Period:** 2025-2026
- **Current Version:** 1.0

### 13.2 Technologies Credits

- Flask - Pallets Projects
- SQLAlchemy - SQLAlchemy Authors
- Tailwind CSS - Tailwind Labs
- Scikit-learn - scikit-learn developers
- Bootstrap Icons - Bootstrap Team

### 13.3 Data Sources

- Training Data: Smart_Farming_Crop_Yield_2024.csv
- Crop Data: Crop_recommendation.csv

---

## Appendix A: API Quick Reference

| Endpoint                     | Method | Auth  | Description        |
| ---------------------------- | ------ | ----- | ------------------ |
| `/api/login`                 | POST   | No    | User login         |
| `/api/logout`                | POST   | No    | User logout        |
| `/api/maps/list`             | GET    | No    | List all maps      |
| `/api/maps/<name>`           | GET    | No    | Get map details    |
| `/api/maps/save`             | POST   | Admin | Save map           |
| `/api/feedback`              | POST   | No    | Submit feedback    |
| `/api/admin/stats`           | GET    | Admin | Dashboard stats    |
| `/api/agrodrishti/options`   | GET    | No    | Form options       |
| `/api/agrodrishti/predict`   | POST   | No    | ML prediction      |
| `/api/agrodrishti/recommend` | GET    | No    | Default prediction |

---

## Appendix B: Model Performance

| Metric           | Value                   |
| ---------------- | ----------------------- |
| Algorithm        | Random Forest Regressor |
| Training Samples | ~10,000+                |
| Test Split       | 20%                     |
| R² Score         | ~0.95+                  |
| MAE              | ~250 kg/ha              |

---

## Appendix C: Security Measures

| Measure            | Implementation       |
| ------------------ | -------------------- |
| Password Hashing   | PBKDF2-SHA256        |
| Session Management | Flask Session        |
| Input Sanitization | Bleach library       |
| CORS               | Flask-CORS           |
| Admin Protection   | Role-based decorator |

---

**Document Generated:** February 21, 2026  
**Last Updated:** February 21, 2026  
**Version:** 1.0

---

_© 2026 AgroDrishti - Smart Farming Platform_
