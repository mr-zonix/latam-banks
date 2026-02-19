# 🏦 Template para Agregar Bancos al Dashboard

## Estructura de un Banco
```javascript
{ 
    rank: X,                          // Se calcula automáticamente por assets
    name: "Nombre del Banco", 
    country: "XX",                    // Código ISO 2 letras
    countryName: "Nombre País", 
    flag: "🏳️",                       // Emoji bandera
    assets: 00,                       // Activos totales en USD Billones (miles de millones)
    segment: "xxx",                   // mega (>$200B), large ($50-200B), mid ($20-50B), emerging (<$20B)
    ownership: "Tipo",                // Privado, Estatal, Multinacional
    roe: 00.0,                        // Return on Equity %
    cir: 00,                          // Cost-to-Income Ratio %
    npl: 0.0,                         // Non-Performing Loans %
    growth: 00,                       // Crecimiento activos 3 años %
    infra: ["tag1", "tag2"],          // Ver tags disponibles abajo
    signals: [
        { level: "hot|warm|cool", text: "Señal comercial" }
    ]
}
```

## Tags de Infraestructura Disponibles
| Categoría | Tags |
|-----------|------|
| **Compute** | `cloud-native`, `hybrid-cloud`, `on-prem` |
| **AI** | `ai-advanced`, `ai-active`, `ai-exploring` |
| **Core** | `core-modern`, `core-transition`, `core-legacy` |
| **Data** | `data-platform`, `data-growing`, `data-basic` |

## Signal Levels
- 🔴 `hot` - Oportunidad urgente/activa (RFP activo, transformación en curso)
- 🟠 `warm` - Oportunidad en desarrollo (evaluando, planes anunciados)
- 🟢 `cool` - Situación estable, menos urgente (infraestructura moderna)

## Para Agregar un País Nuevo
En `index.html`:
1. Agregar código al array `countryOrder` (línea ~942)
2. Agregar entrada en `countryNames` (línea ~943)
3. Agregar opción en filtro HTML `<select id="country-filter">` (~línea 370)
4. Agregar bancos al array `banks` (antes del `];` ~línea 935)

## Países Actuales
| Código | País | Bandera |
|--------|------|---------|
| BR | Brasil | 🇧🇷 |
| MX | México | 🇲🇽 |
| CL | Chile | 🇨🇱 |
| CO | Colombia | 🇨🇴 |
| PE | Perú | 🇵🇪 |
| AR | Argentina | 🇦🇷 |
| PA | Panamá | 🇵🇦 |
| CR | Costa Rica | 🇨🇷 |
| GT | Guatemala | 🇬🇹 |

## Ejemplo: Agregar un banco
```javascript
// NUEVO PAÍS - EJEMPLO
{ 
    rank: 99, name: "Banco Ejemplo", country: "XX", countryName: "País", flag: "🏳️", 
    assets: 15, segment: "emerging", ownership: "Privado",
    roe: 14.0, cir: 48, npl: 2.5, growth: 8,
    infra: ["hybrid-cloud", "ai-exploring", "core-transition", "data-growing"],
    signals: [
        { level: "warm", text: "Señal comercial relevante" }
    ]
},
```
