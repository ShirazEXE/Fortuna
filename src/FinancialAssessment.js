import React, { useEffect } from 'react';

const FinancialAssessment = ({ financialData }) => {
  useEffect(() => {
    alert('Welcome to the Financial Assessment page!');
  }, []);

  if (!financialData) {
    return <div>Loading...</div>;
  }

  const { financial_condition, recommendations } = financialData;

  return (
    <div>
      <h2>Financial Assessment</h2>
      <div>
        <h3>Financial Condition: {financial_condition}</h3>
        <h4>Recommendations:</h4>
        <ul>
          {recommendations.map((recommendation, index) => (
            <li key={index}>{recommendation}</li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default FinancialAssessment;