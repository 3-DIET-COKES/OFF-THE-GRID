# OFF-THE-GRID

It is an automated, open-source microgrid planning tool designed to size and simulate hybrid solar, wind, and battery storage infrastructure for remote connectivity nodes.

## Overview:

Off the Grid bridges the gap between complex energy engineering and field operations. Built for NGO disaster response teams, rural operators, and connectivity initiatives, the platform replaces expensive enterprise software and static spreadsheets with an intuitive, one-click geospatial tool.
By automatically ingesting satellite telemetry from the NASA POWER API, the app calculates precise microgrid sizing requirements to maintain continuous 99.9% uptime for critical communication hardware (e.g., Starlink terminals, LoRaWAN gateways, cellular repeaters).

## Key Features:

**Instant Geospatial Telemetry:** Automatically fetches historical solar irradiance ($kWh/m^2/day$), wind speed ($m/s$), and ambient temperature directly from NASA satellites for any global coordinate.

**Hybrid Sizing Engine:** Computes optimal hardware parameters for solar PV capacity, vertical/horizontal wind turbines, and LiFePO4 battery banks.

**24-Hour Digital Twin:** Runs dynamic, time-series simulations visualizing generation curves against battery State-of-Charge ($SoC$) across a synthetic 24-hour cycle.

**Automated Bill of Materials (BOM):** Generates an itemized hardware shopping list alongside total cost estimates and financial payback metrics compared to legacy diesel generators.

**Offline-First UI:** Designed for low-bandwidth field environments using responsive Mapbox GL maps and clean data visualizations.


## Tech Stack

**Frontend**

**Framework:** React + Vite
**Styling:** Tailwind CSS + Shadcn/ui
**Mapping:** Mapbox GL JS / React-Map-GL
**Data Visualization:** Recharts

**Backend Engine**

**API Framework:** Python / FastAPI
**Data Fetching:** HTTPX / Requests
**Mathematical Operations:** NumPy + Pandas

**External Data**

**Solar & Wind Telemetry:** NASA POWER API
**Geocoding:** Mapbox Geocoding API

---

## Architecture & Data Pipeline

```text
[ React / Mapbox GL UI ] 
        │
        ▼ (Lat / Long Pin Drop)
[ FastAPI Backend ]
        │
        ├─► [ NASA POWER API Ingestion Layer ] (Solar Irradiance, Wind Speed, Temp)
        │
        ├─► [ Mathematical Sizing Engine ] (PV Watts, Wind Kinetic Energy, DoD Battery Sizing)
        │
        └─► [ 24-Hour Digital Twin Simulation ] (Time-Series Generation & SoC Vectors)
