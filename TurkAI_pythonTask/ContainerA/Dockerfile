# Base image
FROM python:3.9

# Set working directory
WORKDIR /turkai_python_task/TurkAI_pythonTask/ContainerA

# Copy requirements file
COPY Container A/requirements.txt 

# Install dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY turkai_python_task/TurkAI_pythonTask/ContainerA/redNotices.py /app/

# Set environment variable for interval(Çalıştırma zamanı ortam değişkenini ayarlar. )
ENV INTERVAL=300

# Run the application
CMD ["python", "redNotices.py"]
