# -TransBorder-Freight-Data-Analysis-Project
 TransBorder Freight Data Analysis Project

**Project Overview**
This project analyzes cross-border freight transportation data provided by the U.S. Bureau of Transportation Statistics (BTS) using the CRISP-DM methodology. The goal is to uncover insights into freight movement, identify inefficiencies, and provide actionable recommendations on safety, environmental impact, and economic disruptions.

## 📌 Objectives
- Uncover freight movement patterns
- Identify operational inefficiencies
- Investigate the effect of economic disruptions
- Provide actionable data-driven recommendations

## 📊 Business Questions
1. Which modes of transportation carry the largest freight volumes over time?
2. How does freight volume vary by region and time?
3. Where do inefficiencies like operational cost?
4. Which transportation modes carries goods with more value?
5. What underutilized routes or modes can be optimized?
6. How have economic events affected freight efficiency?
7. What is export rate compared to import rate by states?


## 🧰 Tools & Technologies
| Tool | Description |
|------|-------------|
| **Python** | Main programming language for data processing |
| **Pandas** | Data cleaning and manipulation |
| **Seaborn/Matplotlib** | Visualizations and trend analysis |
| **Jupyter Notebooks** | EDA, documentation, and analysis |
| **Git/GitHub** | Version control and project hosting |

---

## Executive Summary
This report presents a comprehensive analysis of freight transport data with the goal of identifying trends, operational efficiencies, and areas for improvement. The analysis focuses on shipment volumes, weight distributions, transportation modes, and geographical shipping patterns. Insights derived from this study can support strategic decision-making for logistics optimization, resource allocation, and environmental planning.

## Introduction
Freight transport plays a vital role in supply chain management. Analyzing historical data provides actionable insights into improving logistics operations. This analysis was conducted on a dataset containing information on shipments, including origin-destination pairs, transport modes, distances, weights, and other logistics parameters.

## Data Overview
The dataset includes the following key variables:

* Origin and Destination (city/country)
* Mode of Transport (Road, Rail, Air, Sea)
* Shipment Weight and Volume
* Transport Distance (km)
* Transport Cost
* Shipment Frequency

Initial data cleaning was performed to handle missing values, normalize data formats, and ensure consistency across categorical variables.



## Key Findings
### Transport Mode Utilization
* Road transport dominates short-distance routes, especially for regional shipments.
* Rail transport is underutilized despite cost-efficiency in bulk and long-distance freight.
* Air freight accounts for the smallest share but is primarily used for time-sensitive deliveries.
* Sea freight is heavily used for international trade, particularly for high-weight shipments.

### Shipment Weight Distribution
* Majority of shipments fall within the 1–10 tons weight bracket.
* Heavy shipments (>20 tons) are more common in sea and rail transport, suggesting optimal mode selection based on weight.

### Geographic Insights
* High-volume corridors include major cities and ports (e.g., Hamburg, Rotterdam, Milan).
* A notable clustering of shipments was observed around central logistics hubs, suggesting strategic network positioning.

### Transport Efficiency
* Efficiency metrics show that rail and sea provide better cost-per-ton-km ratios.
* Air transport has the highest cost and carbon footprint per unit, justifying its use only when necessary.
* Road transport shows a moderate balance but presents congestion issues in urban centers.

## Recommendations
### Optimize Mode Selection
* Encourage modal shift from road to rail or sea where feasible to reduce costs and emissions.
* Improve infrastructure to support intermodal transport systems.

### Improve Route Planning
* Leverage data to identify optimal shipping routes, reducing distance and fuel consumption.
* Use AI-assisted logistics for real-time route adjustments.

### Invest in Rail and Sea Logistics
* Rail networks need better integration and investment to support bulk inland transport.
* Sea freight logistics could be enhanced with digitization and port automation.

### Sustainability and Emissions Tracking
* Adopt greener practices through low-emission transport modes.
* Track CO₂ emissions per shipment and incorporate sustainability KPIs into logistics planning.

## Conclusion
The freight transport dataset reveals a number of actionable insights that can help optimize logistics strategies. A shift towards more cost-effective and sustainable transport modes, coupled with data-driven planning, can significantly enhance operational efficiency. Further analysis integrating real-time tracking and external data (e.g., weather, traffic) is recommended for predictive modeling and dynamic optimization.
