import os 
import sys 

files = [

    'src/__init__.py',
    'src/components/__init__.py',
    'src/components/data_ingestion.py',
    'src/components/data_transformation.py',
    'src/components/model_trainer.py',
    'src/components/model_evaluation.py',
    'src/pipeline/__init__.py',
    'src/pipeline/training_pipeline.py',
    'src/pipeline/predictions_pipeline.py',
    'src/utils/__init__.py',
    'src/utils/utils.py',
    'src/exception/__init__.py',
    'src/exception/exception.py',
    'src/logger/logging.py',
    'src/logger/__init__.py',

    'test/unit/__init__.py',
    'test/integration/__init__.py',

    'requirements.txt',
    'requirements_dev.txt',
    'init_setup.sh',
    'setup.py',
    'setup.cfg',
    'pyproject.toml',
    'tox.ini',
    'experiments/experiments.ipynb',
    '.github/workflows/.gitkeep'

]



for file in files:
    dir = os.path.dirname(file)
    file_name = os.path.basename(file)

    if dir :
        os.makedirs(dir , exist_ok=True)
    
    if not os.path.exists(file_name):
        with open(file , 'w') as file:
            pass 