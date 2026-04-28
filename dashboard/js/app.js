// Page Navigation
function switchPage(pageName) {
    // Remove active from all nav items and pages
    document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
    document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
    
    // Activate the selected page
    const navItem = document.querySelector(`.nav-item[data-page="${pageName}"]`);
    const page = document.getElementById('page-' + pageName);
    
    if (navItem) navItem.classList.add('active');
    if (page) page.classList.add('active');
    
    // Scroll to top
    window.scrollTo(0, 0);
}

// Click handlers for nav items
document.querySelectorAll('.nav-item').forEach(item => {
    item.addEventListener('click', () => {
        switchPage(item.dataset.page);
    });
});

// Make switchPage available globally
window.switchPage = switchPage;

console.log('🏦 LATAM Bank Intelligence Dashboard v1.0');
console.log('Built by Mr Zonix for Zuni');
