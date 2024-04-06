import React from 'react';
import { BrowserRouter as Router, Route, Routes, useNavigate } from 'react-router-dom';
import { useAuth0 } from '@auth0/auth0-react';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

const Auth0Callback = () => {
  const navigate = useNavigate();
  const { handleRedirectCallback, isAuthenticated } = useAuth0();

  React.useEffect(() => {
    const handleCallback = async () => {
      await handleRedirectCallback();
      if (isAuthenticated) {
        navigate('/Dashboard');
      }
    };

    handleCallback();
  }, [handleRedirectCallback, isAuthenticated, navigate]);

  return <div>Loading...</div>;
};

const Dashboard = () => {
  const { user } = useAuth0();

  return (
    <div>
      <h1>Dashboard</h1>
      <p>Welcome, {user.name}!</p>
      {/* Add your dashboard content here */}
    </div>
  );
};

function App() {
  const { loginWithRedirect, isAuthenticated, user } = useAuth0();
  const navigate = useNavigate();

  const handleLogin = () => {
    loginWithRedirect();
  };

  React.useEffect(() => {
    if (isAuthenticated) {
      navigate('/dashboard');
    }
  }, [isAuthenticated, navigate]);

  return (
    <div className="background">
      <header className="container-fluid d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 mb-4 border-bottom">
        <div className="col-md-3 mb-2 mb-md-0">
          <a href="/" className="d-inline-flex link-body-emphasis text-decoration-none">
            <svg className="bi" width="40" height="32" role="img" aria-label="Bootstrap">
              <use xlinkHref="#bootstrap"></use>
            </svg>
          </a>
        </div>
        <ul className="nav col-12 col-md-auto mb-2 justify-content-center mb-md-0">
          <li>
            <a href="#" className="nav-link px-2 link-secondary button">
              Home
            </a>
          </li>
          <li>
            <a href="#" className="nav-link px-2 button">
              Features
            </a>
          </li>
          <li>
            <a href="#" className="nav-link px-2 button">
              FAQs
            </a>
          </li>
          <li>
            <a href="#" className="nav-link px-2 button">
              About
            </a>
          </li>
        </ul>
        <div className="col-md-3 text-end">
          <button type="button" className="btn btn-primary me-2" onClick={handleLogin}>
            Get Started
          </button>
        </div>
      </header>
      <div className="container1">
        <div className="App">
          <h1 style={{ color: 'black' }}>FORTUNA
          <p>Personal Finance Guardian</p></h1>
          
        </div>
      </div>

      <Routes>
        <Route path="/auth0-callback" element={<Auth0Callback />} />
        <Route path="/Dashboard" element={<Dashboard />} />
      </Routes>
    </div>
  );
}

export default App;