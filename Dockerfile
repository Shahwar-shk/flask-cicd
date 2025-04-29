# Use Python 3.9 as base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy the requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your Flask app
COPY . .

# Expose port 5000 for Flask
EXPOSE 5000

# Use gunicorn to run the app in production
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]
