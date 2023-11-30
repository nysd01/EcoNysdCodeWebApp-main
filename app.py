from flask import Flask, render_template, request
from openai import OpenAI

client = OpenAI(api_key='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')
from codecarbon import EmissionsTracker



app = Flask(__name__)

def analyze_code(code):
    try:
        response = client.chat.completions.create(model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Check this code for errors: \n{code}"}
        ])
        return response.choices[0].message.content
    except Exception as e:
        return str(e)
    
def optimize_code(code):
    try:
        response = client.chat.completions.create(model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Optimize this code for better efficiency and lower energy consumption: \n{code}"}
        ])
        optimized_response = response.choices[0].message.content
        print("Optimized Response:", optimized_response)  # Temporary print statement
        return optimized_response
    except Exception as e:
        return str(e)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_code = request.form['code_input']
        print("User Code:", user_code)

        # Remove the error check and directly proceed to optimization
        print("Optimizing code...")
        optimized_code = optimize_code(user_code)
        print("Optimized Code:", optimized_code)

        # Hypothetical CO2 Emission Calculation (for demo purposes)
        tracker = EmissionsTracker()
        tracker.start()
        # Simulate processing of user's original code
        emissions_original = tracker.stop()

        tracker.start()
        # Simulate processing of optimized code
        emissions_optimized = tracker.stop()

        return render_template('index.html', original_code=user_code, optimized_code=optimized_code, emissions_original=emissions_original, emissions_optimized=emissions_optimized)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

