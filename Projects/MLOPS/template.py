'''Script for automatic creation of project files'''
import os
from pathlib import Path
import logging

# to see log in terminal (saves the time when code was executed and error message)
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') 

project_name = 'mlProject'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config.configg.yaml",
    "paramas.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files: # starts a loop where each element in list_of_files is assigned to the variable filepath
    filepath = Path(filepath) # Path(filepath) converts the string filepath into a Path object, which is part of the pathlib module.
    filedir, filename = os.path.split(filepath) # os.path.split(filepath) splits the filepath into filedir: The directory portion of the path (everything up to the last directory separator). filename: The base name of the file (everything after the last directory separator).

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file {filepath}")
    else:
        logging.info(f"{filename} already exists")