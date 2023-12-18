# Project Currecies checker

### Description:

Currencies checker is a mini app for getting a current information about USD and EUR. This app is built on FastAPI framework and polls the external API https://api.currencybeacon.com/v1/ on command.

### How to install a project:

Clone the repository and go to it on the command line:

```
git clone git@github.com:Starkiller2000Turbo/currencies_checker.git
cd currencies_checker
```

Create and activate a virtual environment for Windows:

```
python -m venv venv
source venv/Scripts/activate
```

For Linux:

```
python3 -m venv venv
source venv/bin/activate
```

Update pip:

```
make pip
```

Dependency files are separated according to the following purposes:

```
requirements.txt - requirements for running the backend basics of the application
make req

requirements-style.txt - requirements for styling code during development
make style-req

```

For the application to work, a .env file is required:

```
touch .env
```

You need to fill out the .env (server.env) file with the following:

```
ACCESS_KEY = zf3ZlGtTE6oIdgZAjk8sI1TO0drMreVf
Key for accessing https://api.currencybeacon.com/v1/ API.
```

### How to run backend:

Launch the application:

```
make run
```

The application will be available via this address:
```
127.0.0.1:8000
```

API documentation will be awailable at:
```
127.0.0.1:8000/api/docs
```

### Data storage

Data is stored in data folder
```
cd app/data
```
The file name is the last day of the week for which the exchange rate information was collected

### Endpoints

| Endpoint           |Method | Body   | Response                         | Commentary  |
|--------------------|-------|--------|----------------------------------|-------------|
|api/v1/currencies/  |GET    |        | ``` {"message":"successfull"}``` |             |

### Technology stack used in the project:

- JSON
- FastAPI
- Pydantic
- Python
- Swagger
- Uvicorn

<p align="left">
<a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="45" height="45" alt="Python" /></a>
<a href="https://fastapi.tiangolo.com/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/fastapi-colored.svg" width="45" height="45" alt="Fast API" /></a>
<a href="https://pydantic-docs.helpmanual.io/" class="external-link" target="_blank"> <img src="https://avatars.githubusercontent.com/u/110818415?s=48&v=4" alt="pydantic" width="45" height="45"/> </a>
<a href="https://www.swagger.io/" target="_blank" rel=”noopener”> <img src="https://cdn.svgporn.com/logos/swagger.svg" alt="swagger" width="45" height="45"/> </a>
<a href="https://www.github.com/" target="_blank" rel=”noopener”>  <img src="https://github.githubassets.com/assets/GitHub-Mark-ea2971cee799.png" alt="swagger" width="45" height="45"/> </a> 
</p>

### Authors:

- :white_check_mark: [Maksim Ermoshin](https://github.com/Starkiller2000Turbo)
