from flask import Flask, request, jsonify
from flask_cors import CORS
from decimal import Decimal
from financial_assessment import assess_financial_condition_logic

app = Flask(__name__)
CORS(app)
# Define your Flask routes and other app configurations below

@app.route('/assess_financial_condition', methods=['POST'])
def assess_financial_condition():
    try:
        data = request.get_json()


        print("Received data:", data)

        # Validate input data (consider using a schema for robustness)
        # ... (validation logic)

        # Extract financial data
        current_assets = Decimal(data['current_assets'])
        current_liabilities = Decimal(data['current_liabilities'])
        revenue = Decimal(data['revenue'])
        net_income = Decimal(data['net_income'])
        total_assets = Decimal(data['total_assets'])
        total_equity = Decimal(data['total_equity'])
        ebit = Decimal(data['ebit'])
        interest_expense = Decimal(data['interest_expense'])
        # Extract income and expense data
        gross_income = Decimal(data.get('gross_income'))  # Handle potential absence
        total_expenses = Decimal(data.get('total_expenses'))  # Handle potential absence

        # Calculate financial ratios
        current_ratio = CurrentRatio(current_assets, current_liabilities)
        quick_ratio = QuickRatio(current_assets, 0, 0, current_liabilities)  # Assuming no marketable securities or receivables for simplicity
        debt_to_equity_ratio = DebtToEquityRatio(total_liabilities, total_equity)
        interest_coverage_ratio = InterestCoverageRatio(ebit, interest_expense)
        profit_margin_ratio = ProfitMarginRatio(net_income, revenue)
        roa_ratio = ROARatio(net_income, total_assets)
        roe_ratio = ROERatio(net_income, total_equity)
        # Calculate additional ratios based on income and expenses
        gross_margin_ratio = GrossMarginRatio(gross_income, revenue).calculate() if gross_income else None
        operating_margin_ratio = OperatingMarginRatio(ebit, revenue).calculate()

        # Store calculated ratios in a dictionary
        ratios = {
            "current_ratio": current_ratio.calculate(),
            "quick_ratio": quick_ratio.calculate(),
            "debt_to_equity_ratio": debt_to_equity_ratio.calculate(),
            "interest_coverage_ratio": interest_coverage_ratio.calculate(),
            "profit_margin_ratio": profit_margin_ratio.calculate(),
            "roa_ratio": roa_ratio.calculate(),
            "roe_ratio": roe_ratio.calculate(),
            "gross_margin_ratio": gross_margin_ratio,
            "operating_margin_ratio": operating_margin_ratio,
        }


        return jsonify({
            "financial_condition": "Good",
            "recommendations": ["Maintain healthy financial position."],
            "ratios": {"current_ratio": 1.5, "debt_to_equity_ratio": 0.3}
        })

        # Assess the financial condition and get recommendations
        assessment, recommendations = assess_financial_condition_logic(ratios)

        # Return the assessment and recommendations as a JSON response
        return jsonify({
            "financial_condition": assessment,
            "recommendations": recommendations
        })

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)

