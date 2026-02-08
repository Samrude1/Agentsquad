/**
 * Utility function to handle API errors with user-friendly messages.
 * Detects rate limiting errors and provides helpful feedback.
 */
export function handleApiError(error) {
    // Check if it's a rate limit error (429 status)
    if (error.response?.status === 429) {
        const data = error.response.data;
        return {
            status: 'error',
            result: `⏱️ ${data.message || 'Rate limit exceeded'}\n\n${data.hint || 'Please try again in a few minutes.'}`
        };
    }

    // Check for network errors
    if (error.code === 'ERR_NETWORK' || !error.response) {
        return {
            status: 'error',
            result: '🔌 Unable to connect to the server. Please check if the backend is running.'
        };
    }

    // Check for authentication errors
    if (error.response?.status === 401) {
        return {
            status: 'error',
            result: '🔒 Authentication failed. Please check your PIN and try again.'
        };
    }

    // Generic error with server response
    if (error.response?.data?.detail) {
        return {
            status: 'error',
            result: `❌ ${error.response.data.detail}`
        };
    }

    // Fallback error message
    return {
        status: 'error',
        result: `❌ An error occurred: ${error.message}`
    };
}
