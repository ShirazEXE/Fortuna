import React from 'react';
import ReactDOM from 'react-dom';
import { Auth0Provider } from '@auth0/auth0-react'; // Import Auth0Provider
import Routes from './Routes'; // Import your Routes component
import './index.css';
import reportWebVitals from './reportWebVitals';



ReactDOM.render(
  <React.StrictMode>
    <Auth0Provider
      domain="dev-krh7bt4ydn23zwqs.us.auth0.com"
      clientId="W84RkD3A6VxFqRcipyr4kgACiLmuI1qE"
      redirectUri="http://localhost:3000/Dashboard"
    >
      <Routes /> {/* Render the Routes component */}
    </Auth0Provider>
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();
