# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system-level dependencies required by scikit-learn
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    python3-dev \
    libopenblas-dev \
    liblapack-dev && \
    rm -rf /var/lib/apt/lists/*

# Copy the project files into the container
COPY model2.pkl /app/
COPY tfidfvect2.pkl /app/
COPY model.pkl /app/
COPY tfidfvect.pkl /app/
COPY . .

# Install dependencies one by one
RUN pip install --no-cache-dir Flask==2.0.3  # Flask 2.x version for compatibility with newer features
RUN pip install --no-cache-dir Flask_WTF==0.15.1  # Flask-WTF compatible with Flask 2.x
RUN pip install --no-cache-dir WTForms==2.3.1  # Same version of WTForms

# Install scikit-learn with its system dependencies
RUN pip install --no-cache-dir scikit-learn

# Install pandas
RUN pip install --no-cache-dir pandas

# Install nltk
RUN pip install --no-cache-dir nltk==3.4.5  # Ensure nltk is installed

# Install Werkzeug 2.x (compatible with Flask 2.x)
RUN pip install --no-cache-dir werkzeug==2.0.3

# Install the remaining dependencies
RUN pip install --no-cache-dir gunicorn==20.0.4
RUN pip install --no-cache-dir joblib==0.14.1

# Clean up unnecessary files to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Expose the port the app runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
