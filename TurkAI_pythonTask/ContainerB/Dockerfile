# Base image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r /app/requirements.txt

# Install PostgreSQL
RUN apt update && apt install -y postgresql postgresql-contrib

# Copy application code
COPY connect_db.py /app/
COPY myflaskapp/app.py /app/myflaskapp/
COPY myflaskapp/templates/index.html /app/myflaskapp/templates/
COPY start_app.sh /app/
COPY pg_hba.conf ../etc/postgresql/15/main/pg_hba.conf

# Give execute permissions to the startup script
RUN chmod +x /app/start_app.sh

# Expose port for web server
EXPOSE 5000

# Run the application
CMD ["/app/start_app.sh"]