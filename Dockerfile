FROM python:3.8-slim

# Install Java (required by Spark)
RUN apt-get update 
RUN apt-get install -y default-jdk
# Set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/default-java
ENV PATH $JAVA_HOME/bin:$PATH

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy your application code
COPY . /app
WORKDIR /app

# Expose port for FastAPI
EXPOSE 8000

# Run FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]