# 🏦 Template para Agregar Países al Dashboard

## Pasos para Agregar un Nuevo País

### 1. Crear carpeta del país
```
mkdir -p [pais]/
```

### 2. Crear archivos necesarios
- `[pais]/index.html` — Landing page del país
- `[pais]/[banco].html` — Una página por cada banco

### 3. Actualizar sidebar en TODOS los archivos
Agregar después de la última entrada de país:
```html
<li class="nav-item" onclick="window.location.href='../[pais]/index.html'">
    <span class="nav-icon">🏳️</span>
    <span>[País]</span>
</li>
```

### 4. Actualizar index.html principal
- Incrementar contador de bancos
- Incrementar contador de países
- Agregar priority cards si aplica
- Agregar country card en la sección Countries

## Estructura de Página de País (index.html)
Ver `ecuador/index.html` como referencia:
- Bank Comparison Table (Rank, Assets, Growth, ROE, CIR, NPL, Opportunity)
- Infrastructure Opportunity Matrix
- Key Market Insights

## Estructura de Página de Banco ([banco].html)
Ver `ecuador/banco_pichincha.html` como referencia:
- Key Financial Metrics (Assets, Growth, ROE, CIR, NPL)
- Bank Profile
- Technology & Infrastructure
- Best Infrastructure Plays
- Commercial Signals
- Key Executives

## Métricas Requeridas por Banco
| Métrica | Descripción |
|---------|-------------|
| Assets | Activos totales en USD (ej: $18B) |
| 3Y Growth | Crecimiento de activos 3 años % |
| ROE | Return on Equity % |
| CIR | Cost-to-Income Ratio % |
| NPL | Non-Performing Loans % |

## Opportunity Levels
- 🟢 HIGH — Active opportunity, strong signals
- 🟡 MEDIUM — Latent need, potential
- 🔴 LOW — Low priority

## Tier Classification
- **TIER 1** — High opportunity, strategic priority
- **TIER 2** — Medium opportunity, worth pursuing

## Países Actuales
| Código | País | Bancos |
|--------|------|--------|
| 🇪🇨 | Ecuador | 5 |
| 🇵🇪 | Peru | 1 |
| 🇨🇴 | Colombia | 7 |
| 🇬🇹 | Guatemala | 3 |
