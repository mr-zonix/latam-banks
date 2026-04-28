# 🏦 METHODOLOGY.md — LATAM Banks Intelligence

> Guía estructurada para investigar y documentar bancos de cualquier país de LATAM.
> Seguir este proceso garantiza consistencia y utilidad comercial.

---

## 📁 Estructura de Archivos por País

```
{pais}/
├── OVERVIEW.md              # Visión macro del sector bancario del país
├── DASHBOARD.md             # Tabla ejecutiva comparativa (Top 5-10 bancos)
└── banks/
    ├── {banco_1}.md         # Deep dive del banco
    ├── {banco_1}_EXECUTIVES.md   # Ejecutivos clave
    ├── {banco_2}.md
    ├── {banco_2}_EXECUTIVES.md
    └── ...
```

Adicionalmente, actualizar los dashboards HTML:
- `latam-banks/index.html` — Ranking regional Top 50
- `dashboard_new/{pais}/index.html` — Dashboard visual del país

---

## 📊 OVERVIEW.md — Contenido Requerido

1. **Contexto Macro del País**
   - PIB, población, economía general
   - Regulador bancario (ej: Superintendencia de Bancos)
   - Características del sistema financiero

2. **Estructura del Sector Bancario**
   - Número de bancos
   - Concentración (top 5 = X% del mercado)
   - Tipos: privados, estatales, cooperativas

3. **Tendencias Tecnológicas Relevantes**
   - Digitalización
   - Regulaciones de datos/cloud
   - Fintechs y competencia

4. **Fuentes de Datos**
   - Links a regulador
   - Reportes anuales
   - Rankings sectoriales

---

## 📋 DASHBOARD.md — Estructura Exacta

### Tabla Ejecutiva Principal
| Rank | Bank | Assets | 3Y Growth | ROE | CIR | NPL | Opportunity |
|:----:|------|-------:|:---------:|:---:|:---:|:---:|:-----------:|

- **Assets**: En USD (normalizado)
- **3Y Growth**: Crecimiento compuesto 3 años
- **ROE**: Return on Equity
- **CIR**: Cost-to-Income Ratio
- **NPL**: Non-Performing Loans ratio
- **Opportunity**: 🟢 HIGH | 🟡 MEDIUM | 🔴 LOW

### Secciones Obligatorias
1. **Opportunity Prioritization Matrix** — Tier 1/2/3 con justificación
2. **Infrastructure Layer Opportunities** — Matriz 6 capas x bancos
3. **Financial Health Comparison** — Gráficos ASCII de assets, ROE, CIR
4. **Recommended Engagement Sequence** — Orden de prioridad con primer movimiento
5. **Quick Links** — Links a deep dives y ejecutivos

---

## 🏦 {banco}.md — Deep Dive Structure

### 1. PROFILE
| Attribute | Detail |
|-----------|--------|
| Full Name | |
| Type | Private/State/Cooperative |
| Founded | |
| Headquarters | |
| Total Assets | USD |
| Market Position | |
| Employees | |
| Branches | |
| International | Presencia fuera del país |

- **Ownership Structure**: Controlantes, cotiza en bolsa?
- **Business Focus**: Retail, corporate, SME, etc.
- **Digital Maturity**: 🔴 LOW | 🟡 MEDIUM | 🟢 HIGH

### 2. FINANCIAL ANALYSIS

#### Key Ratios Table
| Ratio | Value | Interpretation | Commercial Implication |
|-------|-------|----------------|------------------------|
| Total Assets | | | |
| 3Y Asset Growth | | | |
| ROE | | | |
| CIR | | | |
| NPL Ratio | | | |

#### 3-Year Trend Analysis
| Year | Assets | Growth | ROE | CIR | Signal |
|------|--------|--------|-----|-----|--------|

#### Investment Appetite Hypothesis
HIGH/MEDIUM/LOW + justificación

### 3. INFRASTRUCTURE LAYERS (6 capas)

Para CADA capa, analizar:

#### Layer 1: Processing & Compute 🟢/🟡/🔴
| Aspect | Assessment |
|--------|------------|
| Current State | |
| Technology Stack | |
| Modernization Signals | |
| Pain Points | |

**Commercial Opportunity:** [Descripción]

#### Layer 2: Storage 🟢/🟡/🔴
*(mismo formato)*

