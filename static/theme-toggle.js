/**
 * Theme Toggle System
 * Handles light/dark theme switching with localStorage persistence
 */

(function() {
    'use strict';
    
    // Theme constants
    const THEME_KEY = 'preferred-theme';
    const THEME_LIGHT = 'light';
    const THEME_DARK = 'dark';
    
    /**
     * Get the current theme from localStorage or system preference
     * @returns {string} 'light' or 'dark'
     */
    function getPreferredTheme() {
        const storedTheme = localStorage.getItem(THEME_KEY);
        
        if (storedTheme) {
            return storedTheme;
        }
        
        // Check system preference
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            return THEME_DARK;
        }
        
        return THEME_LIGHT;
    }
    
    /**
     * Apply theme to the document
     * @param {string} theme - 'light' or 'dark'
     */
    function applyTheme(theme) {
        const html = document.documentElement;
        
        if (theme === THEME_DARK) {
            html.setAttribute('data-theme', 'dark');
        } else {
            html.removeAttribute('data-theme');
        }
        
        // Update toggle button icon
        updateToggleIcon(theme);
    }
    
    /**
     * Update the theme toggle button icon
     * @param {string} theme - 'light' or 'dark'
     */
    function updateToggleIcon(theme) {
        const toggleBtn = document.getElementById('theme-toggle');
        if (!toggleBtn) return;
        
        const icon = toggleBtn.querySelector('i');
        if (!icon) return;
        
        if (theme === THEME_DARK) {
            icon.className = 'fas fa-sun';
            toggleBtn.setAttribute('aria-label', 'Switch to light theme');
            toggleBtn.setAttribute('title', 'Switch to light theme');
        } else {
            icon.className = 'fas fa-moon';
            toggleBtn.setAttribute('aria-label', 'Switch to dark theme');
            toggleBtn.setAttribute('title', 'Switch to dark theme');
        }
    }
    
    /**
     * Toggle between light and dark themes
     */
    function toggleTheme() {
        const currentTheme = getPreferredTheme();
        const newTheme = currentTheme === THEME_LIGHT ? THEME_DARK : THEME_LIGHT;
        
        // Save to localStorage
        localStorage.setItem(THEME_KEY, newTheme);
        
        // Apply the new theme
        applyTheme(newTheme);
    }
    
    /**
     * Initialize theme on page load
     */
    function initTheme() {
        const theme = getPreferredTheme();
        applyTheme(theme);
    }
    
    /**
     * Set up event listeners
     */
    function setupEventListeners() {
        const toggleBtn = document.getElementById('theme-toggle');
        if (toggleBtn) {
            toggleBtn.addEventListener('click', toggleTheme);
            
            // Keyboard accessibility
            toggleBtn.addEventListener('keydown', function(e) {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    toggleTheme();
                }
            });
        }
        
        // Listen for system theme changes
        if (window.matchMedia) {
            window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function(e) {
                // Only update if user hasn't set a preference
                if (!localStorage.getItem(THEME_KEY)) {
                    const newTheme = e.matches ? THEME_DARK : THEME_LIGHT;
                    applyTheme(newTheme);
                }
            });
        }
    }
    
    // Initialize theme immediately (before DOM loads to prevent flash)
    initTheme();
    
    // Set up event listeners when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', setupEventListeners);
    } else {
        setupEventListeners();
    }
    
    // Expose toggle function globally for potential external use
    window.toggleTheme = toggleTheme;
})();
