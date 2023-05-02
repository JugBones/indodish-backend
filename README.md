# IndODish-BackEnd

## Scripts

Running the app with hot reload, use http://localhost:8000 to access it.
open http://localhost:8000/docs to access the documentation

> uvicorn main:app --reload

## Installing packages

**There might be more packages later, be sure to check and update your environment**

### Using conda

[Conda documentation](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

Installing environment

```bash
conda env create -f environment.yml
```

Installing packages

```bash
conda install --name indodish-backend spec-file.txt
```

### Using venv

[virtualenv guides](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)

Installing virtualenv

```bash
pip install virtualenv
```

Creating virtual environment

```bash
python -m venv venv
```

Activating the virtual environment

Windows

```bash
.\venv\Scripts\activate
```

MacOS / Linux

```bash
source ./venv/bin/activate
```

Installing packages

```bash
pip install -r requirements.txt
```
