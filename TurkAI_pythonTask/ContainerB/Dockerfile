# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r /app/requirements.txt

# Copy application code
COPY connect_db.py /app/
COPY myflaskapp/app.py /app/
COPY myflaskapp/templates/index.html /app/myflaskapp/templates/
COPY start_app.sh /app/


RUN chmod +x /app/start_app.sh

# Expose port for web server
EXPOSE 80

# Run the application
CMD ["/app/start_app.sh"]
