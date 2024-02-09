# Use an official Python base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file (if you have one) and install dependencies
COPY requirements.txt .
COPY .env .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Specify the command to run the application
CMD ["python", "bot.py"]