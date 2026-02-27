from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = pd.DataFrame([[

            float(request.form['funding_total_usd']),
            float(request.form['funding_rounds']),
            float(request.form['relationships']),
            float(request.form['milestones']),
            float(request.form['avg_participants']),
            float(request.form['is_top500']),
            float(request.form['has_VC']),
            float(request.form['age_first_funding_year'])

        ]], columns=[

            'funding_total_usd',
            'funding_rounds',
            'relationships',
            'milestones',
            'avg_participants',
            'is_top500',
            'has_VC',
            'age_first_funding_year'

        ])

        prediction = model.predict(input_data)[0]
        probs = model.predict_proba(input_data)[0]

        status_map = {
            0: "Operating (Successful Startup)",
            1: "Closed (Failed Startup)",
            2: "Acquired (Highly Successful Startup)"
        }

        result = status_map.get(prediction, "Unknown")
        confidence = round(max(probs) * 100, 2)

        if prediction == 2:
            risk = "Very Low Risk"
        elif prediction == 0:
            risk = "Low Risk"
        else:
            risk = "High Risk"

        return render_template(
            "result.html",
            outcome=result,
            probability=confidence,
            risk=risk
        )

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)