import pandas as pd
from db_config import get_db_engine

def get_features_from_db(visit_id):
    engine = get_db_engine()
    sql = f"""
        Select Neutrophil_Percentage, Body_Temperature, WBC_Count, Lower_Right_Abd_Pain, Age, Peritonitis, BMI, Gender, Neutrophilia, Contralateral_Rebound_Tenderness, Loss_of_Appetite
          FROM patient JOIN visit v USING(patient_id)
                       JOIN exam USING(visit_id)
                       JOIN lab USING (visit_id)
                       JOIN vital_sign USING(visit_id)
         WHERE v.visit_id = {visit_id};
    """
    df = pd.read_sql(sql, con=engine)
    # df = df.replace({'yes': 1, 'no': 0, 'female': 0, 'male': 1})
    df = df.fillna(0)
    df.rename(columns={
        'age': 'Age',
        'bmi': 'BMI',
        'gender': 'Sex',
        'body_temperature': 'Body_Temperature',
        'peritonitis': 'Peritonitis',
        'wbc_count': 'WBC_Count',
        'neutrophil_percentage': 'Neutrophil_Percentage',
        'neutrophilia': 'Neutrophilia',
        'lower_right_abd_pain': 'Lower_Right_Abd_Pain',
        'contralateral_rebound_tenderness': 'Contralateral_Rebound_Tenderness',
        'loss_of_appetite': 'Loss_of_Appetite'
    }, inplace=True)
    feature_order = [
        'Age', 'BMI', 'Sex', 'Neutrophil_Percentage', 'WBC_Count', 'Neutrophilia',
        'Peritonitis', 'Lower_Right_Abd_Pain', 'Contralateral_Rebound_Tenderness',
        'Loss_of_Appetite', 'Body_Temperature'
    ]
    df = df[feature_order]

    return df

if __name__ == "__main__":
    d = get_features_from_db(1);
    print(d.columns)
