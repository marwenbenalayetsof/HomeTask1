# Project Title: Data Engineering ETL and API Service

## Description
This project implements an ETL (Extract, Transform, Load) pipeline using PySpark to process data and a FastAPI application to expose the processed data through RESTful APIs. It's designed to demonstrate data engineering practices, including data ingestion from CSV files, data transformation, loading into SQLite database, and serving data via API.

## Installation
Ensure you have Python 3.8+, Java 11, and Spark 3.1.2 installed on your system.

### Dependencies
- PySpark
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite JDBC

Install Python dependencies using:
pip install -r requirements.txt


### Spark Setup
Download Spark and include the JDBC driver for SQLite in your Spark job's classpath.

## Usage

### Starting the ETL Process
Run the PySpark script to process your CSV data and load it into the SQLite database:
spark-submit --jars path/to/sqlite-jdbc.jar your_etl_script.py


### Running the API Server
Start the FastAPI server using:
uvicorn main:app --reload


## Running the Tests
To run the tests for both the ETL process and the API, use:
pytest


## Docker Setup
To containerize the application, use the provided Dockerfile:
docker build -t test-image:latest .
docker run -p 8000:8000 test-image:latest
## API Reference
### Read First Chunk
- **URL**: `/read/first-chunck`
- **Method**: `GET`
- **Success Response**: Code: 200, Content: first 10 rows from the database.

## Kubernetes Setup
To run the application using k8s, use the provided command:
kubectl apply -f app_deployment.yaml

## Script Shell Setup
To run the application using script Shell :
./deploy.sh


## Contributing
Please read [CONTRIBUTING.md](LINK_TO_YOUR_CONTRIBUTING_GUIDELINES) for details on our code of conduct, and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.

## Authors and Acknowledgment
- Marwen Ben Alayet - Initial work

## FAQs
Q: How do I change the database configuration?
A: Edit the `DATABASE_URL` in the main.py file.

## Contact Information
For any queries, please open an issue in the GitHub repository or contact "marwen.benalayet.sof@gmail.com".
