import { useState, useEffect } from 'react';
import SalesForm from './components/SalesForm';
import ResearchForm from './components/ResearchForm';
import MeetingPrepForm from './components/MeetingPrepForm';
import ResultsView from './components/ResultsView';
import LoginPage from './components/LoginPage';
import './style.css';

function App() {
  const [activeTab, setActiveTab] = useState('sales');
  const [result, setResult] = useState(null);
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [authChecking, setAuthChecking] = useState(true);

  useEffect(() => {
    checkAuth();
  }, []);

  const checkAuth = async () => {
    try {
      const res = await fetch('http://localhost:8000/api/config/auth-enabled');
      const data = await res.json();

      if (!data.enabled) {
        setIsAuthenticated(true);
      } else {
        const storedPin = localStorage.getItem('agent_platform_pin');
        if (storedPin) {
          // Verify stored pin
          const vRes = await fetch('http://localhost:8000/api/auth/verify', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ pin: storedPin }),
          });
          if (vRes.ok) setIsAuthenticated(true);
        }
      }
    } catch (err) {
      console.error('Auth check failed', err);
    } finally {
      setAuthChecking(false);
    }
  };

  if (authChecking) return <div className="loading-screen">Starting Platform...</div>;
  if (!isAuthenticated) return <LoginPage onSuccess={() => setIsAuthenticated(true)} />;

  return (
    <div className="app-container">
      <div className="content-wrapper">
        <h1 className="app-title">AI Agent Platform</h1>

        <div className="tab-navigation">
          <button
            onClick={() => { setActiveTab('sales'); setResult(null); }}
            className={`tab-button ${activeTab === 'sales' ? 'active' : ''}`}
          >
            Sales Agent
          </button>
          <button
            onClick={() => { setActiveTab('research'); setResult(null); }}
            className={`tab-button ${activeTab === 'research' ? 'active research' : ''}`}
          >
            Deep Research
          </button>
          <button
            onClick={() => { setActiveTab('scout'); setResult(null); }}
            className={`tab-button ${activeTab === 'scout' ? 'active' : ''}`}
          >
            Meeting Prep
          </button>
        </div>

        {activeTab === 'sales' && <SalesForm onResult={setResult} />}
        {activeTab === 'research' && <ResearchForm onResult={setResult} />}
        {activeTab === 'scout' && <MeetingPrepForm onResult={setResult} />}

        <ResultsView result={result} />
      </div>
    </div>
  );
}

export default App;
