# Dashboard Standards - LATAM Bank Intelligence

## Estándar de Campos para Bank Comparison Tables

Todas las tablas de comparación de bancos deben usar estos campos:

| Campo | Descripción | Fuente |
|-------|-------------|--------|
| Rank | Posición por activos totales | Superintendencia local |
| Bank | Nombre del banco | - |
| Assets (USD) | Activos totales en USD | Estados financieros |
| **CAGR** | Compound Annual Growth Rate de activos (3 años) | Calculado: (Final/Inicial)^(1/3)-1 |
| Mkt Share | % del mercado de colocaciones | Superintendencia |
| ROE | Return on Equity | Estados financieros |
| CIR | Cost-to-Income Ratio (Eficiencia) | Estados financieros |
| NPL | Non-Performing Loans ratio | Superintendencia |
| Opp | Rating comercial (🟢/🟡/🔴) | Análisis propio |
| Action | Link a detalle | - |

## Estándar de Fuentes

Cada tabla DEBE incluir:
1. Año de los datos (ej: "Datos 2024" o "Datos Q3 2024")
2. Fuente primaria (Superintendencia del país)
3. Fuente secundaria (Memorias anuales, IR pages)

## Fuentes por País

### Ecuador
- Superintendencia de Bancos: https://www.superbancos.gob.ec
- Boletines: https://www.superbancos.gob.ec/bancos/catastro-publico-bancos-privados/
- Datos actuales: **2025** (Estimado cierre año)
- CAGR período: **2022→2025**

### Perú  
- SBS: https://www.sbs.gob.pe
- Estadísticas: https://www.sbs.gob.pe/app/stats_net/stats/EstadisticaBoletinEstadistico.aspx?p=1
- Datos actuales: **Nov 2025** (SBS boletín mensual)
- CAGR período: **2022→2025**

## Conversiones de Moneda

**🚨 REGLA: TODOS los valores monetarios deben estar en USD**

- **Perú:** PEN/USD = 3.72
- **Colombia:** COP/USD = 4,150
- **Ecuador:** USD (economía dolarizada)

Siempre mostrar en USD para comparabilidad. Incluir nota con tipo de cambio usado.

## Assets en USD (para comparabilidad)
| País | Banco | Assets Local | Assets USD |
|------|-------|--------------|------------|
| PE | BCP | S/205B | ~$55B |
| PE | BBVA | S/95B | ~$25B |
| PE | Interbank | S/68B | ~$18B |
| PE | Scotiabank | S/62B | ~$17B |
| EC | Pichincha | $14.2B | $14.2B |
| EC | Guayaquil | $6.1B | $6.1B |
| EC | Produbanco | $5.4B | $5.4B |
| EC | Pacífico | $5.2B | $5.2B |
| EC | Internacional | $4.1B | $4.1B |

## Timestamp en Footer

**SIEMPRE** actualizar el timestamp en el footer de todas las páginas:
- Ubicación: sidebar footer, donde dice versión
- Formato: `v[X.X] • DD/MM HH:MM ECT`
- Zona horaria: **Ecuador (ECT = UTC-5)**
- Ejemplo: `v3.2 • 05/02 09:10 ECT`

Esto aplica a TODAS las páginas del dashboard.

---
*Última actualización: 05/02 09:10 ECT*
