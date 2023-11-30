
# EconysdCodeWebApp

EconysdCodeWebApp is a Flask-based web application that integrates with the OpenAI API to analyze and optimize Python code. It's designed to provide users with insights on their code's efficiency and suggest optimized versions for better performance and lower energy consumption. Additionally, the app estimates the CO2 emissions associated with running the original and optimized code.

## Features

- **Code Analysis and Optimization**: Users can submit Python code, which is then analyzed and optimized for efficiency.
- **CO2 Emissions Estimation**: The app estimates the CO2 emissions for both the original and optimized code, aiding in understanding the environmental impact.
- **Integration with OpenAI API**: Leverages the power of OpenAI's GPT-4 model for code analysis and optimization suggestions.
- **User-Friendly Interface**: Simple and intuitive interface for submitting code and viewing results.

## Getting Started

To get started with EcoCodeWebApp, you need to have Python installed on your system. Follow these steps to run the app locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/TYPW1/EcoCodeWebApp.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd EcoCodeWebApp
   ```

3. **Install Dependencies**:
   ```bash
   pip install flask openai codecarbon
   ```

4. **Set Up OpenAI API Key**:
   Ensure you have an API key from OpenAI. Set it as an environment variable:
   ```bash
   export OPENAI_API_KEY='your_api_key_here'
   ```

5. **Run the Flask App**:
   ```bash
   python app.py
   ```

6. **Access the Web App**:
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- On the web page, input the Python code you want to analyze and optimize in the provided text area.
- Submit the code to receive the analysis results, optimized code, and estimated CO2 emissions.

## Contributions

Contributions to the EconysdCodeWebApp are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

## License

This project is open-sourced under the MIT License. See the [LICENSE](LICENSE) file for details.

---

_EcoCodeWebApp - Making code optimization and environmental impact awareness more accessible._
