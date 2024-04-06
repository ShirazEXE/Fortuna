from decimal import Decimal
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import datetime
from financial_model import FinancialRatios

app = Flask(__name__)
CORS(app)

def assess_financial_condition_logic(ratios):
    """
    This function assesses the financial condition based on provided ratios and returns a string representing the assessment and a list of recommendations.

    Args:
        ratios: A dictionary containing calculated financial ratios.

    Returns:
        A tuple containing the financial condition (string) and recommendations (list).
    """
    condition = ""
    recommendations = []

    current_ratio = ratios.get("current_ratio")
    quick_ratio = ratios.get("quick_ratio")
    debt_to_equity_ratio = ratios.get("debt_to_equity_ratio")
    interest_coverage_ratio = ratios.get("interest_coverage_ratio")
    profit_margin_ratio = ratios.get("profit_margin_ratio")
    roa_ratio = ratios.get("roa_ratio")
    roe_ratio = ratios.get("roe_ratio")

    current_ratio_threshold = 1.5
    quick_ratio_threshold = 1.0
    debt_to_equity_threshold = 0.5
    interest_coverage_threshold = 2.0
    profit_margin_threshold = 0.05
    roa_threshold = 0.03
    roe_threshold = 0.1

    if (current_ratio >= current_ratio_threshold
        and quick_ratio >= quick_ratio_threshold
        and debt_to_equity_ratio <= debt_to_equity_threshold
        and interest_coverage_ratio >= interest_coverage_threshold
        and profit_margin_ratio >= profit_margin_threshold
        and roa_ratio >= roa_threshold
        and roe_ratio >= roe_threshold):
        condition = "Good"
        recommendations = [
            "Maintain healthy financial position.",
            "Consider growth opportunities.",
            "Optimize investment strategies."
        ]
    elif (current_ratio >= 1
         and quick_ratio >= 0.8
         and debt_to_equity_ratio <= 1
         and interest_coverage_ratio >= 2
         and profit_margin_ratio >= 0.05
         and roa_ratio >= 0.03
         and roe_ratio >= 0.1):
        condition = "Fair"
        recommendations = [
            "Improve liquidity by reducing short-term liabilities.",
            "Increase cash flow and profitability.",
            "Explore opportunities to reduce debt burden."
        ]
    else:
        condition = "Poor"
        recommendations = [
            "Prioritize reducing short-term liabilities.",
            "Increase current assets and liquidity.",
            "Identify ways to improve profitability and efficiency."
        ]

    return condition, recommendations

def save_data_to_json(ratios):
    try:
        filename = 'financial_data.json'
        data_to_store = {
            "date": datetime.datetime.now().isoformat(),
            "current_ratio": float(ratios["current_ratio"]),
            "quick_ratio": float(ratios["quick_ratio"]),
            "debt_to_equity_ratio": float(ratios["debt_to_equity_ratio"]),
            "interest_coverage_ratio": float(ratios["interest_coverage_ratio"]),
            "profit_margin_ratio": float(ratios["profit_margin_ratio"]),
            "roa_ratio": float(ratios["roa_ratio"]),
            "roe_ratio": float(ratios["roe_ratio"])
        }

        with open(filename, 'w') as file:  # Open in write mode ('w') instead of append mode ('a')
            json.dump(data_to_store, file)
            file.write('\n')
            file.flush()

        print(f"Data saved to {filename}")
    except Exception as e:
        print(f"Error saving data to JSON file: {str(e)}")

def insert_financial_ratios():
    try:
        data_file_path = "./financial_data.json"
        with open(data_file_path, "r") as file:
            data = json.load(file)
        print(data)
        current_ratio = data.get('current_ratio')
        quick_ratio = data.get('quick_ratio')
        debt_to_equity_ratio = data.get('debt_to_equity_ratio')
        interest_coverage_ratio = data.get('interest_coverage_ratio')
        profit_margin_ratio = data.get('profit_margin_ratio')
        roa_ratio = data.get('roa_ratio')
        roe_ratio = data.get('roe_ratio')

        # Create an instance of FinancialRatios model
        financial_ratios = FinancialRatios(current_ratio, quick_ratio, debt_to_equity_ratio, interest_coverage_ratio, profit_margin_ratio, roa_ratio, roe_ratio)
        
        # Save financial ratios to MongoDB
        financial_ratios.save_to_mongodb()

        return jsonify({"message": "Financial ratios inserted successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/assess_financial_condition', methods=['POST'])
def assess_financial_condition():
    try:
        data = request.get_json()
        print("Received data:", data)

        cash = Decimal(data['cash'])
        accounts_receivable = Decimal(data['accounts_receivable'])
        current_assets = cash + accounts_receivable
        accounts_payable = Decimal(data['accounts_payable'])
        short_term_loans = Decimal(data['short_term_loans'])
        current_liabilities = accounts_payable + short_term_loans
        revenue = Decimal(data['revenue'])
        net_income = Decimal(data['net_income'])
        total_assets = Decimal(data['total_assets'])
        total_equity = Decimal(data['total_equity'])
        interest_paid = Decimal(data['interest_paid'])

        current_ratio = current_assets / current_liabilities
        quick_ratio = cash / current_liabilities
        debt_to_equity_ratio = (total_assets - total_equity) / total_equity
        interest_coverage_ratio = revenue / interest_paid
        profit_margin_ratio = net_income / revenue
        roa_ratio = net_income / total_assets
        roe_ratio = net_income / total_equity

        ratios = {
            "current_ratio": current_ratio,
            "quick_ratio": quick_ratio,
            "debt_to_equity_ratio": debt_to_equity_ratio,
            "interest_coverage_ratio": interest_coverage_ratio,
            "profit_margin_ratio": profit_margin_ratio,
            "roa_ratio": roa_ratio,
            "roe_ratio": roe_ratio
        }

        assessment, recommendations = assess_financial_condition_logic(ratios)
        save_data_to_json(ratios)
        insert_financial_ratios()

        return jsonify({
            "financial_condition": assessment,
            "recommendations": recommendations
        })
    except Exception as e:
        return jsonify({"error": str(e)})





if __name__ == '__main__':
    app.run(debug=True)