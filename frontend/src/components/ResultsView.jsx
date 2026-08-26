import { useState } from 'react';
import Markdown from 'react-markdown';

export default function ResultsView({ result }) {
    const [copied, setCopied] = useState(false);

    if (!result) return null;

    // Show loading state while agents are working
    if (result.status === 'running') {
        return (
            <div className="results-container">
                <h3 className="results-title">🔄 {result.agent || 'Agent'} is executing...</h3>
                <div className="results-content loading-content">
                    <div className="loading-indicator">
                        <span className="pulse-dot"></span>
                        <span>{result.message || 'Processing and synthesizing executive intelligence...'}</span>
                    </div>
                </div>
            </div>
        );
    }

    const handleCopy = () => {
        const textToCopy = typeof result.result === 'string' ? result.result : JSON.stringify(result.result, null, 2);
        navigator.clipboard.writeText(textToCopy);
        setCopied(true);
        setTimeout(() => setCopied(false), 2500);
    };

    const downloadReport = () => {
        const content = typeof result.result === 'string' ? result.result : JSON.stringify(result.result, null, 2);
        const element = document.createElement("a");
        const file = new Blob([content], { type: 'text/markdown' });
        element.href = URL.createObjectURL(file);
        element.download = `AgentSquad_Briefing_${new Date().toISOString().split('T')[0]}.md`;
        document.body.appendChild(element);
        element.click();
        document.body.removeChild(element);
    };

    return (
        <div className="results-container">
            <div className="results-header">
                <h3 className="results-title">
                    {result.status === 'success' ? '✅ Executive Report & Intelligence' : '❌ System Error'}
                </h3>

                {result.status === 'success' && (
                    <div className="results-actions">
                        <button onClick={handleCopy} className="action-button">
                            {copied ? '✅ Copied!' : '📋 Copy Markdown'}
                        </button>
                        <button onClick={downloadReport} className="action-button action-button-primary">
                            📥 Download .md
                        </button>
                    </div>
                )}
            </div>

            <div className={`results-content ${result.status === 'error' ? 'error-content' : 'markdown-content'}`}>
                {result.status === 'success' ? (
                    <Markdown>{typeof result.result === 'string' ? result.result : JSON.stringify(result.result, null, 2)}</Markdown>
                ) : (
                    result.result || result.message
                )}
            </div>
        </div>
    );
}
