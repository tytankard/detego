# Detego technical assessment

## Creating a virtual environment

- To run the pytests a virtual environment is needed, to do this follow the below steps:
    - Ensure pip & python venv are installed on your computer
    - Create virtual environment e.g. 'python -m venv venv'
    - Activate virtual environment
    - Install dependencies with the following command: "pip install -r requirements.txt"

## Running unit tests

- In order to verify that a folders contents have succesfully been reconstructed and hashed correctly we can run the suite of tests included in this directory. To do this issue the following command:
    - python -m pytest py_tests.py

## Reconstructing files

- To reconstruct files located in 'SplitFile' run the command:
    - python file_reconstructor.py

## Future improvements

- Add a CLI wrapper to the file_reconstructor script so that any file can be restructured
