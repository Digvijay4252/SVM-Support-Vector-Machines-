<!-- # SVM-Support-Vector-Machines-

# Student Pass Prediction using SVM

This is a simple machine learning web app that predicts whether a student will pass or fail based on input features such as hours studied, attendance, assignments completed, and sleep hours. The backend uses a Support Vector Machine (SVM) classifier, and the frontend is built with Flask.



## How to Use
<img width="1071" height="799" alt="image" src="https://github.com/user-attachments/assets/bfafd75c-3bd9-489a-89c9-a915641eeecc" />
<img width="1148" height="839" alt="image" src="https://github.com/user-attachments/assets/65546498-a85e-4589-9f39-48a83b41d6f7" />
<img width="1165" height="755" alt="image" src="https://github.com/user-attachments/assets/86e336a8-9601-4f6a-bf9e-345c8c308f28" />
 -->

## SVM – Support Vector Machines

Welcome to the SVM Classifier Web App! This project demonstrates how to train, save, and deploy a Support Vector Machine (SVM) model using Flask and scikit-learn. Users can input student-related data to predict whether a student will pass or fail based on the trained SVM model.

---

## Project Structure

```
SVM-Support-Vector-Machines/
│
├── app.py                  # Flask application
├── train_model.py          # SVM model training script
├── model.pkl               # Trained SVM model
├── pass_map.pkl            # Label encoder for target values
├── student_performance.csv # Dataset used for training
├── templates/
│   └── index.html          # HTML form for user input
└── static/
   └── style.css           # (optional) CSS for form styling

```

---

## Setup Instructions

1.  **Clone the repository**

```
git clone https://github.com/Digvijay4252/SVM-Support-Vector-Machines-.git
cd SVM-Support-Vector-Machines-
```

Install dependencies

```
pip install -r requirements.txt
```

Run the application

```
python app.py
```

Open in browser

Visit: http://localhost:5000

## Screenshots

 <img width="1071" height="799" alt="image" src="https://github.com/user-attachments/assets/bfafd75c-3bd9-489a-89c9-a915641eeecc" />
 
 <img width="1148" height="839" alt="image" src="https://github.com/user-attachments/assets/65546498-a85e-4589-9f39-48a83b41d6f7" />
 
 <img width="1165" height="755" alt="image" src="https://github.com/user-attachments/assets/86e336a8-9601-4f6a-bf9e-345c8c308f28" />
 
 ## Future Improvements
 Add model confidence scores

Enable CSV file upload and batch predictions

Add charts using Plotly or Chart.js

Host on Render/Heroku for live demo
