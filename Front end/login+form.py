import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import datetime
from datetime import date
import sqlalchemy
from sqlalchemy import create_engine, text

#some calculation functions
            
def calc_BMI(Height, Weight):
    BMI = round((Weight/((Height/100)**2)),2)
    return BMI

min_dob = datetime.date(1900, 1, 1)  # Earliest selectable date
max_dob = datetime.date.today()       # Latest selectable date (today)

#Load Yaml
with open('./credentials.yml') as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

# Create the authenticator object using your YAML structure
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

#align ids with databases
def get_db_engine():
    engine = create_engine(
        "postgresql+psycopg2://dadb:123456789qQ@localhost:5432/DSS" )
    return engine
engine = get_db_engine()

def get_last_visit_id():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT MAX(visit_id) FROM visit"))
        last_vid = result.fetchone()[0]
        return last_vid if last_vid is not None else 0
last_visit_id = get_last_visit_id()
new_visit_id = last_visit_id + 1

def get_last_patient_id():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT MAX(patient_id) FROM patient"))
        last_pid = result.fetchone()[0]
        return last_pid if last_pid is not None else 0
last_patient_id = get_last_patient_id()
new_patient_id = last_patient_id + 1

def get_last_lab_id():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT MAX(lab_id) FROM lab"))
        last_lid = result.fetchone()[0]
        return last_lid if last_lid is not None else 0
last_lab_id = get_last_lab_id()
new_lab_id = last_lab_id + 1

def get_last_diagnosis_id():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT MAX(diagnosis_id) FROM diagnosis"))
        last_did = result.fetchone()[0]
        return last_did if last_did is not None else 0
last_diagnosis_id = get_last_diagnosis_id()
new_diagnosis_id = last_diagnosis_id + 1

def get_last_clinical_id():
     with engine.connect() as conn:
        result = conn.execute(text("SELECT MAX(clinical_id) FROM exam"))
        last_cid = result.fetchone()[0]
        return last_cid if last_cid is not None else 0
last_clinical_id = get_last_clinical_id()
new_clinical_id = last_clinical_id + 1   

def get_last_demo_id():
     with engine.connect() as conn:
        result = conn.execute(text("SELECT MAX(demographic_id) FROM vital_sign"))
        last_deid = result.fetchone()[0]
        return last_deid if last_deid is not None else 0
last_demo_id = get_last_demo_id()
new_demo_id = last_demo_id + 1

