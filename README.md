# tanX.fi Assessment for Infrastructure Engineer

## Overview

- This project analyzes customer orders using a Python and as an added feature also makes a very basic webpage using Flask hosted on AWS EC2 to view the results and incorporate AWS. 
- Dockerized with Docker Compose. 
- It includes a test service to validate the functionality of the analysis.

## Table of Contents

1. [Introduction](#introduction)
2. [Files](#files)
3. [Setup and Installation](#setup-and-installation)
4. [Build and Run the Application](#build-and-run-the-application)
5. [Running Tests](#running-tests)
6. [Deploying to AWS](#deploying-to-aws)
7. [Screenshots](#screenshots)
8. [Troubleshooting](#troubleshooting)
9. [Contributing](#contributing)


## Introduction

This project provides a web service that analyzes customer order data. The analysis includes revenue per month, revenue per product, revenue per customer, and the top 10 customers. The application is Dockerized and uses Flask for the web service.

## Files

- `analyze.py`: Contains the Flask app to analyze orders and return results.
- `tester.py`: Contains unit tests for the `AnalyzeOrders` class.
- `Dockerfile`: Defines the Docker image for the Flask app.
- `docker-compose.yml`: Defines two Docker services: `app` for the Flask app and `test` for running tests.
- `requirements.txt`: Lists the Python dependencies.
- `orders.csv`: Sample CSV file with order data.

## Setup and Installation

### Prerequisites

1. **Docker**: Ensure Docker is installed on your system. If not, follow the [official Docker installation guide](https://docs.docker.com/get-docker/).
2. **Docker Compose**: Ensure Docker Compose is installed. Follow the [official Docker Compose installation guide](https://docs.docker.com/compose/install/).

### Clone the Repository

```
git clone https://github.com/db2003/tanx.fi-exp.git
```

### Build and Run the Application

1. **Build the Docker images and start the services:**

   ```
   docker-compose up --build
   ```

   This command will build the Docker images for both the `analyze` and `tester` services and start them.

2. **Access the web application:**

   Open a browser and go to `http://localhost:4000/results` to see the analysis results and to see the test status go to `http://localhost:4000/test_status`.

### Running Tests

1. **Run the tests using Docker Compose:**

   ```
   docker-compose run test
   ```

   This command will execute the tests defined in `tester.py`.

## Deploying to AWS

Integration with AWS EC2 to test and verify its easy application with AWS hosting.

### Create an EC2 Instance

1. **Log in to the AWS Management Console** and navigate to EC2.
2. **Launch a new EC2 instance** with Amazon Linux 2 AMI and select the instance type.
3. **Configure security group rules** to allow inbound traffic on port 4000 (for the web service) and port 22 (for SSH access).

### Connect to the EC2 Instance

1. **Use PuTTY to connect:**
   - Open PuTTY and load your private key.
   - Make sure to get a pem key and convert it to ppk key for further use.
   - Connect to your EC2 instance using the Public DNS and port 22.

2. **Install Docker and Docker Compose:**
   - Install Docker and Docker Compose in our EC2 machine to replicate the localhost docker on AWS.
     
  
   ```
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

   ```
   cd /path/to/your/project
   ```

2. **Build and run the Docker services:**

   ```
   docker-compose up --build
   ```

   Your application will be available at `http://<YOUR_PUBLIC_IP>:4000/results`, the test status will be available at `http://<YOUR_PUBLIC_IP>:4000/test_status`
   

## Screenshots
### Web Application Results

1. FileZilla Preview for EC2 instance:
   
![WhatsApp Image 2024-07-29 at 02 30 05_201bfbc7](https://github.com/user-attachments/assets/51031089-759f-42ab-b689-2a1830dc132a)

2. puTTy Connection showcase for EC2 instance:
   
![WhatsApp Image 2024-07-29 at 02 31 48_feac4812](https://github.com/user-attachments/assets/3217afcd-b30a-4533-8480-e2a72d86f373)


### Test Results

| Hosted Links | Screenshots |
| ------------ | ----------- |
| [Test Status](http://ec2-34-239-136-30.compute-1.amazonaws.com:4000/test_status) | ![Screenshot 1](https://github.com/user-attachments/assets/d2304620-31a7-4d5a-af8e-7de3fd6cab23) |
| [Analysis Result](http://ec2-34-239-136-30.compute-1.amazonaws.com:4000/results) | ![Screenshot 2](https://github.com/user-attachments/assets/16938a4e-a061-49e4-ba19-0b22b7a215aa) |




## Troubleshooting

### Common Issues

- **Connection Refused/Error**: Ensure that the security group allows traffic on port 4000 and that the Docker services are running.

- **Internal Server Error**: Check the application logs for errors and ensure that the `orders.csv` file is correctly loaded and accessible.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.


