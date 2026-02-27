
# 🚀 AI Startup Success Predictor

An AI-powered web application that predicts whether a startup will:

- ✅ Operate Successfully  
- ❌ Fail / Close  
- 💼 Get Acquired  

The system uses Machine Learning to analyze financial and business indicators and provides a confidence score along with risk level.

---

## 📌 Project Overview

This project integrates a trained Machine Learning model with a Flask-based web application.  
Users can input startup-related parameters, and the system predicts the likely outcome.

The model evaluates:

- Financial strength
- Investor confidence
- Business growth indicators
- Market recognition
- Venture capital involvement

---

## 🧠 Machine Learning Model

The model was trained using historical startup data.

### 🎯 Target Classes:
- `Operating` – Successful startup
- `Closed` – Failed startup
- `Acquired` – Highly successful startup

### 📊 Input Features:

| Parameter | Description |
|------------|-------------|
| Total Funding | Total capital raised |
| Funding Rounds | Number of investment rounds |
| Business Relationships | Partnerships and connections |
| Milestones | Achievements and growth stages |
| Average Investors | Average investor participation |
| Top 500 Status | Whether startup is recognized |
| Venture Capital | VC funding availability |
| Age at First Funding | Startup maturity at first funding |

---

## 🌐 Web Application Features

- Modern Dark Themed UI
- Animated Loading Screen
- Dynamic Confidence Progress Bar
- Risk-Based Color Indicators
- Responsive Layout
- Glassmorphism Design

---

## 🛠 Tech Stack

- Python
- Flask
- Scikit-learn
- HTML5
- CSS3
- JavaScript
- Joblib / Pickle

---

## 📂 Project Structure

```

Startup_Prediction/
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── model.pkl
├── app.py
└── README.md

````

---

## ⚙ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/startup-success-predictor.git
cd startup-success-predictor
````

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 4️⃣ Run Application

```bash
python app.py
```

Open browser and go to:

```
http://127.0.0.1:5000
```

---

## 📊 Output

The system displays:

* Predicted Startup Outcome
* Confidence Percentage
* Risk Level
* Animated Progress Indicator

---

## 🎓 Academic Use

This project demonstrates:

* Machine Learning model deployment
* Flask web integration
* Frontend & Backend integration
* UI/UX design principles
* Real-world AI application development

---

## 📌 Future Improvements

* Feature importance visualization
* Model accuracy display
* Cloud deployment (AWS / Heroku)
* Database integration
* REST API version

---
