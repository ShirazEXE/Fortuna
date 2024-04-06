import pymongo

class FinancialRatios:
    def __init__(self, current_ratio, quick_ratio, debt_to_equity_ratio, interest_coverage_ratio, profit_margin_ratio, roa_ratio, roe_ratio):
        self.current_ratio = current_ratio
        self.quick_ratio = quick_ratio
        self.debt_to_equity_ratio = debt_to_equity_ratio
        self.interest_coverage_ratio = interest_coverage_ratio
        self.profit_margin_ratio = profit_margin_ratio
        self.roa_ratio = roa_ratio
        self.roe_ratio = roe_ratio

    def save_to_mongodb(self):
        try:
            client = pymongo.MongoClient("mongodb://localhost:27017/hackbyte")
            #mongodb+srv://samarthgayakhe:NtnwJTLzxFInAYAb@cluster0.t2zw5ra.mongodb.net/
            db = client['test']
            col = db['test']
            data = {
                "current_ratio": self.current_ratio,
                "quick_ratio": self.quick_ratio,
                "debt_to_equity_ratio": self.debt_to_equity_ratio,
                "interest_coverage_ratio": self.interest_coverage_ratio,
                "profit_margin_ratio": self.profit_margin_ratio,
                "roa_ratio": self.roa_ratio,
                "roe_ratio": self.roe_ratio
            }
            print(data)
            col.insert_one(data)
            print("Financial ratios inserted into MongoDB successfully")
        except Exception as e:
            print(f"Error inserting financial ratios into MongoDB: {str(e)}")
