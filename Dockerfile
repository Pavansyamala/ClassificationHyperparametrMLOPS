FROM python:3.9-slim-buster
USER root

# Create application directory
RUN mkdir -p /app/airflow/dags
COPY . /app/
WORKDIR /app/

# Install Python dependencies
RUN pip install -r requirements.txt

# Set environment variables
ENV AIRFLOW_HOME=/app/airflow
ENV AIRFLOW__CORE__DAGS_FOLDER=/app/airflow/dags
ENV AIRFLOW__CORE__SQL_ALCHEMY_CONN=sqlite:////app/airflow/airflow.db

# Initialize Airflow DB
RUN airflow db init

# Create an admin user
RUN airflow users create -e pavansyamaladata2025@gmail.com -f kasa -l pavan -p admin -r Admin -u admin

# Make the start.sh script executable
RUN chmod 777 start.sh

# Update system packages
RUN apt update -y

# Define entry point and default command
ENTRYPOINT ["/bin/sh"]
CMD ["start.sh"]
