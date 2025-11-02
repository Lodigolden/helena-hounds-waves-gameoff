# helena-hounds-waves-gameoff
Our submission for the Github 2025 Gameoff

# Developing
## Creating a Virtual Environment
Build your virtual environment:
> python -m venv venv

Activate the environment:

**Windows**
> venv\Scripts\activate

**Linux**
> source venv/bin/activate

Activate the virtual environment every time you develop.

## Adding and Updating Dependencies
By maintaining a requirements.txt file, it's very easy for other developers to pull in the packages they need to run the scripts.

**Adding Packages**
> pip freeze > requirements.txt

**Pulling in Packages**
> pip install -r requirements.txt

## Running
From root directory, run the following command:

> python -m main

## Linting
Linting is important because it keeps code consistent and easier to read. After pulling in the packages from the requirements.txt file, you can use Black to automatically lint code.

> black **your_file.py**

> black **your_directory/**
