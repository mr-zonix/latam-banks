# Dashboard Standards v4.2 — OBLIGATORIO

*Última actualización: 2025-04-01*

---

## 📌 Sidebar Estándar (8 items — SIEMPRE)

```html
<ul class="nav-menu">
    <li class="nav-item" onclick="window.location.href='../index.html'">
        <span class="nav-icon">📊</span>
        <span>Dashboard</span>
    </li>
    <li class="nav-item" onclick="window.location.href='../ranking/index.html'">
        <span class="nav-icon">📋</span>
        <span>Ranking</span>
    </li>
    <li class="nav-item" onclick="window.location.href='../ecuador/index.html'">
        <span class="nav-icon">🇪🇨</span>
        <span>Ecuador</span>
    </li>
    <li class="nav-item" onclick="window.location.href='../peru/index.html'">
        <span class="nav-icon">🇵🇪</span>
        <span>Peru</span>
    </li>
    <li class="nav-item" onclick="window.location.href='../colombia/index.html'">
        <span class="nav-icon">🇨🇴</span>
        <span>Colombia</span>
    </li>
    <li class="nav-item" onclick="window.location.href='../guatemala/index.html'">
        <span class="nav-icon">🇬🇹</span>
        <span>Guatemala</span>
    </li>
    <li class="nav-item" onclick="window.location.href='../panama/index.html'">
        <span class="nav-icon">🇵🇦</span>
        <span>Panamá</span>
    </li>
    <li class="nav-item" onclick="window.location.href='../executives/index.html'">
        <span class="nav-icon">👔</span>
        <span>Executives</span>
    </li>
</ul>
```

**Notas:**
- El país/sección actual debe tener `class="nav-item active"`
- Para archivos en raíz (index.html), quitar `../` de los hrefs
- NUNCA omitir ningún item

---

## 📌 Footer Estándar

```html
<div class="nav-footer">
    <p>Built by Mr Zonix</p>
    <p class="version">v4.2 • Apr 2025</p>
</div>
```

---

## 📌 Scripts Requeridos

Antes de `</body>`:
```html
<script src="../js/version.js"></script>
</body>
```

Para archivos en raíz:
```html
<script src="js/version.js"></script>
</body>
```

---

## 📌 Versión Actual

- **Versión:** 4.2
- **Fecha:** Apr 2025
- **Archivo:** `js/version.js`

Al actualizar, cambiar en `js/version.js`:
```javascript
const DASHBOARD_VERSION = {
    version: "4.2",
    date: "Apr 2025",
    lastUpdate: "2025-04-01",
    author: "Mr Zonix"
};
```

---

## 📌 Estructura de Países

| País | Bancos | Archivo Index |
|------|--------|---------------|
| 🇪🇨 Ecuador | 5 | ecuador/index.html |
| 🇵🇪 Perú | 5 | peru/index.html |
| 🇨🇴 Colombia | 7 | colombia/index.html |
| 🇬🇹 Guatemala | 5 | guatemala/index.html |
| 🇵🇦 Panamá | 5 | panama/index.html |

**Total: 27 bancos**

---

## 📌 Formato de Página de Banco

Ver `memory/BANK_PAGE_TEMPLATE.md` para el template completo de 6 capas.

**Secciones obligatorias:**
1. 🏢 Bank Profile (3 columnas: General, Ownership, Scale)
2. 📊 Financial Analysis (métricas + interpretación comercial)
3. 🔧 Technology Infrastructure — 6 Layers
4. 👔 Executive Intelligence
5. 🎯 Commercial Synthesis (Top 3 Priority Plays)

---

## 📌 Reglas de Push

1. Actualizar `js/version.js` con fecha actual
2. Verificar sidebar de 8 items en archivos modificados
3. Push inmediato — no preguntar
4. Mensaje de commit descriptivo con emoji

---

## 📌 Colores de Oportunidad

- 🟢 HIGH — `var(--accent-green)` — Prioridad máxima
- 🟡 MEDIUM — `var(--accent-yellow)` — Oportunidad latente
- 🔴 LOW — `#ef4444` — Decisiones globales/limitadas

---

## 📌 Consideraciones Especiales

**Bancos Estatales:**
- Warning box amarillo
- Mencionar proceso de licitación (SEACE, SECOP, etc.)
- Pitch: "Servicio al ciudadano" > "ROI"

**Bancos Globales (BBVA, Scotiabank):**
- Marcar como LOW/MEDIUM
- Indicar qué es local vs centralizado
- Badge: 🌐 GLOBAL BANK

**Conglomerados Locales:**
- Indicar grupo (Grupo Aval, GEA, Grupo Bolívar)
- Badge con color del grupo
- Clarificar autonomía de decisiones tech
