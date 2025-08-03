from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

model = joblib.load('model.pkl')
pass_map = joblib.load('pass_map.pkl')
pass_map_rev = {v: k for k, v in pass_map.items()}

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':     
        hours_studied = float(request.form['hours_studied'])
        attendance = float(request.form['attendance'])
        assignments = float(request.form['assignments_completed'])
        sleep = float(request.form['sleep_hours'])

        pred_num = model.predict([[hours_studied, attendance, assignments, sleep]])[0]
        prediction = pass_map_rev.get(pred_num, "Unknown")

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
