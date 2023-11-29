# Use the official Python 3.11 base image
FROM python:3.11

# Set the working directory inside the container
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container at /code/
COPY ./requirements.txt /code/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Expose the port that Streamlit will run on
EXPOSE 8501

# Set up a health check to ensure the application is running properly
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Specify the command to run on container start
ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]