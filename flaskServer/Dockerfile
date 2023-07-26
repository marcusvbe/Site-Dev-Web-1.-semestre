FROM python:latest
RUN apt-get update 
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /flaskProject
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000", "--debug"]
