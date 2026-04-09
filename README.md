# 🎬 Movie Website Platform

A scalable and performance-focused **movie showcase platform** built with Flask, designed to deliver a cinematic and multilingual user experience.

---

## 🚀 Overview

This project is a dynamic movie website that supports:

- Multiple movies with structured data
- Multi-language support (English & Hindi)
- Optimized media handling
- Modular and scalable architecture

---

## ✨ Features

- **Dynamic Movie Rendering**
- **Multi-language Support (en / hi)**
- **Component-based CSS structure**
- **Optimized Image Handling (High/Low Res)**
- **Responsive Design**
- **Scalable Movie Data System**

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Flask (Python)  
- **Templating:** Jinja2  
- **Data:** JSON-based content system  

---

## 📂 Project Structure

```
MOVIE/
│── env/
│
│── movies/
│   ├── kalyug/
│   │   └── data/
│   │       ├── en.json
│   │       ├── hi.json
│   │
│   ├── mahadev_tak_ka_safar/
│       └── data/
│
│── static/
│   ├── common/
│   │   ├── images/
│   │   ├── common.json
│   │
│   ├── css/
│   │   ├── base.css
│   │   ├── components.css
│   │   ├── layout.css
│   │   ├── sections.css
│   │
│   ├── movies/
│       ├── kalyug/
│       │   └── images/
│       │       ├── high-res/
│       │       ├── low-res/
│       │
│       ├── mahadev_tak_ka_safar/
│
│── templates/
│   └── index.html
│
│── app.py
│── requirements.txt
│── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/ritik-sanatanapp/movie-page.git
cd movie-page
```

### 2. Create virtual environment (optional but recommended)
```bash
python -m venv env
source env/bin/activate   # Mac/Linux
env\Scripts\activate      # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run the Flask app
```bash
python app.py
```

### Open in browser
```
http://127.0.0.1:5050
```

---

## 🌐 Language Support

Language is controlled via query parameters:

```
/movie/kalyug?lang=en
/movie/kalyug?lang=hi
```

---

## ⚡ Architecture Highlights

- **JSON-driven content system** for easy updates  
- **Separated common & movie-specific assets**  
- **High-res / Low-res image strategy** for performance  
- **Modular CSS for maintainability**  

---

## 🔒 Scope

This project is intended for **internal/company use**.  
All changes should align with project architecture and standards.

---

## 📄 License

Proprietary – All rights reserved.
