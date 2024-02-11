FROM python:3.11
WORKDIR /app
COPY requirements.txt /app
COPY main.py /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD [ "python", "main.py" ]