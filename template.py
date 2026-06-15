import os
from pathlib import Path


project_name = "visa"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/Components/__init__.py",
    f"{project_name}/Components/data_ingestion.py",
    f"{project_name}/Components/data_validation.py",
    f"{project_name}/Components/data_transformation.py",
    f"{project_name}/Components/model_trainer.py",
    f"{project_name}/Components/model_evaluation.py",
    f"{project_name}/Components/model_pusher.py",
    f"{project_name}/Configuration/__init__.py",
    f"{project_name}/Constants/__init__.py",
    f"{project_name}/Entity/__init__.py",
    f"{project_name}/Entity/config_entity.py",
    f"{project_name}/Entity/artifact_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "app.py",
    "Dockerfile",
    ".dockerignore",
    "setup.py",
    "demo.py",
    "config/model.yaml",
    "config/schema.yaml"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"{filename} is already present in {filedir} and has some content. Skipping creation.")