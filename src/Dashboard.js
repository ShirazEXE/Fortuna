import React, { useState } from 'react';
import axios from 'axios';
import './Dashboard.css'; // Import the CSS file for styling

const Dashboard = () => {
  const [formData, setFormData] = useState({
    cash: '',
    accounts_receivable: '',
    accounts_payable: '',
    short_term_loans: '',
    revenue: '',
    net_income: '',
    total_assets: '',
    total_equity: '',
    interest_paid: '',
  });
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  const [showInputs, setShowInputs] = useState(false); // State to manage visibility of input fields
  const [salary, setSalary] = useState('');
  const [savings, setSavings] = useState('');
  const [job, setJob] = useState('');
  const [suggestion, setSuggestion] = useState('');

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);

    try {
      const response = await axios.post(
        'http://localhost:5000/assess_financial_condition',
        formData
      );
      const { financial_condition, recommendations } = response.data;

      if (financial_condition && recommendations) {
        setResult({ financial_condition, recommendations });
        setShowInputs(true); // Show input fields when result is generated
      } else {
        setError('Invalid response from the API');
        console.error('Invalid response from the API:', response.data);
      }
    } catch (error) {
      setError('An error occurred. Please try again.');
      console.error('Error:', error);
    }
  };

  const handleSuggestions = async () => {
    try {
      const response = await axios.post('http://localhost:5000/get_suggestion', {
        salary,
        savings,
        job,
        ...formData // Include existing form data
      });
      const { suggestion } = response.data;
      setSuggestion(suggestion); // Update state with the received suggestion
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleLogout = () => {
    window.location.href = '/'; 
  };

  return (
    <div className="background ">
      <header className="container-fluid d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 mb-4 border-bottom">
        <div className="col-md-3 mb-2 mb-md-0">
          <a href="/" className="d-inline-flex link-body-emphasis text-decoration-none">
            <svg className="bi" width="40" height="32" role="img" aria-label="Bootstrap">
              <use xlinkHref="#bootstrap"></use>
            </svg>
            <h2>Financial Assessment</h2>
          </a>
        </div>
        <div className="col-md-3 text-end">
          <button type="button" className="btn btn-primary me-2" onClick={handleLogout}>
            Logout
          </button>
        </div>
      </header>
      <div className="dashboard-container">
        <div className="blur-overlay"></div>
        
        <div className="form-container">
          <form onSubmit={handleSubmit}>
            {/* Form fields for cash and accounts receivable (used for current ratio calculation) */}
            <label>
              Cash:
              <input
                type="number"
                name="cash"
                value={formData.cash}
                onChange={handleChange}
              />
            </label>
            {/* Other form fields for financial data */}
            <label>
              Accounts Receivable:
              <input
                type="number"
                name="accounts_receivable"
                value={formData.accounts_receivable}
                onChange={handleChange}
              />
            </label>
            <label>
              Accounts Payable:
              <input
                type="number"
                name="accounts_payable"
                value={formData.accounts_payable}
                onChange={handleChange}
              />
            </label>
            <label>
              Short-Term Loans:
              <input
                type="number"
                name="short_term_loans"
                value={formData.short_term_loans}
                onChange={handleChange}
              />
            </label>
            <label>
              Revenue:
              <input
                type="number"
                name="revenue"
                value={formData.revenue}
                onChange={handleChange}
              />
            </label>
            <label>
              Net Income:
              <input
                type="number"
                name="net_income"
                value={formData.net_income}
                onChange={handleChange}
              />
            </label>
            <label>
              Total Assets:
              <input
                type="number"
                name="total_assets"
                value={formData.total_assets}
                onChange={handleChange}
              />
            </label>
            <label>
              Total Equity:
              <input
                type="number"
                name="total_equity"
                value={formData.total_equity}
                onChange={handleChange}
              />
            </label>
            <label>
              Interest Paid:
              <input
                type="number"
                name="interest_paid"
                value={formData.interest_paid}
                onChange={handleChange}
              />
            </label>
            <button type="submit">Assess</button>
          </form>
        </div>
        <div className="result-container">
          {result && (
            <div className="result-content">
              <h3>Financial Condition: {result.financial_condition}</h3>
              <h4>Recommendations:</h4>
              <ul>
                {result.recommendations &&
                  result.recommendations.map((recommendation, index) => (
                    <li key={index}>{recommendation}</li>
                  ))}
              </ul>
              {/* Inputs for salary, savings, and job */}
              {showInputs && (
                <div className="inputs-container">
                  <input
                    type="number"
                    name="salary"
                    placeholder="Enter your salary"
                    value={salary}
                    onChange={(e) => setSalary(e.target.value)}
                  />
                  <input
                    type="number"
                    name="savings"
                    placeholder="Enter your savings"
                    value={savings}
                    onChange={(e) => setSavings(e.target.value)}
                  />
                  <input
                    type="text"
                    name="job"
                    placeholder="Enter your job"
                    value={job}
                    onChange={(e) => setJob(e.target.value)}
                  />
                  {/* Suggestions button */}
                  <button className="btn btn-primary" onClick={handleSuggestions}>
                    Suggestions
                  </button>
                </div>
              )}
              {/* Suggestion */}
              {suggestion && (
                <div className="suggestion-container">
                  <h4>Suggestion:</h4>
                  <p>{suggestion}</p>
                </div>
              )}
            </div>
          )}
          {error && <p className="error-message">{error}</p>}
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
