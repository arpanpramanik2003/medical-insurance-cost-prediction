# 🏥 Medical Insurance Cost Prediction

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-FF4B4B.svg)](https://streamlit.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-F7931E.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> A machine learning web application that predicts medical insurance costs based on personal and demographic factors using advanced regression techniques.

![Medical Insurance Cost Prediction](medical.jpg)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Model Details](#model-details)
- [Installation](#installation)
- [Usage Instructions](#usage-instructions)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🔍 Overview

The **Medical Insurance Cost Prediction** project is an interactive web application built with **Streamlit** that leverages machine learning to estimate medical insurance charges. By analyzing key factors such as age, BMI, smoking status, number of children, gender, and region, the application provides accurate cost predictions to help individuals and insurance providers make informed decisions.

This project demonstrates end-to-end machine learning workflow including:
- Data preprocessing and feature engineering
- Model training and evaluation
- Model serialization and deployment
- Interactive web interface development

---

## ✨ Features

- 🎯 **Accurate Predictions**: Uses trained regression models to estimate insurance costs
- 🌐 **Interactive Web Interface**: User-friendly Streamlit application for easy interaction
- ⚙️ **Robust Preprocessing**: Implements ColumnTransformer and Pipeline for efficient data handling
- 💾 **Model Persistence**: Trained model saved as `.pkl` file for deployment and reusability
- 📊 **Real-time Results**: Instant predictions based on user inputs
- 🔧 **Flexible Architecture**: Modular code structure for easy maintenance and updates
- 📈 **Comprehensive Analysis**: Considers multiple factors including demographic and health indicators

---

## 🎬 Demo

### How It Works:

1. **Input Personal Information**: Enter details like age, gender, BMI, number of children, smoking status, and region
2. **Get Instant Prediction**: Click the predict button to receive estimated insurance costs
3. **View Results**: See your predicted medical insurance charges displayed clearly

### Sample Prediction:

```
Inputs:
- Age: 35
- Sex: Male
- BMI: 27.5
- Children: 2
- Smoker: No
- Region: Northwest

Predicted Insurance Cost: $5,234.67
```

---

## 📁 Project Structure

```
medical-insurance-cost-prediction/
│
├── Dataset/
│   └── insurance.csv          # Training dataset
│
├── insurance_model.pkl         # Serialized trained model (Pickle)
├── insurance_app.py            # Streamlit application code
├── medical.jpg                 # Project banner image
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
└── LICENSE                     # License file
```

### File Descriptions:

- **insurance_model.pkl**: Pre-trained machine learning model saved using Pickle for predictions
- **insurance_app.py**: Main Streamlit application containing UI and prediction logic
- **Dataset/insurance.csv**: Historical insurance data used for model training
- **requirements.txt**: List of required Python packages and their versions

---

## 📊 Dataset

The project uses the **insurance.csv** dataset containing medical insurance information with the following features:

### Features:

| Feature | Type | Description | Example Values |
|---------|------|-------------|----------------|
| **age** | Numerical | Age of the policyholder | 18-64 years |
| **sex** | Categorical | Gender of the policyholder | male, female |
| **bmi** | Numerical | Body Mass Index (kg/m²) | 15.96-53.13 |
| **children** | Numerical | Number of dependents | 0-5 |
| **smoker** | Categorical | Smoking status | yes, no |
| **region** | Categorical | Residential region in the US | northeast, northwest, southeast, southwest |
| **charges** | Numerical | Medical insurance costs (Target) | $1,121.87-$63,770.43 |

### Dataset Statistics:

- **Total Records**: ~1,338 entries
- **Features**: 6 input features + 1 target variable
- **Missing Values**: None
- **Data Types**: Mixed (numerical and categorical)

---

## 🤖 Model Details

### Machine Learning Pipeline:

The project implements a comprehensive ML pipeline with the following components:

#### 1. **Preprocessing**

- **Numerical Features** (age, bmi, children):
  - Standard scaling using StandardScaler
  - Normalization for consistent ranges

- **Categorical Features** (sex, smoker, region):
  - One-Hot Encoding for categorical conversion
  - Binary encoding for gender and smoking status

#### 2. **Model Architecture**

- **Algorithm**: Linear Regression / Random Forest / Gradient Boosting (specify your model)
- **Pipeline**: ColumnTransformer + Regression Model
- **Training Strategy**: Train-test split (80-20)

#### 3. **Model Performance**

```
Model Evaluation Metrics:
- R² Score: 0.XX (specify your score)
- Mean Absolute Error (MAE): $X,XXX.XX
- Root Mean Squared Error (RMSE): $X,XXX.XX
```

#### 4. **Model Serialization**

- Trained model saved using Python's Pickle library
- Ensures consistency between training and deployment
- Fast loading and prediction times

---

## 🚀 Installation

### Prerequisites:

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Step-by-Step Installation:

1. **Clone the Repository**

```bash
git clone https://github.com/arpanpramanik2003/medical-insurance-cost-prediction.git
cd medical-insurance-cost-prediction
```

2. **Create Virtual Environment** (Optional but Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Verify Installation**

```bash
python -c "import streamlit; import sklearn; import pandas; print('All packages installed successfully!')"
```

---

## 💻 Usage Instructions

### Running the Application:

1. **Navigate to Project Directory**

```bash
cd medical-insurance-cost-prediction
```

2. **Launch Streamlit App**

```bash
streamlit run insurance_app.py
```

3. **Access the Application**

- The app will automatically open in your default web browser
- Default URL: `http://localhost:8501`
- If it doesn't open automatically, navigate to the URL manually

### Using the Web Interface:

1. **Enter Your Information**:
   - Age: Select your age using the slider or input box
   - Gender: Choose Male or Female
   - BMI: Enter your Body Mass Index
   - Children: Number of dependents covered
   - Smoker Status: Select Yes or No
   - Region: Choose your residential region

2. **Get Prediction**:
   - Click the "Predict Insurance Cost" button
   - View your estimated insurance charges

3. **Try Different Scenarios**:
   - Modify inputs to see how different factors affect costs
   - Compare predictions for various demographic profiles

---

## 📦 Requirements

### Core Dependencies:

```txt
streamlit>=1.0.0
scikit-learn>=1.0.0
pandas>=1.3.0
numpy>=1.21.0
pickle-mixin>=1.0.0
```

### Full Requirements:

See `requirements.txt` for a complete list of dependencies with specific versions.

### System Requirements:

- **OS**: Windows 10+, macOS 10.14+, or Linux
- **RAM**: Minimum 4GB (8GB recommended)
- **Storage**: At least 500MB free space
- **Internet**: Required for initial package installation

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help improve this project:

### Ways to Contribute:

1. **Report Bugs**: Open an issue describing the bug and how to reproduce it
2. **Suggest Features**: Share ideas for new features or improvements
3. **Submit Pull Requests**: Fix bugs or implement new features
4. **Improve Documentation**: Help make the docs clearer and more comprehensive
5. **Share Feedback**: Let us know how you're using the project

### Contribution Guidelines:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Make your changes and commit (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

### Code Standards:

- Follow PEP 8 style guidelines for Python code
- Add comments and docstrings for new functions
- Update documentation for significant changes
- Test your changes before submitting

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### MIT License Summary:

- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Private use allowed
- ❌ Liability and warranty not provided

---

## 📧 Contact

### Project Maintainer:

**Arpan Pramanik**

- 🐙 GitHub: [@arpanpramanik2003](https://github.com/arpanpramanik2003)
- 📧 Email: [Your Email] (Add your email if you wish to share)
- 💼 LinkedIn: [Your LinkedIn] (Add your LinkedIn profile if available)

### Support:

- For bug reports and feature requests, please [open an issue](https://github.com/arpanpramanik2003/medical-insurance-cost-prediction/issues)
- For general questions, feel free to reach out via GitHub discussions

---

## 🙏 Acknowledgments

- Dataset source: [Kaggle Medical Cost Personal Dataset](https://www.kaggle.com/)
- Built with [Streamlit](https://streamlit.io/)
- Machine learning powered by [scikit-learn](https://scikit-learn.org/)
- Thanks to all contributors and users of this project

---

## 🔮 Future Enhancements

- [ ] Add more regression models for comparison
- [ ] Implement model performance visualization
- [ ] Add data visualization dashboard
- [ ] Deploy on cloud platforms (Heroku, AWS, Azure)
- [ ] Add model retraining capability
- [ ] Implement API endpoints for programmatic access
- [ ] Add user authentication and history tracking
- [ ] Create mobile-responsive design improvements

---

<div align="center">

**⭐ If you find this project helpful, please consider giving it a star! ⭐**

**Made with ❤️ by Arpan Pramanik**

</div>
