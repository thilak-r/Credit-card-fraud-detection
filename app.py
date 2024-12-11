from flask import Flask, render_template, request
import numpy as np
import random  # Import random for generating random predictions

app = Flask(__name__)

# Define the feature columns (must match the form inputs)
feature_columns = ['amt', 'category_gas_transport', 'category_grocery_pos',
                   'category_personal_care', 'category_kids_pets', 'category_misc_pos',
                   'category_grocery_net', 'category_travel', 'category_health_fitness',
                   'category_food_dining', 'category_home', 'age', 'latitudinal_distance']

@app.route('/')
def home():
    return render_template('index.html', feature_columns=feature_columns)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user inputs from the form (this is for validation purposes only)
        input_data = [float(request.form[col]) for col in feature_columns]
    except ValueError:
        return "Invalid input. Please enter numeric values for all fields."

    # Generate a random prediction
    prediction = random.choice([0, 1])  # 0: Not Fraudulent, 1: Fraudulent
    confidence_score = round(random.uniform(60, 90), 2)  # Random confidence score between 60-90%

    # Map labels
    labels = ['Not Fraudulent', 'Fraudulent']

    return render_template('index.html',
                           feature_columns=feature_columns,
                           prediction=labels[prediction],
                           confidence_score=confidence_score)

if __name__ == '__main__':
    app.run(debug=True)
