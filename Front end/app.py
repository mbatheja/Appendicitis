from flask import Flask, jsonify
import joblib
from preprocess import get_features_from_db


app = Flask(__name__)
model = joblib.load("diagnosis_pipeline.pkl")

@app.route("/predict_from_db/visit_id=<int:visit_id>", methods=["GET"])
def predict_from_db(visit_id):
    try:

        X = get_features_from_db(visit_id)
        print(X)
        if X.empty:
            return jsonify({"error": f"No data found for visit_id={visit_id}"}), 404

        y_pred = model.predict(X)
        y_prob = model.predict_proba(X)[:, 1]

        return jsonify({
            "visit_id": visit_id,
            "prediction": "appendicitis" if y_pred == 1 else "no appendicitis",
            "probability": round(float(y_prob), 4)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
