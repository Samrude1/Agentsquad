import Markdown from 'react-markdown';

export default function ResultsView({ result }) {
    if (!result) return null;

    // Show loading state while agents are working
    if (result.status === 'running') {
        return (
            <div className="results-container">
                <h3 className="results-title">🔄 {result.agent || 'Agent'} is working...</h3>
                <div className="results-content loading-content">
                    <div className="loading-indicator">
                        <span className="pulse-dot"></span>
                        <span>{result.message || 'Processing your request...'}</span>
                    </div>
                </div>
            </div>
        );
    }

    const downloadReport = () => {
        const element = document.createElement("a");
        const file = new Blob([result.result], {type: 'text/markdown'});
        element.href = URL.createObjectURL(file);
        element.download = `AgentSquad_Report_${new Date().toISOString().split('T')[0]}.md`;
        document.body.appendChild(element);
        element.click();
        document.body.removeChild(element);
    };

    return (
        <div className="results-container">
            <div className="results-header">
                <h3 className="results-title">
                    {result.status === 'success' ? '✅ Result' : '❌ Error'}
                </h3>
                {result.status === 'success' && (
                    <button onClick={downloadReport} className="download-button">
                        📥 Download .md
                    </button>
                )}
            </div>

            <div className={`results-content ${result.status === 'error' ? 'error-content' : 'markdown-content'}`}>
                {result.status === 'success' ? (
                    <Markdown>{result.result}</Markdown>
                ) : (
                    result.result || result.message
                )}
            </div>
        </div>
    );
}
