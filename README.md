# Fortuna

Fortuna is a financial assessment tool that analyzes financial ratios and provides personalized financial advice using AI.

## Features

- Calculates key financial ratios based on user input
- Assesses financial condition (Good, Fair, or Poor)
- Provides recommendations based on the financial assessment
- Stores financial data in MongoDB
- Generates personalized financial advice using the Anthropic API

## Technologies Used

- Python
- Flask
- MongoDB
- Anthropic API (Claude model)
- JSON for data storage

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/ShirazEXE/Fortuna.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up MongoDB:
   - Install MongoDB if not already installed
   - Start the MongoDB service

4. Set up the Anthropic API:
   - Obtain an API key from Anthropic
   - Set the API key in the `app.py` file:
     ```python
     os.environ['ANTHROPIC_API_KEY'] = "your_api_key_here"
     ```

## Usage

1. Start the Flask server:
   ```
   python app.py
   ```

2. Send POST requests to the following endpoints:
   - `/assess_financial_condition`: Assess financial condition based on provided financial data
   - `/get_suggestion`: Get personalized financial advice based on salary, savings, and job information

## Project Structure

- `app.py`: Main Flask application
- `financial_assessment.py`: Contains logic for assessing financial condition
- `financial_model.py`: Defines the FinancialRatios model and MongoDB interaction
- `mongodb_data_upload.py`: Script for uploading data to MongoDB
- `mongo_data.py`: Script for sending data to the Flask app and storing in MongoDB

## Contributing

Contributions to Fortuna are welcome! Please feel free to submit a Pull Request.

## License

The GNU General Public License v3.0
