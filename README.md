# IndODish-BackEnd

## Scripts

Running the app with hot reload, use http://localhost:8000 to access it

> uvicorn main:app --reload

## Installing packages

**There might be more packages later, be sure to check and update your environment**

### Using conda

[Conda documentation](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

Installing environment

> conda env create -f environment.yml

Installing packages

> conda install --name indodish-backend spec-file.txt

### Using venv

[virtualenv guides](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

Installing virtualenv

> pip install virtualenv

Creating virtual environment

> python -m venv venv

Activating the virtual environment

Windows

> .\venv\Scripts\activate

MacOS / Linux

> source ./venv/bin/activate

Installing packages

> pip install -r requirements.txt
