FROM python:3.9-slim
WORKDIR /usr/app
RUN pip install -r requirements.txt
COPY app.py .
COPY requirements.txt .
EXPOSE 5000
#RUN pip install -r requirements.txt
# Command to run the app
CMD ["python", "app.py"]