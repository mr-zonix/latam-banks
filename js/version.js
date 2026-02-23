// ============================================
// 🏦 LATAM Bank Intelligence - Version Control
// ============================================
const DASHBOARD_VERSION = {
    version: "4.1",
    date: "Feb 2025",
    lastUpdate: "2025-02-23",
    author: "Mr Zonix"
};

function updateVersionFooter() {
    const versionElements = document.querySelectorAll(".version, .nav-footer .version");
    const versionText = `v${DASHBOARD_VERSION.version} • ${DASHBOARD_VERSION.date}`;
    versionElements.forEach(el => { el.textContent = versionText; });
}

document.addEventListener("DOMContentLoaded", updateVersionFooter);
window.DASHBOARD_VERSION = DASHBOARD_VERSION;
console.log(`🏦 LATAM Intel Dashboard v${DASHBOARD_VERSION.version} • Last update: ${DASHBOARD_VERSION.lastUpdate}`);
