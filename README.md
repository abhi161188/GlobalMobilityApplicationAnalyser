## Workflow

1. constant
2. config_entity
3. artifacte_entity
4. component
5. pipeline
6. app.py / demo.py


## How to run?

1. Clone the repository:
   ```bash
   git clone https://github.com/abhi161188/GlobalMobilityApplicationAnalyser.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Global-Mobility-Application-Analyzer
    ```
3. Initialize your project using below command.
    ```bash
    uv init
    ```
3. Create and activate a virtual environment:
    ```bash
    uv add venv
    ```
    ```bash
    source .venv/bin/activate
    ```
4. Install the required dependencies:
    ```bash
    uv add -r requirements.txt
    ```
### Export the environment variable
```bash
export MONGODB_URL = "your_mongodb_connection_string
```