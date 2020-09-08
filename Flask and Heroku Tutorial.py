#Deploying a Flask app on Heroku
"""
REQUIREMENTS:
1. Git account
2. Heroku account
3. Heroku CLI/toolbelt (install here: https://devcenter.heroku.com/articles/heroku-cli#download-and-install) or via npm using:
    $ npm install -g heroku
    $ heroku --version          #verify npm has intalled heroku correctly

"""
### 1. Create simple Flask app (source: https://realpython.com/flask-by-example-part-1-project-setup/)

#       1.1 create required folders and files to start flask project
"""
In shell
1. create a directory for flask project

mkdir flask-by-example && cd flask-by-example

2. initialise new git repo within working directory
git init

3. create virtual env for python
python -m venv env

4. Create required files for flask project
 type nul > app.py
 type nul > .gitgnore
 type nul > README.md
 type nul > requirements.txt

5. Add required packages to requirements files
python -m pip freeze > requirements.txt

"""

#       1.2 Add requirements to app.py file
"""
open app.py file and add following code:

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()
    
"""
#       1.3 Run app.py
"""
In shell
python app.py
"""

#       1.4 Create Procfile
"""
In Shell
type nul > Procfile

Open Procfile and add following text:
web: gunicorn app:app
"""

#       1.5 Add guicorn for Heroku
"""
In Shell
python -m pip install gunicorn==20.0.4
python -m pip freeze > requirements.txt
"""

#       1.6 Add appropriate python runtime for Heroku
"""
In shell
type nul > runtime.txt
python --version            #check your python version

Open runtime.txt and add following text:
python-3.8.5                #enter your python version
"""

#       1.7 Commit changes to git (use commit tab in pycharm or press Ctrl+K) -optional
"""
Add commit message:
Deploy flask app to Heroku
"""
#       1.8 create new heroku app
