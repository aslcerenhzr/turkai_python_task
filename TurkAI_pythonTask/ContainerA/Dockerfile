# Base image
FROM python:3.9

# Set working directory
WORKDIR /turkai_python_task/TurkAI_pythonTask/ContainerA

# Copy requirements file
COPY requirements.txt /app/

# Install dependencies 
RUN pip install -r /app/requirements.txt
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update
RUN apt-get install -y google-chrome-stable

# Copy application code
COPY redNotices.py /app/

# Set environment variable for interval(Çalıştırma zamanı ortam değişkenini ayarlar. )
ENV INTERVAL=300

# Run the application
CMD ["python", "/app/redNotices.py"]