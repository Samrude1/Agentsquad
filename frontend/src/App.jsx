import { useState } from 'react';
import SalesForm from './components/SalesForm';
import ResearchForm from './components/ResearchForm';
import ResultsView from './components/ResultsView';
import './style.css';

function App() {
  const [activeTab, setActiveTab] = useState('sales');
  const [result, setResult] = useState(null);

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
            Research Agent
          </button>
        </div>

        {activeTab === 'sales' && <SalesForm onResult={setResult} />}
        {activeTab === 'research' && <ResearchForm onResult={setResult} />}

        <ResultsView result={result} />
      </div>
    </div>
  );
}

export default App;
