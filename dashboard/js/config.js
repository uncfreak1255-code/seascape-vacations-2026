/**
 * Seascape Analytics Dashboard - API Configuration
 * 
 * This file contains your API credentials.
 * IMPORTANT: Keep this file secure and never commit to public repositories.
 */

const API_CONFIG = {
  // ============================================
  // Google Analytics 4 Configuration
  // ============================================
  googleAnalytics: {
    // Your GA4 Property ID (find in GA4 Admin > Property Settings)
    // Format: numeric ID like "123456789"
    propertyId: '', // TODO: Add your GA4 Property ID
    
    // API Key from Google Cloud Console
    apiKey: 'AIzaSyA4CuI6-d35RP21U8IaRYFhI-vnas-uGyU',
    
    // Project ID
    projectId: 'seascape-analytics-dashboard',
    
    // API Endpoint
    endpoint: 'https://analyticsdata.googleapis.com/v1beta'
  },

  // ============================================
  // Meta Pixel / Marketing API Configuration
  // ============================================
  meta: {
    // Your Meta Pixel ID
    pixelId: '2748551298816267',
    
    // App ID from developers.facebook.com
    // TODO: Complete developer registration to get this
    appId: '',
    
    // App Secret (keep secure!)
    // TODO: Get from App Dashboard > Settings > Basic
    appSecret: '',
    
    // User Access Token with ads_read, read_insights permissions
    // TODO: Generate from Graph API Explorer
    accessToken: '',
    
    // API Version
    apiVersion: 'v19.0',
    
    // API Endpoint
    endpoint: 'https://graph.facebook.com'
  },

  // ============================================
  // Dashboard Settings
  // ============================================
  dashboard: {
    // Refresh interval in milliseconds (default: 5 minutes)
    refreshInterval: 300000,
    
    // Default date range in days
    defaultDateRange: 7,
    
    // Enable API data fetching (set to true once APIs are configured)
    useApiData: false
  }
};

// Export for use in dashboard
if (typeof module !== 'undefined' && module.exports) {
  module.exports = API_CONFIG;
}
