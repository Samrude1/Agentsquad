// API Configuration utility
// In production, this should be set to your Hugging Face Space URL
// In development, it defaults to localhost:8000
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const getApiUrl = (endpoint) => {
    // Remove leading slash if present
    const cleanEndpoint = endpoint.startsWith('/') ? endpoint.substring(1) : endpoint;
    return `${API_BASE_URL}/${cleanEndpoint}`;
};

export default API_BASE_URL;
