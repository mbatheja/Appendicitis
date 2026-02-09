# Diagnosis Support System (DSS)
This project is a decision support system designed to predict the likelihood of appendicitis in patients based on various demographic, clinical, and laboratory features. It includes a machine learning pipeline for classification and a web-based user interface for data entry and prediction.

## Project Structure
<li> lab_data_eda.ipynb: Focused on the EDA and cleaning of laboratory data (Neutrophil %, WBC Count, Ketones). </li>

<li> Clin_data_EDA.ipynb: Dedicated to EDA of clinical symptoms (Body Temperature, Migratory Pain, etc.). </li>

<li> classification.ipynb: The primary development notebook for model comparison (Random Forest, Gradient Boosting, XGBoost). </li>

<li> diagnosis_pipeline.pkl: Serialized scikit-learn pipeline containing the final model and preprocessing steps. </li>

<li> login+form.py: Streamlit application for patient data entry and database storage. </li>

<li> Prediction.py: Streamlit interface for retrieving and recording diagnostic outcomes. </li>

<li> app.py: Flask REST API serving as the bridge between the database and the model. </li>

<li> preprocess.py: Utility script for data retrieval, imputation, and feature formatting. </li>

<li> db_config.py: Configuration for the SQLAlchemy engine and PostgreSQL connection. </li>

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

## Contributors
Feinong Lyu: Exploratory Data Analysis, Modelling, SQL database design, Pipeline automation.

Mahima Batheja: Exploratory Data Analysis, Modelling and interpretability, Front End development.

Jon Hellner: Exploratory Data Analysis and Data Cleaning, Exploration of unsupervised models, Documentation.
