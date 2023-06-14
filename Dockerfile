FROM python:3.11.3-slim
RUN mkdir /pythonProject/
ADD .  /pythonProject/
WORKDIR /pythonProject/
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT py.test test_weather_api.tavern.yaml -v --network=my-network --html=report.html
#Below command is to run both pytest and tavern tests
#ENTRYPOINT pytest --html=report.html
