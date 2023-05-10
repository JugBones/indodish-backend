# IndODish-BackEnd

## File Structure

[Reference](https://github.com/zhanymkanov/fastapi-best-practices#4-chain-dependencies)

## Prerequisite

Before running the application be sure to create **.env** file on the root folder, please use the following template

```env
DATABASE_URI = "<your_postgresql_uri>"
ACCESS_TOKEN_SECRET_KEY = "<access_token_secret_key>"
REFRESH_TOKEN_SECRET_KEY = "<refresh_token_secret_key>"

```

## Scripts

Running the app with hot reload, use http://localhost:8000 to access it.
open http://localhost:8000/docs to access the documentation

```bash
uvicorn src.main:app --reload
```

## Installing packages

**There might be more packages later, be sure to check and update your environment**

### Using conda

[Conda documentation](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

Creating environment

```bash
conda env create --name <environment_name> python=3.10
```

Activating environment

```bash
conda activate <environment_name>
```

Installing packages

```bash
pip install -r ./requirements/dev.txt
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
pip install -r ./requirements/dev.txt
```
