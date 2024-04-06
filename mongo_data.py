import time
import requests
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb+srv://samarthgayakhe:NtnwJTLzxFInAYAb@ac-owusixi-shard-00-01.e1boifc.mongodb.net/test?retryWrites=true&w=majority')
db = client['financial_assessment']
collection = db['user_assessments']

def send_data_to_flask(data):
    try:
        # Send data to the Flask app to get calculated ratios
        url = 'http://localhost:5000/assess_financial_condition'
        response = requests.post(url, json=data)
        response_data = response.json()
        print(f"Response from Flask app: {response_data}")

        if 'error' in response_data:
            print(f"Error from Flask app: {response_data['error']}")
            return None

        assessment = response_data.get('financial_condition')
        recommendations = response_data.get('recommendations')
        ratios = response_data.get('ratios')

        if not assessment or not recommendations or not ratios:
            print("Invalid response from Flask app")
            return None

        # Store the data in MongoDB
        user_data = {
            'user_id': data['user_id'],
            'cash': data['cash'],
            'accounts_receivable': data['accounts_receivable'],
            'accounts_payable': data['accounts_payable'],
            'short_term_loans': data['short_term_loans'],
            'revenue': data['revenue'],
            'net_income': data['net_income'],
            'total_assets': data['total_assets'],
            'total_equity': data['total_equity'],
            'interest_paid': data['interest_paid'],
            'ratios': ratios,
            'financial_condition': assessment,
            'recommendations': recommendations
        }
        result = collection.update_one(
            {'user_id': data['user_id']},
            {'$set': user_data},
            upsert=True
        )
        return str(result.upserted_id)
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def main():
    # Dummy data for testing
    data = {
        'user_id': 'user_123',
        'cash': '10000',
        'accounts_receivable': '5000',
        'accounts_payable': '3000',
        'short_term_loans': '2000',
        'revenue': '100000',
        'net_income': '20000',
        'total_assets': '150000',
        'total_equity': '100000',
        'interest_paid': '5000',
    }

    while True:
        document_id = send_data_to_flask(data)
        if document_id:
            print(f"Data stored in MongoDB with document ID: {document_id}")
        else:
            print("Failed to store data in MongoDB")

        # Wait for 5 seconds before sending the data again
        time.sleep(5)

if __name__ == '__main__':
    main()