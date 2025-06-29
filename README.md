# 🧩 Lambda API Gateway and Monitoring

This project demonstrates how to build a fully serverless API architecture using **AWS Lambda**, **API Gateway**, and **CloudWatch Monitoring**, with additional features like **CORS**, **Canary Deployments**, and **JWT-based Lambda Authorizer**.

---

## **ALL THE STEP BY STEP GUIDE TO CREATE THE PROJECT IN THIS REPO IS AVAILABLE AND CAN BE READ INSIDE THE Docs/PDF FILE**

## 📌 Table of Contents

- [Architecture](#architecture)
- [Features](#features)
- [Getting Started](#getting-started)
- [Deployment Steps](#deployment-steps)
- [Monitoring](#monitoring)
- [Security (Lambda Authorizer)](#security-lambda-authorizer)
- [Tools Used](#tools-used)
- [What I Learned](#what-i-learned)
- [Next Steps](#next-steps)

---

## 🏗️ Architecture

A simple RESTful serverless API with two versions (v1 and v2) using AWS services:
Client → API Gateway → Lambda Functions → (CloudWatch, JWT Auth)

---

## ✨ Features

- 🖥️ Lambda Function with Python runtime
- 🌐 REST API Gateway integration
- 🔁 Canary Deployment for version control
- 🌍 CORS support for cross-origin requests
- 🛡️ JWT-based Lambda Authorizer
- 📈 CloudWatch log monitoring
- 📤 Tested with Postman and curl

---

## 🚀 Getting Started

### Prerequisites

- AWS Account
- IAM permissions for Lambda, API Gateway, CloudWatch
- Tools such as Postman or Insomnia or use curl for API testing
- Python 3 and pip

---

## Project Diagram

_![API Gateway Lambda Integration](img/Integrate-APIGW-Lambda.png)_

_![Lambda Authorization Diagram](img/lambda-authorization-diagram.png)_

---

## ⚙️ Deployment Steps

### 1. Create Lambda Function

- Runtime: Python
- Function name: `dausFunction1`
- Test with Hello World event

### 2. Connect to API Gateway

- Create REST API (Regional)
- Create resource `/helloworld`
- Create `GET` method → integrate with Lambda

### 3. Deploy API

- Stage name: `PROD`
- Copy Invoke URL and test via Postman

### 4. Create Canary Deployment

- Create new function: `dausFunction2`
- Update message: `"Greetings from Firdaus!"`
- Split traffic 50/50 in Canary Settings
- Create `/v2/helloworld` resource and method
- Deploy and test new version

### 5. Enable CORS

- Enable OPTIONS method on `/v2/helloworld`
- Add custom response and mapping template
- Deploy and promote Canary

---

## 🕵️ Monitoring

- Use **CloudWatch** to view Lambda logs
- Navigate to Lambda → Monitoring → View Logs in CloudWatch

---

## 🔐 Security (Lambda Authorizer)

1. Generate JWT secret using OpenSSL
2. Create Lambda Authorizer function
3. Use `PyJWT` to decode JWT tokens
4. Add permissions so API Gateway can invoke Lambda
5. Connect Authorizer to `/v2/helloworld` method
6. Test using JWT from [jwt.io](https://jwt.io)

---

## 🛠️ Tools Used

- AWS Lambda
- API Gateway (REST)
- CloudWatch
- Python (runtime & authorizer)
- Postman
- PyJWT
- JWT.io

---

## 📚 What I Learned

- Full AWS serverless API deployment
- Canary deployment with live traffic shifting
- CORS handling using OPTIONS method
- JWT token creation and validation via Lambda
- Using CloudWatch for real-time debugging

---

## 🔮 Next Steps

- Integrate with DynamoDB
- Add frontend client interface
- Implement rate-limiting and API keys
- Build reusable Terraform template

---

## 📸 Screenshots

_![Hello world message from the lambda](img/helloworld1.png)_

_![Hello world message from the lambda with your name](img/helloworld2.png)_

_![CORS testing successful reply](img/CORS.png)_

_![CORS testing successful reply from the CMD](img/CORS2.png)_

_![Lambda Authorizer testing successful reply from the AWS Console](img/authorizer.png)_

_![Lambda Authorizer testing successful reply from the VSCode Terminal](img/authorizer2.png)_

---

## Summary

✅ PART 1: Creating the Lambda and Monitoring the Function Logs
AWS Lambda was used as the core backend function written in Python.

A function named dausFunction1 was created from scratch to return a simple message.

The Lambda function was tested using a "Hello World" test event, and its execution logs were monitored through CloudWatch, which is automatically integrated with Lambda.

📌 Summary: Lambda acted as the main compute resource and was paired with CloudWatch for observability.

✅ PART 2: Connecting Lambda with the API Gateway
The Lambda function (dausFunction1) was connected to API Gateway using a GET method.

API Gateway served as the public HTTP endpoint, while Lambda handled the business logic and returned responses.

📌 Summary: Lambda function acted as the backend handler for a REST API.

✅ PART 3: Implementing API Canary
A second Lambda function (dausFunction2) was created with a different message: "Greetings from Firdaus!".

Canary deployment was configured on API Gateway to split traffic 50/50 between dausFunction1 and dausFunction2.

This allowed gradual testing of the new version before fully promoting it to production.

📌 Summary: Lambda was used in a versioned deployment setup with controlled traffic rollout.

✅ PART 4: Enabling CORS
Lambda remained the backend processor, but API Gateway was configured with an OPTIONS method to handle CORS preflight requests.

This made it possible for front-end clients from different origins to access the Lambda-powered API securely.

📌 Summary: Lambda worked with API Gateway to support cross-origin resource sharing.

✅ PART 5: Controlling Access Using Lambda Authorizer
A new Lambda function was created as a custom Lambda Authorizer to validate JWT tokens before allowing access to protected API endpoints.

The authorizer parsed and verified tokens using the PyJWT library.

It acted as a security layer, verifying authentication before forwarding the request to the actual Lambda function.

📌 Summary: Lambda was used to implement authentication and access control with JWT.

🔚 Overall Summary:
In this project, AWS Lambda was used to:

Handle serverless API logic (Part 1–2)

Manage version control with canary deployment (Part 3)

Support frontend access via CORS (Part 4)

Implement secure access using JWT-based Lambda Authorizer (Part 5)

---

## 👨‍💻 Author

**Muhamad Firdaus**

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
