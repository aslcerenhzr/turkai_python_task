TURK AI ARTIFICIAL INTELLIGENCE INFORMATION AND SOFTWARE SYSTEMS INC.
Python Developer Task: Interpol Data Flow and Web Server

This project involves a Python application that retrieves wanted persons data published by Interpol, stores it in a database, and shares it through a web server. This project is configured to work in a Docker environment and consists of three separate containers.

# Architecture

This project follows a three-container architecture:

- **Container A**: Retrieves Interpol's wanted persons data at specific intervals and sends it to the queue system in Container C.

- **Container B**: A Python-based web server. It listens to the queue in Container C and stores the received data in the desired database. The information is presented in an HTML web page along with timestamp. The web page is updated each time new data arrives in the queue. When previously stored data is updated, an alert is displayed on the web interface.

- **Container C**: Contains the RabbitMQ message queue system.

# Prerequisites

- Docker and Docker Compose must be installed.
- Clone this project using your GitHub or GitLab account.

# Installation and Execution

1. Open a Terminal or Command Prompt.
2. Navigate to the project directory: cd turkai_python_task
3. Start using Docker Compose: docker-compose up 
4. Access the web server by going to `http://172.21.0.4:5000/` in your web browser.
5. When finished, stop the application: docker-compose down

# Learn More

For more details and contribution instructions, visit the GitHub page: [Our Project on GitHub](https://github.com/aslcerenhzr/turkai_python_task)


