FROM python:3.9
WORKDIR /usr/app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 5000
#RUN pip install -r requirements.txt
# Command to run the app
CMD ["python", "app.py"]