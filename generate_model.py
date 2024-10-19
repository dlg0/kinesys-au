import os


def create_model_structure():
    import os

    # Define the directory structure
    base_dir = "./"
    input_data_dir = os.path.join(base_dir, "input_data")
    scenario_data_dir = os.path.join(base_dir, "scenario_data", "scenario1")
    scripts_dir = os.path.join(base_dir, "scripts")
    docs_dir = os.path.join(base_dir, "docs")

    # Create directories
    os.makedirs(os.path.join(input_data_dir, "technologies"), exist_ok=True)
    os.makedirs(os.path.join(input_data_dir, "fuels"), exist_ok=True)
    os.makedirs(os.path.join(input_data_dir, "demand"), exist_ok=True)
    os.makedirs(os.path.join(input_data_dir, "constraints"), exist_ok=True)
    os.makedirs(os.path.join(input_data_dir, "scenarios"), exist_ok=True)
    os.makedirs(os.path.join(scenario_data_dir, "inputs"), exist_ok=True)
    os.makedirs(os.path.join(scenario_data_dir, "results"), exist_ok=True)
    os.makedirs(scripts_dir, exist_ok=True)
    os.makedirs(docs_dir, exist_ok=True)

    # Create the minimal input files

    # Technology data (adding Gas with CCS)
    tech_content = """Technology,InputFuel,Output,Efficiency,InvestmentCost(USD/kW),Lifetime(years)
CoalPlant,Coal,Electricity,0.35,1500,40
SolarPV,Solar,Electricity,1.00,800,25
WindTurbine,Wind,Electricity,1.00,1000,25
GasPlant,NaturalGas,Electricity,0.50,1000,35
GasPlant_CCS,NaturalGas,Electricity,0.45,2000,35
"""
    with open(os.path.join(input_data_dir, "technologies", "technology.csv"), "w") as f:
        f.write(tech_content)

    # Fuel prices data
    fuel_content = """Fuel,Price(USD/MWh)
Coal,50
NaturalGas,30
Solar,0
Wind,0
"""
    with open(os.path.join(input_data_dir, "fuels", "fuel_prices.csv"), "w") as f:
        f.write(fuel_content)

    # Demand data (extending to 2050)
    demand_content = """Year,Region,Demand(MWh)
2025,NSW,5000000
2030,NSW,5500000
2040,NSW,6000000
2050,NSW,6500000
"""
    with open(
        os.path.join(input_data_dir, "demand", "demand_projection.csv"), "w"
    ) as f:
        f.write(demand_content)

    # Updated Emission constraints to reflect both state-level and Tomago Aluminium
    # Introducing the carbon budget and a net-zero target by 2050
    emissions_content = """Year,Region,Technology,EmissionLimit(tons CO2)
2025,NSW,StateLevel,CoalPlant,1000000
2025,NSW,StateLevel,GasPlant,500000
2025,NSW,StateLevel,GasPlant_CCS,100000  # Reduced emissions due to CCS
2025,NSW,TomagoAluminium,AluminiumProduction,1500000
2030,NSW,StateLevel,CoalPlant,800000
2030,NSW,StateLevel,GasPlant,400000
2030,NSW,StateLevel,GasPlant_CCS,80000  # Stringent constraint on gas with CCS
2030,NSW,TomagoAluminium,AluminiumProduction,1250000  # Reflecting a 4.9% annual reduction
2040,NSW,StateLevel,CoalPlant,300000  # Phasing out coal by 2040
2040,NSW,StateLevel,GasPlant,200000  # Reduced emissions from gas
2040,NSW,StateLevel,GasPlant_CCS,50000
2050,NSW,StateLevel,NetZero,0  # Net zero emissions by 2050
"""
    with open(
        os.path.join(input_data_dir, "constraints", "emission_constraints.csv"), "w"
    ) as f:
        f.write(emissions_content)

    # Scenario definition (including the option to build Gas with CCS)
    scenario_content = """Scenario,Year,Region,Technology,CapacityAddition(MW)
Scenario1,2025,NSW,SolarPV,500
Scenario1,2025,NSW,WindTurbine,300
Scenario1,2025,NSW,GasPlant_CCS,100  # Adding Gas with CCS
Scenario1,2030,NSW,SolarPV,600
Scenario1,2030,NSW,WindTurbine,400
Scenario1,2030,NSW,GasPlant_CCS,200  # Expanding Gas with CCS capacity
Scenario1,2040,NSW,SolarPV,700
Scenario1,2040,NSW,WindTurbine,500
Scenario1,2040,NSW,GasPlant_CCS,300
Scenario1,2050,NSW,SolarPV,800
Scenario1,2050,NSW,WindTurbine,600
"""
    with open(
        os.path.join(input_data_dir, "scenarios", "scenario_definitions.csv"), "w"
    ) as f:
        f.write(scenario_content)

    # Create the model documentation in docs folder

    model_doc_content = """# KiNESYS+ Model for NSW, Australia (AusGrid Distribution Network)

## Overview
This model represents the energy system for **New South Wales (NSW)**, Australia, with a detailed focus on the **AusGrid distribution network**. The model covers various energy technologies, including conventional and renewable sources, and incorporates **Gas with Carbon Capture and Storage (CCS)** as an option to meet increasing electricity demand under stringent emissions constraints. The model simulates how different energy technologies contribute to meeting demand over time, while complying with Australia's **Safeguard Mechanism** and other emission reduction targets.

## Key Features
- **Region**: The model covers the national electricity grid with special focus on NSW.
- **Time Horizon**: The model simulates energy demand and supply between 2025 and 2050.
- **Technologies**: Includes coal, gas, gas with CCS, solar PV, and wind turbines, each with defined costs, efficiency, and emission profiles.
- **Emissions Constraints**: Applies emissions limits at the **state level** and for large industrial emitters (e.g., Tomago Aluminium) in compliance with Australia's **Safeguard Mechanism**.
- **Demand Growth**: The model captures increasing electricity demand over time in NSW.
- **Scenario Flexibility**: Users can explore various future pathways, such as expanding solar and wind capacity or introducing new technologies like gas with CCS.
"""
    with open(os.path.join(docs_dir, "model_description.md"), "w") as f:
        f.write(model_doc_content)

    # Continue the rest of the documentation
    model_doc_content_cont = """
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
"""
    with open(os.path.join(docs_dir, "model_description.md"), "a") as f:
        f.write(model_doc_content_cont)

    print("Model files and directory structure created successfully.")


def main():
    create_model_structure()
    print("Model files and directory structure created successfully.")


if __name__ == "__main__":
    main()
