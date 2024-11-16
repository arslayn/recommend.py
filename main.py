from flask import Flask, render_template, request
import pandas as pd

# Load the dataset
df = pd.read_csv("college_evaluation_dataset.csv")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/find_colleges', methods=['POST'])
def find_colleges():
    # Get user inputs from the form
    accreditation = request.form.get('accreditation') == 'yes'
    preferred_fees = request.form.get('preferred_fees')
    preferred_location = request.form.get('preferred_location').lower()
    desired_courses = int(request.form.get('desired_courses'))
    desired_safety = request.form.get('desired_safety') == 'yes'

    # Prepare requirements dictionary
    requirements = {
        "accreditation": accreditation,
        "preferred_fees": preferred_fees,
        "preferred_location": preferred_location,
        "desired_courses": desired_courses,
        "desired_safety": desired_safety,
    }

    suggested_colleges = suggest_colleges(requirements)

    return render_template('results.html', colleges=suggested_colleges)

def suggest_colleges(requirements):
    filtered_df = df.copy()

    if requirements['accreditation']:
        filtered_df = filtered_df[filtered_df['Accreditation'] == 1]

    if requirements['preferred_fees'] != "Any":
        filtered_df['Fees'] = filtered_df['Fees'].str.lower()
        filtered_df = filtered_df[filtered_df['Fees'].str.lower() == requirements['preferred_fees'].lower()]

    if requirements['preferred_location'] != "any":
        filtered_df['State'] = filtered_df['State'].str.lower()
        filtered_df = filtered_df[filtered_df['State'] == requirements['preferred_location']]

    filtered_df = filtered_df[filtered_df['Courses'] >= requirements['desired_courses']]

    if requirements['desired_safety']:
        filtered_df = filtered_df[filtered_df['Safety'] == 'Secure']
    else:
        filtered_df = filtered_df[filtered_df['Safety'] == 'Insecure']

    return filtered_df

if __name__ == '__main__':
    app.run(debug=True)
