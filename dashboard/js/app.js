// LATAM Bank Intelligence Dashboard - App.js
// Handles page switching and navigation

function switchPage(pageName) {
    // Hide all pages
    document.querySelectorAll('.page').forEach(page => {
        page.classList.remove('active');
    });
    
    // Show selected page
    const targetPage = document.getElementById('page-' + pageName);
    if (targetPage) {
        targetPage.classList.add('active');
    }
    
    // Update nav active state
    document.querySelectorAll('.nav-item').forEach(item => {
        item.classList.remove('active');
        if (item.dataset.page === pageName) {
            item.classList.add('active');
        }
    });
    
    // Scroll to top
    window.scrollTo(0, 0);
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    // Check URL hash for direct page linking
    const hash = window.location.hash.substring(1);
    if (hash && document.getElementById('page-' + hash)) {
        switchPage(hash);
    }
});
