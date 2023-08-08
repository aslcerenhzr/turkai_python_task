# Base image
FROM python:3.9

# Set working directory
WORKDIR /turkai_python_task/TurkAI_pythonTask/ContainerB

# Copy requirements file
COPY ContainerB/requirements.txt 

# Install dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY ContainerB/connect_db.py
COPY ContainerB/myflaskapp/app.py
COPY ContainerB/myflaskapp/templates/index.html

# Expose port for web server
EXPOSE 80

# Run the application
CMD ["./start_app.sh"]
