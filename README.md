# NOTES API

Welcome to Note API, a simple CRUD project showcasing the development of a web API using a modern tech stack:

- FastAPI: A high-performance web framework for building APIs with Python, known for its speed, simplicity, and intuitive design.
- Docker and Docker Compose: Tools for containerization, enabling seamless deployment and scalability of applications across different environments.
- PostgreSQL: A powerful open-source relational database management system, chosen here for its reliability, performance, and robust feature set.
- Pytest: A flexible and easy-to-use testing framework for Python, essential for ensuring the correctness and stability of our application through automated tests.


# Local Setup Guide

A Step by Step to reproducing the Modern Python API codebase, but first make sure that you have docker and docker compose set and running.

1. Clone the repository:
```git clone https://github.com/tandavala/morden-python-api.git```

2. Navigate to the Project Directory:
```cd morden-python-api```

3. Build and Start Docker Containers:
```docker-compose up -d --build```

4. Run Tests:
```docker-compose exec web pytest .```

***NOTE***: You're encouraged to delve into the codebase, tweak functionalities, and experiment with the API's features. This project adheres to standard conventions for a FastAPI application, utilizing Docker and Docker Compose for containerization and PostgreSQL as the database backend.

Now that the application is up and running, you can further explore its capabilities through the provided link below:

API Documentation

Happy exploring!


