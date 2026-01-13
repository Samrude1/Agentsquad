export default function ResultsView({ result }) {
    if (!result) return null;

    return (
        <div className="max-w-4xl mx-auto mt-8 p-6 bg-white rounded-lg shadow-lg">
            <h3 className="text-xl font-bold mb-4 text-gray-800">
                {result.status === 'success' ? '✅ Result' : '❌ Error'}
            </h3>

            <div className="prose max-w-none">
                {result.status === 'success' ? (
                    <pre className="whitespace-pre-wrap bg-gray-50 p-4 rounded border border-gray-200 text-sm">
                        {result.result}
                    </pre>
                ) : (
                    <div className="text-red-600 bg-red-50 p-4 rounded border border-red-200">
                        {result.result}
                    </div>
                )}
            </div>
        </div>
    );
}
