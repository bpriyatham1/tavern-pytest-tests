Python based Tavern Testing Framework

Required installations:
Python 3.11(and Above)
Pip
Tavern


```pip install pipenv```

```pip install -r requirements.txt```


Prerequisite to run the test:
1. Clone the setup the project and run it using maven
https://github.com/bpriyatham1/Springboot-WeatherApplication.git
2. once the project is running test it using swagger ui
http://localhost:8080/swagger-ui/index.html#/
3. Running Tests
   1. To Run tests via tavern use below command
   ```tavern-ci weather_api_positive.tavern.yaml```
   2. To Run tests via pytest use below command
   ```python -m pytest -v -s```