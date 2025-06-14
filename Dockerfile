# official image from python
FROM python:3.13-slim

# stablish work directory for the container
WORKDIR /app

# copy the file with the dependencies
COPY requirements.txt .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy all the code to the container
COPY  . .

# port for the container
EXPOSE 8000

# command to execute the app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]