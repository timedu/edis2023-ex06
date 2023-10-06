FROM python:3.9-slim
WORKDIR /home/app
COPY dockerfiles/requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