# Define CSS for background image and header
login_css = """
<style>
    /* Set background image for entire app */
    .stApp {
        position: relative;
        background-image: url("https://images.pexels.com/photos/5207102/pexels-photo-5207102.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");
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

    /* Banner (clinic title) styling */
    .banner {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 1rem;
        border-radius: 15px;
        width: 80%;
        margin: 4rem auto;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
    }

    /* Header inside the banner */
    .header {
        font-size: 48px;
        font-weight: bold;
        font-family: 'Helvetica', sans-serif;
        color: #333333;
        margin: 0;
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


st.markdown(login_css, unsafe_allow_html=True)  # Apply CSS

# Display the banner only once, before the login logic
st.markdown(
    """<div class='banner'><h1 class='header'>CMU Kids Clinic</h1></div>""",
    unsafe_allow_html=True,
)

#Login widget
authenticator.login(location='main')

name = st.session_state.get('name')
authentication_status = st.session_state.get('authentication_status')
username = st.session_state.get('username')

if authentication_status:
    authenticator.logout('Logout', 'sidebar')
    st.success(f"Welcome, {name}!")

     # Define the physician ID mapping
    physician_id_map = {
        "jsmith": 1,
        "edavis": 2
    }
    admin_username = "group7"
    
    # Generate physician ID based on username
    if username == admin_username:
        physician_id = None
    elif username in physician_id_map:
        physician_id = physician_id_map[username]

#Patient form button
    if 'show_patient_form' not in st.session_state:
        st.session_state.show_patient_form = False
        
    if not st.session_state.show_patient_form:
        if st.button("Fill Patient History"):
            st.session_state.show_patient_form = True

#Patient form structure
    if st.session_state.show_patient_form:
        
        #generate visit id
        with st.form("patient_med_form"):
            if 'new_visit_id' in locals():
                st.write(f"Visit ID: {new_visit_id}")
            else:
                st.error("new_visit_id is not defined. Please run the initialization cell first.")

            if 'new_patient_id' in locals():
                st.write(f"Patient ID: {new_patient_id}")
            else:
                st.error("new_patient_id is not defined. Please run the initialization cell first.")
            
            st.header("Patient Information")
            first_name = st.text_input("First Name")
            last_name = st.text_input("Last Name")
            parent_first_name = st.text_input(" Parent First Name")
            parent_last_name = st.text_input(" Parent Last Name")
            dob = st.date_input("Date of Birth", value=datetime.date(2000, 1, 1),  min_value=min_dob, max_value=max_dob)
            age= st.number_input("age", min_value=0.0, max_value=100.0, value=0.0)
            
            sex = st.selectbox("Sex",["Select","male", "female"])
            address = st.text_input("Address")
            phone = st.text_input("Phone Number")
            email = st.text_input("Email")
            has_insurance = st.selectbox("Has Insurance?",["Select", "yes", "no"])
            
            st.header("Vitals")
            body_temperature = st.number_input("Body Temperature in Celsius")
            
            height = st.number_input("Height in cm", min_value=0.0, max_value=200.0, value=0.0)
            weight = st.number_input("Weight in kgs",min_value=0.0, max_value=100.0, value=0.0)

            #BMI Calculator
            if st.form_submit_button("Calculate BMI"):
                bmi = calc_BMI(height,weight) if height and weight else None
                st.session_state["calculated_bmi"] = bmi
                
            bmi_display = st.session_state.get("calculated_bmi", "")
            st.text_input("BMI (auto-calculated or enter manually)", value=bmi_display, key="bmi_input")
            
            st.header("Family Medical History")
            family_history = st.text_area("Family history of major illnesses (heart disease, diabetes, cancer, etc.)")
                
            st.header("Reason for visit")
            concern = st.text_area("Primary Complaint")
            #if concern.lower() = "appendicitis":

            st.header("Medical History")
            conditions = st.text_area("Previous/Current Medical Conditions")
            allergies = st.text_area("Allergies (medication, food, etc.)")
            medications = st.text_area("Current Medications (separate by comma)")
            surgeries = st.text_area("Past Surgeries or Hospitalizations (with year)")
            physician = st.text_input("Current PCP")
        
            st.header("Clinical Assessment")
            migratory_pain = st.selectbox("Migratory Pain",["select one","yes", "no"])
            lower_right_abd_pain = st.selectbox("Pain in the Lower Right Abdomen",["select one","yes", "no"])
            contralateral_rebound_tenderness = st.selectbox("Contralateral_Rebound_Tenderness",["select one","yes", "no"])
            ipsilateral_rebound_tenderness = st.selectbox("Ipsilateral_Rebound_Tenderness",["select one","yes", "no"])
            peritonitis = st.selectbox("Peritonitis",["select one","no", "localized","generalized"])
            coughing_pain = st.selectbox("Coughing_Pain",["select one","yes", "no"])
            psoas_sign = st.selectbox("Psoas_Sign",["select one","yes", "no"])
            nausea = st.selectbox("Nausea",["select one","yes", "no"])
            loss_of_appetite = st.selectbox("Loss of Appetite",["select one","yes", "no"])
            dysuria = st.selectbox("Dysuria",["select one","yes", "no"])
            stool = st.selectbox("Stool type",["select one","normal", "diarrhea","constipation"])
        
            st.header("Lab Tests")
            wbc_count = st.number_input("WBC_Count", min_value=0.0, max_value=40.0, value=0.0)
            rbc_count = st.number_input("RBC_Count",min_value=0.0, max_value=7.0, value=0.0)
            hemoglobin = st.number_input("Hemoglobin",min_value=0.0, max_value=25.00, value=0.0)
            rdw = st.number_input("RDW",min_value=0.0, max_value=100.0, value=0.0)
            thrombocyte_count = st.number_input("Thrombocyte_Count",min_value=0, max_value=600, value=0)
            neutrophil_percentage = st.number_input("Neutrophil_Percentage",min_value=0.0, max_value=100.00, value=00.0)
            neutrophilia = st.selectbox("Neutrophilia",["select one","yes", "no"])
            segmented_neutrophils = st.number_input("Segmented_Neutrophils",min_value=0.0, max_value=100.0, value=00.0)
            crp = st.number_input("CRP",min_value=0, max_value=300, value=0, step=1 )
            ketones_in_urine = st.selectbox("Ketones_in_Urine",["select one","no", "+","++","+++"])
            rbc_in_urine = st.selectbox("RBC_in_Urine",["select one","no", "+","++","+++"])
            wbc_in_urine = st.selectbox("WBC_in_Urine",["select one","no", "+","++","+++"])     

            submitted = st.form_submit_button("Done!")
            if submitted:
                #link with database
                with engine.begin() as conn:
                    

                    #INSERT data into patient table
                    conn.execute(
                        text("""
                INSERT INTO patient (patient_id, f_name, l_name, age, gender)
                VALUES (:patient_id, :first_name, :last_name, :age, :sex)
                """),
                        {"patient_id": new_patient_id, "first_name": first_name, "last_name": last_name, "age": age, "sex":sex})


                    #INSERT data into visit table                  
                    conn.execute(
                        text("""
                INSERT INTO visit (patient_id, visit_id, physician_id)
                VALUES (:patient_id, :visit_id, :physician_id)
                """),
                        {"patient_id": new_patient_id, "visit_id": new_visit_id, "physician_id": physician_id})
                    

                    #INSERT data into clinical table
                    conn.execute(
                        text("""
                INSERT INTO exam (clinical_id, peritonitis, migratory_pain, lower_right_abd_pain, 
                contralateral_rebound_tenderness, ipsilateral_rebound_tenderness, coughing_pain,
                psoas_sign, nausea, loss_of_appetite, body_temperature, dysuria, stool, visit_id)
                VALUES (:clinical_id, :peritonitis, :migratory_pain, :lower_right_abd_pain,
                :contralateral_rebound_tenderness, :ipsilateral_rebound_tenderness, :coughing_pain,
                :psoas_sign, :nausea, :loss_of_appetite, :body_temperature, :dysuria, :stool, :visit_id)
                """),
                        {"clinical_id": new_clinical_id, "peritonitis": peritonitis, "migratory_pain":migratory_pain, 
                         "lower_right_abd_pain":lower_right_abd_pain, "contralateral_rebound_tenderness":contralateral_rebound_tenderness, 
                         "ipsilateral_rebound_tenderness":ipsilateral_rebound_tenderness, "coughing_pain":coughing_pain, "psoas_sign":psoas_sign, 
                         "nausea":nausea, "loss_of_appetite":loss_of_appetite, "body_temperature":body_temperature, 
                         "dysuria":dysuria, "stool":stool,"visit_id":new_visit_id})

                    #INSERT data into lab table
                    conn.execute(
                        text("""
                INSERT INTO lab (lab_id, neutrophil_percentage, wbc_count, 
                neutrophilia, ketones_in_urine, rdw, hemoglobin, rbc_count, 
                rbc_in_urine, thrombocyte_count, wbc_in_urine, visit_id)
                VALUES (:lab_id, :neutrophil_percentage, :wbc_count, 
                :neutrophilia, :ketones_in_urine, :rdw, :hemoglobin, :rbc_count, 
                :rbc_in_urine, :thrombocyte_count, :wbc_in_urine, :visit_id)
                """),
                        {"lab_id":new_lab_id, "neutrophil_percentage":neutrophil_percentage, "wbc_count":wbc_count, 
                "neutrophilia":neutrophilia, "ketones_in_urine":ketones_in_urine, "rdw":rdw, "hemoglobin":hemoglobin, "rbc_count":rbc_count, 
                "rbc_in_urine":rbc_in_urine, "thrombocyte_count":thrombocyte_count, "wbc_in_urine":wbc_in_urine, "visit_id":new_visit_id})

                    #INSERT data into vital_sign table
                    conn.execute(
                        text("""
                INSERT INTO vital_sign (demographic_id, height, weight, 
                bmi, visit_id)
                VALUES (:demographic_id, :height, :weight, 
                :bmi, :visit_id)
                """),
                        {"demographic_id":new_demo_id, "height":height, "weight":weight, 
                         "bmi":int(st.session_state.get("calculated_bmi", 0)), "visit_id":new_visit_id})
                st.success(f"Patient history for {first_name} {last_name} saved!")

        if st.button("let's Predict Diagnosis!"):
            st.session_state["latest_visit_id"] = last_visit_id
            st.session_state["first_name"] = first_name
            st.session_state["last_name"] = last_name
            st.switch_page("pages/Prediction.py")           

#login error message
elif authentication_status is False:
    st.error("Username/password is incorrect")
elif st.session_state.get("authentication_status") is None:
    st.warning("Please enter your username and password")
