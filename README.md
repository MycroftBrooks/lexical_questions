# Lexical Questions
Lexical questions was developed for teachers, who wants to get some examples (up to 30) of sentences for their students. For example, you can get sentences with the word "***sheep***". Also you get some information and examples with this word from [cambirdge dictionary](https://dictionary.cambridge.org/dictionary/english-russian/sheep).
## Installation:
1. First you need to create a virtual environment:
   for this you need to use the command - `python -m venv venv` (for Windows), `python3 -m venv venv` (for macOS)
2. Next, you need to activate the virtual environment - `venv\Scripts\Activate.ps1` (for Windows), `source venv/bin/activate` (for macOs)
3. The next step is to install the necessary dependencies - `pip install -r requirements.txt` (for all platforms)
4. Make migrations - `python manage.py makemigrations` (for Windows) or `python3 manage.py makemigrations` (for macOS) and `python manage.py migrate` (for Windows) or `python3 manage.py migrate` (for macOS)
5. ***THIS STEP IS REQUIRED IF YOU WANT TO USE AUTH SYSTEM.*** Create a superuser - `python manage.py createsuperuser` (for Windows) or `python3 manage.py createsuperuser` (for macOS)
6. Make application in [Reddit api website](https://www.reddit.com/prefs/apps). Write in .env file your API keys from Reddit, enter secret key for Django app (you can generate it [here](https://djecrety.ir/)), and write your email address with app password if you want to use email sending function.
## Usage
1. ***THIS STEP IS REQUIRED IF YOU WANT TO USE CHANGE THEME OPTION!*** You need to install [node.js and npm](https://nodejs.org/en/download/). Open `parser` directory and run `python manage.py tailwind start` (for Windows) or  `python3 manage.py tailwind start` (for macOS) in seperate terminal *(in first terminal you need to run server, in second terminal you need to run tailwind)*.
2. Run the server - `python manage.py runserver` (for Windows) or `python3 manage.py runserver` (for macOS) 


> App running on ```http://127.0.0.1:8000/```
