import Markdown from 'react-markdown';

export default function ResultsView({ result }) {
    if (!result) return null;

    return (
        <div className="results-container">
            <h3 className="results-title">
                {result.status === 'success' ? '✅ Result' : '❌ Error'}
            </h3>

            <div className={`results-content ${result.status === 'error' ? 'error-content' : 'markdown-content'}`}>
                {result.status === 'success' ? (
                    <Markdown>{result.result}</Markdown>
                ) : (
                    result.result
                )}
            </div>
        </div>
    );
}
