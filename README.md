# AWS Serverless Quiz Application

## Project Overview

This project demonstrates a simple **serverless quiz application deployed using AWS services**.
The frontend is hosted on an EC2 instance running Nginx, while the backend uses API Gateway, AWS Lambda, and DynamoDB to process and store quiz results.

This project was built as part of a **Cloud & DevOps learning exercise**.

---

## Architecture

User → EC2 (Frontend) → API Gateway → Lambda → DynamoDB

---

## AWS Services Used

### EC2

Hosts the quiz frontend application using **RHEL 9 and Nginx**.

### API Gateway

Provides a REST API endpoint that allows the frontend to send quiz results to the backend.

### AWS Lambda

Processes quiz submissions and writes the data into DynamoDB.

### DynamoDB

Stores user quiz results including:

* Name
* Email
* Phone
* Score
* Attempted Questions
* Timestamp

---

## Application Workflow

1. User accesses the quiz webpage hosted on EC2.
2. User enters personal details and answers quiz questions.
3. The frontend calculates the score.
4. A POST request is sent to API Gateway.
5. API Gateway triggers a Lambda function.
6. Lambda stores the quiz result in DynamoDB.

---

## Example Data Stored in DynamoDB

```
email: user@example.com
name: Test User
phone: 9999999999
score: 8
attempted: 10
timestamp: 2026-03-11
```

---

## Technologies Used

* AWS EC2
* AWS API Gateway
* AWS Lambda
* AWS DynamoDB
* HTML / JavaScript
* Nginx
* RHEL Linux

---


## Future Improvements

* Add authentication using AWS Cognito
* Deploy frontend using S3 + CloudFront
* Implement CI/CD using GitHub Actions
* Containerize application using Docker

