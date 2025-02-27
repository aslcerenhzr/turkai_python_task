TURK AI ARTIFICIAL INTELLIGENCE INFORMATION AND SOFTWARE SYSTEMS INC.
Python Developer Task: Interpol Data Flow and Web Server

I completed this project during my internship at TURK AI. In this project, I developed a system to fetch, queue, store, and display Interpol's wanted persons data via a web server. I started by conducting a requirement analysis and creating a UML diagram. Using Selenium, I extracted the data and saved it in a .txt file. I designed a database and table structure in PostgreSQL and integrated RabbitMQ for message queuing. Leveraging Flask, I built a web interface to present the retrieved data, designing the frontend with HTML and CSS. Finally, I containerized the project using Docker, ensuring compatibility with a microservices architecture, and managed version control through GitHub.

# Installation and Execution

1. Open a Terminal or Command Prompt.
2. Navigate to the project directory: cd turkai_python_task
3. Start using Docker Compose: docker-compose up 
4. Access the web server by going to `http://172.21.0.4:5000/` in your web browser.
5. When finished, stop the application: docker-compose down
