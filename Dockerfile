FROM python:3.9-slim
WORKDIR /usr/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 5000
#RUN pip install -r requirements.txt
# Command to run the app
CMD ["python", "app.py"]