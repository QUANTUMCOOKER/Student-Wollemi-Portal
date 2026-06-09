import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider } from './hooks/useTheme';
import LandingPage from './pages/LandingPage';

function App() {
  return (
    <ThemeProvider>
      <Router>
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/auth-success" element={<div>Auth Successful! (Redirecting...)</div>} />
        </Routes>
      </Router>
    </ThemeProvider>
  );
}

export default App;
