# Medical_Insurance_Cost_Prediction-Streamlit

## Project Structure

|-- insurance_model.pkl # Saved model using Pickle |-- insurance_app.py # Streamlit application code |-- README.md # Project documentation |-- requirements.txt # Required Python packages |-- Dataset/ |-- insurance.csv # Dataset for training


## Features
- Interactive web-based application using **Streamlit**.
- Predicts insurance charges based on user inputs.
- Uses **ColumnTransformer** and **Pipeline** for efficient preprocessing.
- Trained model saved as a `.pkl` file for deployment and reusability.

## Dataset
The project uses the `insurance.csv` dataset with the following features:
- `age`: Age of the policyholder.
- `sex`: Gender of the policyholder (`male` or `female`).
- `bmi`: Body Mass Index.
- `children`: Number of children or dependents.
- `smoker`: Smoking status (`yes` or `no`).
- `region`: Residential region (`southeast`, `southwest`, `northeast`, `northwest`).
- `charges`: Insurance charges (target variable).
