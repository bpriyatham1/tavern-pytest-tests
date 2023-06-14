Python based Tavern API Testing Framework

### Required Installations

#### The following are needed for executing Robot Framework tests:

Required installations:
Python 3.11(and Above)
Pip
Tavern

For installation of Pytest, Tavern and the related Python libraries, using pip is recommended. You just need to execute:

```pip install -r requirements.txt```

For a complete list of libraries that are used by system tests, see the `requirements.txt` file.

#### Set up using `virtualenv` (Windows/Mac)

`virtualenv` allows using different versions of python in the same machine and removes permission problems that can
occur during the installation of libraries as below:

`pip install virtualenv` (Windows/Mac)

1. Create a new virtual environment in the working directory
   `py -3 -m virtualenv ./python3_env` (Windows)
   or
   `python -m virtualenv ./python3_env` (Mac)
2. Activate the new environment
   `.\python3_env\Scripts\activate.bat` (Windows)
   or
   `source ./python3_env/bin/activate` (Mac)

Prerequisite to run the test:

1. Clone the setup the project and run it using maven
   https://github.com/bpriyatham1/Springboot-WeatherApplication.git
2. once the project is running test it using swagger ui
   http://localhost:8080/swagger-ui/index.html#/
3. Running Tests
    1. To Run tests via tavern use below command
       ```tavern-ci test_weather_api.tavern.yaml```
    2. To Run tests via pytest use below command
       ```python -m pytest -v -s```
    3. To generate report run below command
       ```pytest --html=report.html```

Running the tests:

```pip install pipenv```

```pip install tavern[pytest]```

```py.test test_weather_api.tavern.yaml -v --html=report.html```

```pytest --html=report.html```

Viewing the report:
![report.JPG](resources%2Freport.JPG)
![report-html.JPG](resources%2Freport-html.JPG)