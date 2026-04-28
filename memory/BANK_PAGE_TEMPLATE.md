# Bank Detail Page Template — Estándar Obligatorio

Este es el formato estándar para TODAS las páginas de detalle de bancos en el dashboard.
Referencia: `dashboard/panama/banco_general.html`

---

## Estructura de Secciones (EN ORDEN)

### 1. 🏢 Bank Profile
Grid de 3 columnas:
- **General Information:** Founded, HQ, Type, License, Listed
- **Ownership & Control:** Control, Structure, Decision Authority, Chairman, CEO
- **Scale & Footprint:** Employees, Branches, ATMs, Digital Users, Countries

+ Info banner con "Strategic Position"

### 2. 📊 Financial Analysis
- Key metrics cards: Assets, 3Y Growth, ROE, CIR
- Tabla de Profitability Metrics (Net Income, ROE, ROA, NIM, CIR)
- Tabla de Asset Quality (NPL, Coverage, Loans, Deposits, CAR)
- Box de "💡 Commercial Interpretation"

### 3. 🔧 Technology Infrastructure — 6 LAYERS

Cada layer tiene:
- Current State (bullets)
- Vendors/Strategy (bullets)
- 🎯 Opportunity box

**Layer 1: Processing & Compute**
- Primary DC, DR Site, Server Architecture
- Virtualization, Cloud Strategy, HPC/AI

**Layer 2: Storage & Data Management**
- Primary Storage, Backup & DR
- Data Governance, Capacity

**Layer 3: Networking & Security**
- Network Architecture, Security Stack
- Connectivity (Direct Connect, SWIFT, ACH)

**Layer 4: Core Banking System**
- Core Platform, Satellite Systems
- Integration Layer, Open Banking status

**Layer 5: Digital Banking Platform**
- Consumer Digital (app, users, features)
- Business Digital, Technology Stack

**Layer 6: Data, Analytics & AI**
- Data Platform, Analytics/BI
- AI/ML Initiatives

### 4. 👔 Executive Intelligence
- C-Suite box
- Technology Leadership box (con "To verify" + LinkedIn search links)
- Digital & Data box
- Engagement Notes (Decision Structure, Procurement, Contact preference, Events)

### 5. 🎯 Commercial Synthesis
Grid con:
- 💰 Opportunity Assessment (Deal Size, Budget Cycle, Decision Speed, Hot Projects)
- 🎪 Recommended Strategy (numbered list)
- 👔 Key Stakeholders (con LinkedIn search tip)
- 📅 Timing & Entry Points

+ **🏆 Top 3 Priority Plays** (numbered priority items con deal size y timeline)

### 6. Navigation Footer
```html
<div class="exec-navigation">
    <a href="index.html" class="btn-secondary">← Back to [País]</a>
    <a href="[next_bank].html" class="btn-primary">Next: [Bank Name] →</a>
</div>
```

---

## Sidebar Estándar (8 items — OBLIGATORIO)

```html
<ul class="nav-menu">
    <li class="nav-item">📊 Dashboard</li>
    <li class="nav-item">📋 Ranking</li>
    <li class="nav-item">🇪🇨 Ecuador</li>
    <li class="nav-item">🇵🇪 Peru</li>
    <li class="nav-item">🇨🇴 Colombia</li>
    <li class="nav-item">🇬🇹 Guatemala</li>
    <li class="nav-item">🇵🇦 Panamá</li>
    <li class="nav-item">👔 Executives</li>
</ul>
```

El país actual debe tener `class="nav-item active"`

---

## Footer Obligatorio

```html
<div class="nav-footer">
    <p>Built by Mr Zonix</p>
    <p class="version">v4.0 • Feb 2025</p>
</div>
```

Y antes de `</body>`:
```html
<script src="../js/version.js"></script>
```

---

## Para Bancos con Consideraciones Especiales

**Bancos Estatales:**
- Warning box amarillo con consideraciones de licitación
- Mencionar SEACE/OSCE (Perú), SECOP (Colombia), Guatecompras (Guatemala)
- Pitch: "Servicio al ciudadano" > "ROI"

**Bancos de Grupos Globales (BBVA, Scotiabank):**
- Marcar como LOW/MEDIUM opportunity
- Indicar "Global decisions" donde aplique
- Mencionar qué SÍ es local vs centralizado

**Bancos de Conglomerados Locales:**
- Indicar el grupo (Grupo Aval, GEA, etc.)
- Clarificar si tech es centralizada o autónoma
