FROM python:3.9-slim
WORKDIR /usr/app
COPY app.py .
COPY requirements.txt .
EXPOSE 5000
RUN pip install -r requirements.txt
#RUN pip install -r requirements.txt
# Command to run the app
CMD ["python", "app.py"]