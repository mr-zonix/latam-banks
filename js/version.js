// ============================================
// 🏦 LATAM Bank Intelligence - Version Control
// ============================================
// Este archivo controla la versión global del dashboard.
// Actualizar aquí y todas las páginas se actualizan.

const DASHBOARD_VERSION = {
    version: "4.0",
    date: "Feb 2025",
    lastUpdate: "2025-02-23",
    author: "Mr Zonix"
};

// Función para actualizar el footer automáticamente
function updateVersionFooter() {
    const versionElements = document.querySelectorAll('.version, .nav-footer .version');
    const versionText = `v${DASHBOARD_VERSION.version} • ${DASHBOARD_VERSION.date}`;
    
    versionElements.forEach(el => {
        el.textContent = versionText;
    });
}

// Ejecutar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', updateVersionFooter);

// Exportar para uso global
window.DASHBOARD_VERSION = DASHBOARD_VERSION;

console.log(`🏦 LATAM Intel Dashboard v${DASHBOARD_VERSION.version} • Last update: ${DASHBOARD_VERSION.lastUpdate}`);
