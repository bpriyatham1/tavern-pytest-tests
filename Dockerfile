FROM python:3.11.3-alpine

# Labels
LABEL maintainer="bpriyatham1@gmail.com, gmail.com"

RUN pip install tavern

# RUN mkdir /pytest-tavern-container/
# ADD .  /pytest-tavern-container/
# WORKDIR /pytest-tavern-container/
# RUN pip install --upgrade pip
# RUN pip install -r requirements.txt
# RUN pip install tavern
# ENTRYPOINT pytest -s -v -m ${GROUP} --disable-warnings



