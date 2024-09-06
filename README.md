# Small Customer data analysis and testing project 

## Overview

This project analyzes customer orders using Python and provides a web interface using Flask, hosted on AWS EC2. It includes:

- **Data Analysis:** Metrics like revenue per month, revenue per product, and top customers are calculated from the data.
- **Web Interface:** A simple web app built with Flask allows users to view the analysis results.
- **Containerization:** The application is Dockerized, using Docker Compose to manage both the app and testing services.
- **Testing:** A test suite validates the analysis functionality using pytest.
- **Cloud Deployment:** The app is deployed on an AWS EC2 instance, demonstrating the integration of cloud services.

## Table of Contents

1. [Introduction](#introduction)
2. [Tech Stack](#tech-stack)
3. [Video Showcase](#video-showcase)
4. [Architecture and Project Structure](#architecture-and-project-structure)
5. [Setup and Installation](#setup-and-installation)
6. [Build and Run the Application](#build-and-run-the-application)
7. [Running Tests](#running-tests)
8. [Deploying to AWS](#deploying-to-aws)
9. [Screenshots](#screenshots)
10. [Troubleshooting](#troubleshooting)
11. [Contributing](#contributing)

## Introduction

This project provides a web service that analyzes customer order data. The analysis includes revenue per month, revenue per product, revenue per customer, and the top 10 customers. The application is Dockerized and uses Flask for the web service. (CI-CD pipeline in progress)

## Tech Stack

| Technology       | Purpose                                   |
|------------------|-------------------------------------------|
| **Python**       | Programming language                      |
| **Flask**        | Web framework                             |
| **Docker**       | Containerization                          |
| **Docker Compose** | Multi-container setup management         |
| **AWS EC2**      | Hosting and deployment                    |
| **PuTTY**        | SSH client for EC2 access                 |
| **FileZilla**    | File transfer to EC2 instance             |

## Video Showcase
### [click here to watch](https://drive.google.com/file/d/1zjkoLSwbLcKg4fDkgh8GjCeOxdKPNZ1L/view?usp=sharing)

## Architecture and Project Structure

The project is structured to separate concerns and streamline the deployment process. Below is an overview of the architecture and a detailed description of each component.

### Architecture

1. **Data Analysis**: The core functionality of the project involves analyzing customer order data. This is handled by the `AnalyzeOrders` class in the `analyze.py` file, which processes a CSV file and computes various metrics.

2. **Web Interface**: The web interface is built using Flask, a lightweight Python web framework. It provides endpoints for users to view the analysis results and test statuses. The Flask app is defined in `analyze.py`.

3. **Containerization**: The entire application, including the Flask app and the testing environment, is containerized using Docker. Docker Compose is used to manage multi-container applications, ensuring that both the application and testing services can be run simultaneously.

4. **Testing**: Unit tests are written in `tester.py` to validate the data analysis logic. These tests are automatically run in a separate Docker container.

5. **Cloud Deployment**: The application is designed to be easily deployable on AWS EC2. The Docker containers can be set up and managed on an EC2 instance, providing a scalable and easily accessible solution.

### Project Structure

- **analyze.py**: This file contains the core functionality for data analysis and the Flask web application.
  - **AnalyzeOrders Class**: This class is responsible for reading and analyzing the `orders.csv` file. It calculates metrics such as total revenue per month, revenue per product, and top customers.
  - **Flask Routes**: Defines routes for accessing analysis results (`/results`) and the test status (`/test_status`).

- **tester.py**: Contains unit tests for the `AnalyzeOrders` class.
  - **Test Cases**: Verifies the correctness of the data analysis methods, ensuring they produce accurate results given a set of input data.

- **Dockerfile**: Describes the environment setup for the Flask app.
  - **Base Image**: Specifies the base image to use (e.g., `python:3.12-slim`).
  - **Dependencies**: Installs necessary Python packages from `requirements.txt`.
  - **App Setup**: Copies the application code and sets up the environment to run the Flask app.

- **docker-compose.yml**: Defines the multi-container setup for the project.
  - **Services**: 
    - **app**: The main service that runs the Flask application.
    - **test**: A separate service for running unit tests using pytest.
  - **Network and Volumes**: Configures networks and shared volumes between containers.

- **requirements.txt**: Lists all Python dependencies required for the project, such as Flask, pandas, and pytest.

- **orders.csv**: A sample CSV file containing customer order data, used for analysis.


## Setup and Installation

### Prerequisites

1. **Docker**: Ensure Docker is installed on your system. If not, follow the [official Docker installation guide](https://docs.docker.com/get-docker/).
2. **Docker Compose**: Ensure Docker Compose is installed. Follow the [official Docker Compose installation guide](https://docs.docker.com/compose/install/).

### Clone the Repository

```sh
git clone https://github.com/db2003/tanx.fi-exp.git
```

## Build and Run the Application

1. **Build the Docker images and start the services:**

   ```sh
   docker-compose up --build
   ```

   This command will build the Docker images for both the `app` and `test` services and start them.

2. **Access the web application:**

   Open a browser and go to `http://localhost:4000/results` to see the analysis results and to `http://localhost:4000/test_status` to see the test status.

## Running Tests

1. **Run the tests using Docker Compose:**

   ```sh
   docker-compose run test
   ```

   This command will execute the tests defined in `tester.py`.

## Deploying to AWS

### Create an EC2 Instance

1. **Log in to the AWS Management Console** and navigate to EC2.
2. **Launch a new EC2 instance** with Amazon Linux 2 AMI and select the instance type.
3. **Configure security group rules** to allow inbound traffic on port 4000 (for the web service) and port 22 (for SSH access).

### Connect to the EC2 Instance

1. **Use PuTTY to connect:**
   - Open PuTTY and load your private key.
   - Ensure you have a pem key and convert it to a ppk key for further use.
   - Connect to your EC2 instance using the Public DNS and port 22.

2. **Install Docker and Docker Compose:**
   - Install Docker and Docker Compose on the EC2 machine to replicate the local Docker environment on AWS.

   ```sh
   sudo yum update -y
   sudo yum install -y docker
   sudo service docker start
   sudo usermod -a -G docker ec2-user

   # Install Docker Compose
   sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### Upload Files to EC2

1. **Use FileZilla to upload the files** to your EC2 instance.

### Start Docker Services

1. **Navigate to the project directory** on your EC2 instance.

   ```sh
   cd /path/to/your/project
   ```

2. **Build and run the Docker services:**

   ```sh
   docker-compose up --build
   ```

   Your application will be available at `http://<YOUR_PUBLIC_IP>:4000/results`, and the test status will be available at `http://<YOUR_PUBLIC_IP>:4000/test_status`.

## Screenshots

### Web Application Results

1. FileZilla Preview for EC2 instance:

<img src="https://github.com/user-attachments/assets/51031089-759f-42ab-b689-2a1830dc132a" width="500">

2. puTTY Connection Showcase for EC2 instance:

<img src="https://github.com/user-attachments/assets/3217afcd-b30a-4533-8480-e2a72d86f373" width="600">



### Test Results

Feel free to click on the links to check my result and test status page hosted on AWS EC2 by me.

| Hosted Links | Screenshots |
| ------------ | ----------- |
| [Test Status](http://ec2-34-239-136-30.compute-1.amazonaws.com:4000/test_status) | <img src="https://github.com/user-attachments/assets/d2304620-31a7-4d5a-af8e-7de3fd6cab23" width="400"> |
| [Analysis Result](http://ec2-34-239-136-30.compute-1.amazonaws.com:4000/results) | <img src="https://github.com/user-attachments/assets/16938a4e-a061-49e4-ba19-0b22b7a215aa" width="500"> |

## Troubleshooting

### Common Issues

- **Connection Refused/Error:** Ensure that the security group allows traffic on port 4000 and that the Docker services are running.
- **Internal Server Error:** Check the application logs for errors and ensure that the `orders.csv` file is correctly loaded and accessible.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

