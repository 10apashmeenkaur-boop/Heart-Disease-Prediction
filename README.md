# ❤️ Heart Disease Prediction System

An end-to-end Machine Learning web application for predicting the likelihood of heart disease using clinical parameters. The project demonstrates a complete ML workflow including data preprocessing, model training, experiment tracking, deployment, and a user-friendly Flask interface.

---

## 🚀 Features

- Predicts heart disease risk from patient health parameters
- Interactive Flask web application
- Data preprocessing and feature engineering pipeline
- Model training and evaluation
- MLflow experiment tracking
- DVC for dataset versioning
- Docker support for deployment
- Modular project architecture

---

## 📊 Dataset

The model is trained on a heart disease dataset containing patient clinical attributes.

### Features

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Serum Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise Induced Angina
- ST Depression
- Slope of ST Segment
- Number of Major Vessels
- Thalassemia

### Target

- Heart Disease
- No Heart Disease

---

## 🛠 Tech Stack

### Backend
- Python
- Flask

### Machine Learning
- Scikit-Learn
- CatBoost
- XGBoost
- Pandas
- NumPy

### Experiment Tracking
- MLflow
- DVC

### Visualization
- Matplotlib
- Seaborn

### Deployment
- Docker

---

## 📂 Project Structure

```
Heart-Disease-Prediction
│
├── src/
│   ├── components/
│   ├── pipeline/
│   ├── utils/
│
├── templates/
├── static/
├── Notebook_Experiments/
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/10apashmeenkaur-boop/Heart-Disease-Prediction.git
```

Move into the project

```bash
cd Heart-Disease-Prediction
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Visit
http://127.0.0.1:5000


## 📈 Machine Learning Workflow

- Data Ingestion
- Data Cleaning
- Feature Engineering
- Model Training
- Model Evaluation
- Prediction Pipeline
- Flask Deployment

## 📷 Application

The web application allows users to enter patient health information and predicts the likelihood of heart disease using the trained machine learning model.

## 🔮 Future Improvements

- User Authentication
- Cloud Deployment
- REST API Support
- Model Monitoring
- Explainable AI (SHAP)

## 📄 License

This project is licensed under the MIT License.
## 👤 Author

**Pashmeen Kaur**

Chemical Engineering Undergraduate, NIT Raipur

GitHub:
https://github.com/10apashmeenkaur-boop

LinkedIn:
(Add your LinkedIn URL)

## Acknowledgements

This repository is based on an open-source Heart Disease Prediction project and has been adapted for learning, experimentation, and deployment practice. Additional modifications, setup, and documentation have been added during customization.