#### Layer 3: Networking 🟢/🟡/🔴
*(mismo formato)*

#### Layer 4: Core Banking 🟢/🟡/🔴
*(mismo formato)*

#### Layer 5: Digital Banking Platform 🟢/🟡/🔴
*(mismo formato)*

#### Layer 6: Data, Analytics & AI 🟢/🟡/🔴
*(mismo formato)*

### 4. COMMERCIAL SYNTHESIS

- **Primary Opportunity**: La jugada principal
- **Entry Strategy**: Cómo entrar
- **Key Stakeholders**: A quién contactar
- **Timing**: Urgencia/ventana
- **Risks/Blockers**: Obstáculos

---

## 👔 {banco}_EXECUTIVES.md — Executive Intelligence

### Estructura por Ejecutivo

Para cada ejecutivo relevante:

| Attribute | Detail |
|-----------|--------|
| Name | |
| Title | |
| Tenure | |
| LinkedIn | URL |
| Influence on Tech Decisions | 🟢 HIGH / 🟡 MEDIUM / 🔴 LOW |

- **Career Trajectory**: Roles anteriores
- **Public Footprint**: Conferencias, artículos, entrevistas
- **Personal Interests/Affiliations**: Lo que se pueda encontrar
- **Education**: Universidad, MBA, certificaciones
- **🎯 Engagement Angle**: Narrativa recomendada para conectar

### Ejecutivos a Investigar (en orden de prioridad)
1. CIO / Chief Information Officer
2. VP/Director of Infrastructure
3. VP/Director of Digital Banking
4. CEO (para contexto)
5. CFO (para deals grandes)
6. Chief Data Officer (si existe)
7. CISO (para security plays)

---

## 🌐 Dashboard HTML — Actualización

### latam-banks/index.html
- Ranking regional Top 50
- Agregar nuevos bancos del país
- Mantener ordenado por assets

### dashboard_new/{pais}/index.html
- Crear si no existe
- Visual interactivo con filtros
- Cards por banco con métricas clave
- Links a deep dives

---

## 🔄 Proceso para Nuevo País

### Paso 1: Investigación Macro (30 min)
- Buscar regulador bancario del país
- Obtener lista de bancos por assets
- Identificar Top 5-10 relevantes

### Paso 2: Data Financiera (1-2 hrs)
- Descargar/buscar ratios de cada banco
- Normalizar assets a USD
- Calcular/encontrar ROE, CIR, NPL, growth

### Paso 3: Crear OVERVIEW.md
- Contexto país
- Estructura sector
- Fuentes

### Paso 4: Crear DASHBOARD.md
- Tabla ejecutiva
- Priorización
- Matrices comparativas

### Paso 5: Deep Dives por Banco
- Crear {banco}.md para Top 5
- 6 infrastructure layers cada uno
- Commercial synthesis

### Paso 6: Executive Intelligence
- LinkedIn research
- Crear {banco}_EXECUTIVES.md
- Engagement angles

### Paso 7: Actualizar Dashboards HTML
- Agregar a ranking regional
- Crear página país si aplica
- Push a GitHub

---

## 📚 Fuentes Típicas por País

| País | Regulador | Ranking Típico |
|------|-----------|----------------|
| 🇪🇨 Ecuador | Superintendencia de Bancos | Asobanca |
| 🇨🇴 Colombia | Superfinanciera | Asobancaria |
| 🇵🇪 Perú | SBS | ASBANC |
| 🇲🇽 México | CNBV | ABM |
| 🇨🇱 Chile | CMF | ABIF |
| 🇦🇷 Argentina | BCRA | — |
| 🇧🇷 Brasil | Banco Central | FEBRABAN |
| 🇵🇦 Panamá | SBP | — |

---

## ✅ Checklist de Calidad

Antes de dar por terminado un país:

- [ ] OVERVIEW.md completo con fuentes
- [ ] DASHBOARD.md con todas las secciones
- [ ] Top 5 bancos con deep dive completo
- [ ] 6 infrastructure layers analizados por banco
- [ ] Executive files creados (aunque sea con [TO RESEARCH])
- [ ] Dashboard HTML actualizado
- [ ] Push a GitHub hecho
- [ ] Zuni puede ver en GitHub Pages

---

*Metodología creada: Febrero 2025*
*Mantener actualizada según aprendamos*
