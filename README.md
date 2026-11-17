# Diagnosis Support System (DSS)
This project is a decision support system designed to predict the likelihood of appendicitis in patients based on various demographic, clinical, and laboratory features. It includes a machine learning pipeline for classification and a web-based user interface for data entry and prediction.

## Project Structure
```
├── app/                         # Web application
│   ├── Home.py                  # Streamlit app: login + patient data entry
│   ├── pages/Prediction.py      # Streamlit page: fetch and record diagnoses
│   ├── app.py                   # Flask REST API serving model predictions
│   ├── preprocess.py            # Pulls a visit's features from the database
│   ├── db_config.py             # Database connection (reads DATABASE_URL)
│   ├── .env.example             # Template for app/.env (database URL)
│   ├── credentials.example.yml  # Template for app/credentials.yml (login users)
│   ├── start_project.py         # Starts Streamlit and Flask together
│   ├── models/diagnosis_pipeline.pkl   # Trained scikit-learn pipeline
│   ├── database/full_backup.sql # PostgreSQL schema + sample data
│   └── tools/hash_passwords.ipynb      # Helper to generate password hashes
├── data/
│   ├── app_data.xlsx            # Raw pediatric appendicitis dataset
│   └── complete_data.csv        # Cleaned dataset (built by notebook 04)
├── notebooks/                   # Analysis, in rough order
│   ├── 01_demographic_eda.ipynb
│   ├── 02_clinical_eda.ipynb    # Clinical symptoms (temperature, migratory pain, ...)
│   ├── 03_lab_eda.ipynb         # Lab values (neutrophil %, WBC count, ketones)
│   ├── 04_build_complete_data.ipynb
│   ├── 05_clustering.ipynb      # Unsupervised exploration
│   ├── 06_classification.ipynb  # Model comparison (RF, gradient boosting, XGBoost) + SHAP
│   ├── 07_final_model.ipynb     # Trains and exports the final pipeline
│   └── archive/                 # Superseded versions kept for reference
├── docs/                        # Final report and presentation
└── requirements.txt
```

## Machine Learning Pipeline & Explainability
The project utilizes a structured machine learning pipeline to ensure consistent data transformation and robust predictions.

### Pipeline Architecture
<li> Preprocessing: Automatically applies StandardScaler to numerical features (Age, BMI, WBC Count) and OneHotEncoder to categorical features (Sex, Peritonitis). </li>

<li> Imputation: KNNImputer handles missing data within clinical and lab records. </li>

<li> Model Selection: Production typically utilizes XGBClassifier or Random Forest for optimal predictive performance. </li>

### Model Explainability with SHAP
To ensure clinical transparency, the project incorporates SHAP (SHapley Additive exPlanations) to interpret model decisions. This allows medical professionals to:

<li> Identify Key Drivers: Understand which features (e.g., high WBC Count) most heavily influenced a specific patient's prediction. </li>

<li> Local Explanations: Visualize how individual clinical signs contribute to a patient's probability score. </li>

<li> Global Importance: Rank the overall importance of features across the entire dataset to validate logic against medical standards. </li>

## Key Features
<li> Multimodal Data: Combines demographic, clinical, and laboratory data. </li>

<li> Database Integration: Real-time fetching from PostgreSQL for seamless clinical workflow. </li>

<li> Dual-Interface: Dedicated modules for data entry and diagnostic review. </li>

## Setup and Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set up PostgreSQL and load the schema: `psql -d DSS -f app/database/full_backup.sql`.
3. Create the two config files. Both are git-ignored, so they never get committed:
   ```bash
   cp app/.env.example app/.env
   cp app/credentials.example.yml app/credentials.yml
   ```
   - In `app/.env`, set `DATABASE_URL` to your database
     (e.g. `postgresql+psycopg2://user:pass@localhost:5432/DSS`).
   - In `app/credentials.yml`, add the login users and a random cookie key.
     Generate password hashes with `app/tools/hash_passwords.ipynb`.
4. Start the app from the `app/` folder:
   ```bash
   cd app
   python start_project.py
   ```
   or run the two parts separately: `flask run` (API on port 5000) and `streamlit run Home.py`.
5. Log in, enter patient data, then open the **Prediction** page to get the diagnosis.

Notebooks read from `data/`, so run them from inside `notebooks/`.

## Contributors
Feinong Lyu: Exploratory Data Analysis, Modelling, SQL database design, Pipeline automation.

Mahima Batheja: Exploratory Data Analysis, Modelling and interpretability, Front End development.

Jon Hellner: Exploratory Data Analysis and Data Cleaning, Exploration of unsupervised models, Documentation.
