import streamlit as st
import requests
from sqlalchemy import create_engine, text

# --- Database connection ---
def get_db_engine():
    return create_engine("postgresql+psycopg2://dadb:123456789qQ@localhost:5432/DSS")

engine = get_db_engine()

#st.title("Appendicitis Diagnosis Prediction")

#---CSS elements---
predict_css = """
<style>
    /* Set background image for entire app */
    .stApp {
        position: relative;
        background-image: url("https://cdn.pixabay.com/photo/2019/04/03/03/06/medical-equipment-4099430_1280.jpg");
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center center;
        background-attachment: fixed;
    }

    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0; right: 0; bottom: 0;
        background: rgba(255,255,255,0.7);
        z-index: 0;
        pointer-events: none;
    }
    /* Ensure content is above the overlay */
    .stApp > * {
        position: relative;
        z-index: 1;
    }

    /* Style for the title to look like a banner */
    .title-banner {
        background-color: rgba(0, 123, 255, 0.8);  /* Blue background with 80% opacity */
        color: white;
        padding: 50px 20px;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        margin-bottom: 20px;
        text-transform: uppercase;
    }
    

    /* Responsive adjustments for smaller screens */
    @media (max-width: 768px) {
        .banner, .login-container, .warning-container {
            width: 90%;
        }
        .header {
            font-size: 36px;
        }
    }      
</style>
"""
st.markdown(predict_css, unsafe_allow_html=True)

# --- Title with banner-style ---
st.markdown('<div class="title-banner">Appendicitis Diagnosis Prediction</div>', unsafe_allow_html=True)


# --- Get latest visit_id from session state ---
visit_id = st.session_state.get("last_visit_id") or st.session_state.get("latest_visit_id")
if not visit_id:
    st.error("No visit ID found. Please complete the patient form first.")
    st.stop()

f_name = st.session_state.get("first_name")
l_name = st.session_state.get("last_name")

st.info(f"Fetching prediction for Visit ID: {visit_id}")

st.info(f"Patient:{f_name} {l_name}")

# --- Call Flask API ---
url = f"http://localhost:5000/predict_from_db/visit_id={visit_id}"
try:
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        prediction = result.get("prediction")
        probability = result.get("probability")

        if prediction is not None and probability is not None:
            st.success(f"Prediction: {prediction}")
            st.write(f"Probability: {probability}")

            # Store the prediction in session state for later use
            st.session_state["prediction"] = prediction
            st.session_state["probability"] = probability

        # --- Insert diagnosis into database ---
        # Get new diagnosis_id
        def get_last_diagnosis_id():
            with engine.connect() as conn:
                result = conn.execute(text("SELECT MAX(diagnosis_id) FROM diagnosis"))
                last_id = result.fetchone()[0]
                return last_id if last_id is not None else 0
        new_diagnosis_id = get_last_diagnosis_id() + 1

        # Insert into diagnosis table
        with engine.begin() as conn:
            conn.execute(
                text("""
                    INSERT INTO diagnosis (diagnosis_id, diagnosis, visit_id)
                    VALUES (:diagnosis_id, :diagnosis, :visit_id)
                """),
                {
                    "diagnosis_id": new_diagnosis_id,
                    "visit_id": visit_id,
                    "diagnosis": prediction
                }
            )
        st.success("Diagnosis recorded")

    else:
        st.error(f"API error: {response.json().get('error', 'Unknown error')}")
except Exception as e:
    st.error(f"Could not connect to prediction API: {e}")
