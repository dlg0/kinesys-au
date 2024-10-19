# KiNESYS+ Model for NSW, Australia (AusGrid Distribution Network)

## Overview
This model represents the energy system for **New South Wales (NSW)**, Australia, with a detailed focus on the **AusGrid distribution network**. The model covers various energy technologies, including conventional and renewable sources, and incorporates **Gas with Carbon Capture and Storage (CCS)** as an option to meet increasing electricity demand under stringent emissions constraints. The model simulates how different energy technologies contribute to meeting demand over time, while complying with Australia's **Safeguard Mechanism** and other emission reduction targets.

## Key Features
- **Region**: The model covers the national electricity grid with special focus on NSW.
- **Time Horizon**: The model simulates energy demand and supply between 2025 and 2050.
- **Technologies**: Includes coal, gas, gas with CCS, solar PV, and wind turbines, each with defined costs, efficiency, and emission profiles.
- **Emissions Constraints**: Applies emissions limits at the **state level** and for large industrial emitters (e.g., Tomago Aluminium) in compliance with Australia's **Safeguard Mechanism**.
- **Demand Growth**: The model captures increasing electricity demand over time in NSW.
- **Scenario Flexibility**: Users can explore various future pathways, such as expanding solar and wind capacity or introducing new technologies like gas with CCS.

### Technology Parameters
- **Investment Costs**: Vary by technology, with gas with CCS being more expensive to install due to the carbon capture component.
- **Operating Costs**: Each technology has a different operational and maintenance cost, with fossil fuels having ongoing fuel costs.
- **Emission Factors**: Coal and gas produce CO2 emissions, while solar and wind are zero-emission technologies. Gas with CCS has a lower emission factor due to the capture of CO2 during the energy generation process.

## Emissions Constraints and Safeguard Mechanism
The model incorporates emissions constraints that become **increasingly stringent** over time. These constraints reflect Australia's **Safeguard Mechanism**, which applies to large emitters like **Tomago Aluminium**. Tomago Aluminium is expected to reduce emissions by **4.9% per year** as mandated by the Safeguard Mechanism.

### Emissions Reduction Targets
- **State-Level Emissions**: The model includes emissions limits for NSW, requiring a reduction of emissions from coal and gas plants over time.
- **Tomago Aluminium**: One of NSW's largest emitters, subject to the Safeguard Mechanism, must reduce its emissions from 1.5 million tons of CO2 in 2025 to 1.25 million tons in 2030, aligned with the national policy.

## Scenarios
The model supports scenario analysis for evaluating different energy transition pathways. Scenarios allow users to explore:
- **Renewable Energy Expansion**: How increasing the capacity of solar and wind can meet demand.
- **Deployment of Gas with CCS**: How the addition of gas with CCS capacity can help meet energy demand while reducing emissions.
- **Emission Reduction Pathways**: The impact of more stringent emission constraints on technology choices and system costs.

### Example Scenarios
- **Scenario 1**: This scenario assumes an increase in solar PV and wind capacity in 2025 and 2030. It also introduces gas with CCS as a potential solution to meet rising electricity demand under emissions constraints.
  
## Data Sources
- **Energy Technology Costs and Efficiencies**: Data from Australia's national energy database and international energy studies.
- **Fuel Costs**: Based on market rates for coal, natural gas, and renewable energy resources in Australia.
- **Emission Targets**: Reflecting Australia's **Safeguard Mechanism** policy and national net-zero targets for 2050.
  
## Future Work
Future improvements to the model
could include:
- Adding **energy storage** (e.g., batteries) to help balance intermittent renewable generation.
- Exploring the impact of **higher carbon prices** on technology deployment and emissions reductions.
- Expanding the model to cover **other states** in Australia or more granular regional details for NSW.

## Conclusion
This model provides a flexible and detailed tool for analyzing the energy transition in NSW, Australia, focusing on the AusGrid distribution network. It enables users to explore various pathways for meeting electricity demand while reducing emissions in line with national policies like the Safeguard Mechanism.

For more information or to contribute to the model, contact the project team.
