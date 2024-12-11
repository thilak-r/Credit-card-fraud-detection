# Credit Card Fraud Detection 💳

## **Project Overview**
This project leverages machine learning techniques to identify fraudulent credit card transactions from a dataset of financial activities. By using advanced algorithms and data preprocessing techniques, this project aims to provide an efficient and accurate solution for detecting fraudulent transactions.

---

## **Key Features**
- **Fraud Detection**: Classifies transactions as either **Fraudulent** or **Legitimate**.
- **Machine Learning Models**: Employs various models like **Logistic Regression**, **Random Forest**, and **Gradient Boosting** to achieve high accuracy.
- **Performance Metrics**: Includes confusion matrix, classification report, ROC curve, and AUC score for model evaluation.
- **Imbalanced Data Handling**: Uses techniques such as **SMOTE** (Synthetic Minority Over-sampling Technique) and **class weighting** to address class imbalance in the dataset.
- **Scalable System**: Code structure designed for scalability and easy integration with other applications.

---

## **Technologies Used**

| **Technology**       | **Description**                                                        |
|-----------------------|------------------------------------------------------------------------|
| **Python**           | Core programming language for data preprocessing and model development |
| **Scikit-Learn**     | Machine learning library for implementing and evaluating models        |
| **Pandas/Numpy**     | For data manipulation and analysis                                     |
| **Matplotlib/Seaborn**| Data visualization for performance evaluation                         |
| **Flask**            | Lightweight web framework for deploying the model as a web service     |

---

## **Dataset**
The dataset used contains anonymized transaction details with the following features:
- **Time**: Seconds elapsed between the transaction and the first transaction in the dataset.
- **V1-V28**: Principal components obtained using PCA for dimensionality reduction.
- **Amount**: Transaction amount.
- **Class**: Target variable where `0` indicates a legitimate transaction and `1` indicates fraud.

The dataset is highly imbalanced, with only ~0.17% of transactions being fraudulent.

---

## **Project Structure**

```plaintext
.
├── app.py                # Backend Flask application
├── logistic_regression_model_2.pkl      # model
├── templates/            # Folder containing HTML templates
│   └── index.html        # Main HTML file for the user interface
├── requirements.txt      # Python dependencies for the project
├── README.md             # Project documentation
└── Credit Card.ipynb            # Jupyter notebooks for EDA and model training
```

---

## 🚀 **How to Run This Project**
1. Clone the repository:
   ```bash
   git clone https://github.com/thilak-r/Credit-card-fraud-detection.git
   cd Credit-card-fraud-detection

2. Install Dependencies: 
Run the following command to install all required dependencies:
   ```bash 
   pip install -r requirements.txt

3. Run the Flask App
Start the Flask application by running:
   ```bash
   python app.py

4. Open Your Browser
Navigate to the following address in your web browser to access the application:
   ```bash
   http://127.0.0.1:5000

   
---
## ❤️ Thank You!
Thank you for checking out our project! We hope this inspires you to explore the intersection of AI and healthcare. Feel free to reach out for questions, suggestions, or collaborations.

---

<br><br>
under guidance of [Dr Agughasi Victor Ikechukwu](https://github.com/Victor-Ikechukwu)
