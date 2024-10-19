# KiNESYS+ Model for NSW (AusGrid Distribution Network)

## Overview
This project contains a minimal **KiNESYS+ energy model** for the **NSW (New South Wales)** region, focusing on the **AusGrid distribution network**. The model is set up to explore different scenarios for the energy transition, including options for renewable energy expansion, fossil fuel phase-out, and **gas with Carbon Capture and Storage (CCS)**. The time horizon extends from **2025 to 2050**, with an emphasis on achieving **net-zero emissions** by 2050.

## Directory Structure
The project is organized as follows:
```
/minimal_kinesys_ausgrid_model
    /input_data
        /technologies             # Definitions of technologies (e.g., solar PV, gas with CCS)
        /fuels                    # Fuel price data (e.g., coal, natural gas)
        /demand                   # Demand projections for NSW
        /constraints               # Emission constraints, including carbon budgets
        /scenarios                 # Scenario definitions (capacity additions, technology mix)
    /scenario_data
        /HighRenewable             # High renewable energy deployment scenario
            /inputs
            /results
        /Balanced                  # Balanced fossil fuel and renewable mix scenario
            /inputs
            /results
        /AggressivePhaseOut        # Aggressive fossil fuel phase-out scenario
            /inputs
            /results
    /scripts                       # Scripts for running, processing, and visualizing the model
    /docs                          # Model documentation (model_description.md)
```

## Requirements
You will need the following software to run the model:
- **Veda2.0** for running the model locally on your machine.
- **VedaOnline** for running the model on the web-based platform.

### Running in Veda2

1. **Set Up a New Project**:
   - Open **Veda2** and create a new project.
   - Define the **regions**, **technologies**, and **time slices** (2025–2050) as per the model requirements.

2. **Import Input Data**:
   - Navigate to the **input_data** folder and import the following files:
     - `technologies/technology.csv`: Defines the available technologies.
     - `fuels/fuel_prices.csv`: Lists the fuel prices.
     - `demand/demand_projection.csv`: Contains energy demand data for NSW.
     - `constraints/emission_constraints.csv`: Specifies the emission limits.
     - `scenarios/scenario_definitions.csv`: Scenario-specific capacity additions for each technology.

3. **Define Scenarios**:
   - Set up **scenarios** using the data in the `scenario_definitions.csv` file, or you can use the pre-defined scenarios in the `scenario_data` folder.
   - If needed, adjust parameters to reflect alternative pathways (e.g., renewable energy deployment, fossil fuel phase-out).

4. **Run the Model**:
   - Run the model by selecting the scenario you want to analyze (e.g., **HighRenewable**, **Balanced**, **AggressivePhaseOut**).
   - The model will generate results, including energy production, emissions, and costs for the selected scenario.

5. **Analyze Results**:
   - Once the model completes, use **Veda2's output tools** to analyze the results. Outputs will include emissions trajectories, energy production, and costs by year and technology.

### Running in VedaOnline

1. **Log In to VedaOnline**:
   - Access the **VedaOnline** platform through your web browser and log in with your credentials.

2. **Create a New Project**:
   - Within VedaOnline, create a new project to import your model files.
   - Define the **regions**, **technologies**, and **time slices** as needed.

3. **Upload Input Files**:
   - Upload the following input files from the **input_data** folder:
     - `technology.csv` (from the `technologies` folder).
     - `fuel_prices.csv` (from the `fuels` folder).
     - `demand_projection.csv` (from the `demand` folder).
     - `emission_constraints.csv` (from the `constraints` folder).
     - `scenario_definitions.csv` (from the `scenarios` folder).
  
4. **Upload Scenario-Specific Inputs**:
   - For each scenario, upload the scenario input files located in the `scenario_data/{scenario_name}/inputs` folder.
   - Example for the **HighRenewable** scenario:
     ```
     /scenario_data/HighRenewable/inputs/scenario_inputs.csv
     ```

5. **Run the Model**:
   - Once the inputs are uploaded, run the model for the selected scenario.
   - Monitor the progress on the platform. Upon completion, results will be stored in the corresponding **results** folder under `/scenario_data/{scenario_name}/results`.

6. **Analyze Results**:
   - Use VedaOnline's built-in tools to visualize and analyze the results of your model run.
   - Outputs may include **emissions profiles**, **technology deployment**, **energy production**, and more.

## Example Scenarios
The following scenarios are included:
1. **HighRenewable**: Focuses on rapid renewable energy deployment.
2. **Balanced**: A balanced transition with gradual coal phase-out and introduction of gas with CCS.
3. **AggressivePhaseOut**: Aggressive phase-out of fossil fuels by 2030, with heavy reliance on gas with CCS.

## Scripts
You can use the scripts in the **`/scripts`** folder to automate common tasks:
- **`run_model.sh`**: Run the model for a specific scenario.
- **`process_results.py`**: Process and analyze the results after running the model.
- **`visualize_results.py`**: Generate plots and charts from the model outputs.

## Contact
For questions or collaboration opportunities, please contact the project team.
