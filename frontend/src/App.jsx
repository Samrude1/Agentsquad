import { useState } from 'react';
import SalesForm from './components/SalesForm';
import ResearchForm from './components/ResearchForm';
import MeetingPrepForm from './components/MeetingPrepForm';
import ResultsView from './components/ResultsView';
import './style.css';

function App() {
  const [activeTab, setActiveTab] = useState('sales');
  const [result, setResult] = useState(null);

  return (
    <div className="app-container">
      <div className="content-wrapper">
        <h1 className="app-title">Agent Squad</h1>
        
        <div className="info-note">
            ℹ️ Pro-tip: Emails are sent via <strong>Resend</strong> from <strong>info@samirautanen.fi</strong>
        </div>

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
