import { useState } from 'react';
import SalesForm from './components/SalesForm';
import ResearchForm from './components/ResearchForm';
import MeetingPrepForm from './components/MeetingPrepForm';
import ResultsView from './components/ResultsView';
import './style.css';

function App() {
  const [activeTab, setActiveTab] = useState('sales');
  const [result, setResult] = useState(null);
  const [showArchModal, setShowArchModal] = useState(false);

  return (
    <div className="app-container">
      <div className="content-wrapper">
        <header className="header-container">
          <h1 className="app-title">Agent Squad</h1>
          <p className="app-subtitle-tag">Autonomous Multi-Agent Platform for Enterprise Teams</p>
          
          <button 
            className="arch-toggle-btn"
            onClick={() => setShowArchModal(true)}
          >
            🏗️ System Architecture & CTO Guide
          </button>
        </header>

        <div className="tab-navigation">
          <button
            onClick={() => { setActiveTab('sales'); setResult(null); }}
            className={`tab-button ${activeTab === 'sales' ? 'active' : ''}`}
          >
            💼 Sales Agent
          </button>
          <button
            onClick={() => { setActiveTab('research'); setResult(null); }}
            className={`tab-button ${activeTab === 'research' ? 'active' : ''}`}
          >
            🔬 Deep Research
          </button>
          <button
            onClick={() => { setActiveTab('scout'); setResult(null); }}
            className={`tab-button ${activeTab === 'scout' ? 'active' : ''}`}
          >
            📋 Meeting Prep
          </button>
        </div>

        {activeTab === 'sales' && <SalesForm onResult={setResult} />}
        {activeTab === 'research' && <ResearchForm onResult={setResult} />}
        {activeTab === 'scout' && <MeetingPrepForm onResult={setResult} />}

        <ResultsView result={result} />

        {/* Architecture & CTO Modal */}
        {showArchModal && (
          <div className="modal-overlay" onClick={() => setShowArchModal(false)}>
            <div className="modal-card" onClick={(e) => e.stopPropagation()}>
              <div className="modal-header">
                <div>
                  <h3 className="modal-title">🏗️ Enterprise Agent Architecture</h3>
                  <p className="agent-subtitle">Engineering overview & production-ready design principles</p>
                </div>
                <button className="modal-close-btn" onClick={() => setShowArchModal(false)}>✕</button>
              </div>

              <div className="modal-body">
                <p style={{ fontSize: '0.92rem', color: '#4b5563', marginBottom: '1rem' }}>
                  Agent Squad orchestrates specialized AI agents using <strong>FastAPI</strong>, <strong>CrewAI</strong>, and <strong>Tavily Search</strong> with built-in fault tolerance.
                </p>

                <div className="arch-grid">
                  <div className="arch-card">
                    <h4>💼 Sales Agent</h4>
                    <p>3-variant generator evaluating professional, engaging, and concise styles. Dispatches through authenticated email delivery.</p>
                    <span className="arch-badge">OpenRouter + Resend</span>
                  </div>

                  <div className="arch-card">
                    <h4>🔬 Deep Research</h4>
                    <p>Multi-step search synthesis with entity cross-referencing and executive markdown report generation.</p>
                    <span className="arch-badge">Tavily + Gemini / Claude</span>
                  </div>

                  <div className="arch-card">
                    <h4>📋 Meeting Prep Crew</h4>
                    <p>3-agent CrewAI pipeline (Intel Researcher, Strategy Analyst, Briefing Coordinator) outputting structured Pydantic schemas.</p>
                    <span className="arch-badge">CrewAI Hierarchical</span>
                  </div>
                </div>

                <div style={{ marginTop: '1.5rem', padding: '1rem', background: '#fafafa', borderRadius: '8px', border: '1px solid #e5e7eb' }}>
                  <h4 style={{ fontSize: '0.95rem', fontWeight: '700', marginBottom: '0.5rem' }}>🛡️ Enterprise Reliability & Guardrails:</h4>
                  <ul style={{ fontSize: '0.85rem', color: '#4b5563', paddingLeft: '1.25rem', lineHeight: '1.6' }}>
                    <li><strong>Automatic Model Fallback:</strong> Seamlessly switches to budget LLM models upon hitting HTTP 429 rate limits without crashing.</li>
                    <li><strong>Schema Integrity:</strong> Strictly typed outputs validated via Pydantic schemas to prevent hallucinations and malformed JSON.</li>
                    <li><strong>Security Headers:</strong> Pre-configured nosniff, frameguard (X-Frame-Options: DENY), and CORS whitelisting.</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
