import { useState } from 'react';
import SalesForm from './components/SalesForm';
import ResearchForm from './components/ResearchForm';
import ResultsView from './components/ResultsView';

function App() {
  const [activeTab, setActiveTab] = useState('sales');
  const [result, setResult] = useState(null);

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-12 px-4">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-4xl font-bold text-center mb-8 text-gray-800">
          Smart Outreach Manager
        </h1>

        {/* Tab Navigation */}
        <div className="flex justify-center mb-8 space-x-4">
          <button
            onClick={() => { setActiveTab('sales'); setResult(null); }}
            className={`px-6 py-3 rounded-lg font-semibold transition-colors ${activeTab === 'sales'
                ? 'bg-blue-600 text-white'
                : 'bg-white text-gray-700 hover:bg-gray-100'
              }`}
          >
            Sales Agent
          </button>
          <button
            onClick={() => { setActiveTab('research'); setResult(null); }}
            className={`px-6 py-3 rounded-lg font-semibold transition-colors ${activeTab === 'research'
                ? 'bg-green-600 text-white'
                : 'bg-white text-gray-700 hover:bg-gray-100'
              }`}
          >
            Research Agent
          </button>
        </div>

        {/* Forms */}
        {activeTab === 'sales' && <SalesForm onResult={setResult} />}
        {activeTab === 'research' && <ResearchForm onResult={setResult} />}

        {/* Results */}
        <ResultsView result={result} />
      </div>
    </div>
  );
}

export default App;
