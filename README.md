# IndODish - BackEnd

COMP6703001 - Web Application Development and Security (Final Project)

## Project Details
Here is our attempt developing the [FrontEnd](https://github.com/JugBones/indodish-frontend) and 
[BackEnd](https://github.com/JugBones/indodish-backend) of a Food Delivery Web application called IndoDish using:

`FrontEnd`
- NextJS
- TypeScript
- SCSS
- Vercel
- etc.

`BackEnd`
- PostGresQL
- FastAPI
- JWT
- Biznet Gio Cloud
- etc.

## Project Member (L4BC)
- Christopher Alexander Tjiandra (2502019230)
- Christopher Owen (2502019180)
- Vincent Yono (2502009583)

## Tools 
![](https://img.shields.io/badge/Tools-Git-informational?style=flat&logo=Git&color=F05032)
![](https://img.shields.io/badge/Tools-GitHub-informational?style=flat&logo=GitHub&color=181717)
![](https://img.shields.io/badge/Tools-Visual-Studio?style=flat&logo=VisualStudioCode&color=0044F9)
![](https://img.shields.io/badge/Language-TypeScript-informational?style=flat&logo=typescript&color=blue)
![](https://img.shields.io/badge/Database-PostGresQL-informational?style=flat&logo=postgresql&color=yellow)
![](https://img.shields.io/badge/Tools-FastAPI-informational?style=flat&logo=fastapi&color=purple)
![](https://img.shields.io/badge/Tools-Vercel-informational?style=flat&logo=vercel&color=black)

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
