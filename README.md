# SVM-Support-Vector-Machines-

# Student Pass Prediction using SVM

This is a simple machine learning web app that predicts whether a student will pass or fail based on input features such as hours studied, attendance, assignments completed, and sleep hours. The backend uses a Support Vector Machine (SVM) classifier, and the frontend is built with Flask.

## 📁 Project Structure
svm_student_project/
├── app.py # Flask app
├── train_model.py # SVM model training script
├── student_performance.csv # Dataset
├── model.pkl # Trained model (generated after running train_model.py)
├── pass_map.pkl # Label mapping (generated after running train_model.py)
└── templates/
└── index.html # HTML UI

