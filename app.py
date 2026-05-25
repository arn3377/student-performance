from flask import Flask, render_template, request

app = Flask(__name__)

# Route 1: Serves up the baseline HTML data form setup layout
@app.route('/')
def home():
    return render_template('index.html')

# Route 2: Processes incoming user metrics and renders the custom summary dashboard
@app.route('/predict', methods=['POST'])
def predict():
    # Capture incoming metric features sent over from the HTML elements
    study_hours = request.form.get('study_hours')
    attendance = request.form.get('attendance')
    assignments = request.form.get('assignments_completed')
    sleep_hours = request.form.get('sleep_hours')
    previous_score = request.form.get('previous_score')
    
    # -----------------------------------------------------------------
    # PLACEHOLDER: Run your actual ML model array parsing math arrays here
    # e.g., output = model.predict([[study_hours, attendance, ...]])
    calculated_prediction = 92.4 
    # -----------------------------------------------------------------

    # Load result.html page and map your variable name directly to it
    return render_template('result.html', prediction=calculated_prediction)

if __name__ == '__main__':
    app.run(debug=True)