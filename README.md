# 🔐 Zero Trust Architecture Demo (AWS)

## 🚀 Overview
This project demonstrates the implementation of a Zero Trust security model using AWS services, enforcing strict identity-based access control for all API requests.

## 🧠 Concept: Zero Trust
"Never trust, always verify" — Every request must be authenticated and authorized before accessing backend resources.

---

## 🏗️ Architecture

User → API Gateway (IAM Auth) → Lambda → S3 (Private)

- API Gateway enforces IAM authentication
- Lambda executes only for authorized requests
- S3 bucket is private (no public access)

---

## 🛠️ Tech Stack
- AWS API Gateway (HTTP API)
- AWS Lambda
- Amazon S3
- IAM (Identity-based access control)
- Postman (for testing AWS Signature requests)

---

## 🔐 Security Implementation

- IAM-based authentication enabled on API Gateway
- Only signed AWS requests are allowed
- Unauthorized access is blocked (HTTP 403)
- Lambda uses least privilege role to access S3
- No public exposure of backend services

---

## 🧪 Testing Scenarios

### ❌ Without Authentication
Response:{"message":"Forbidden"}


### ❌ Invalid Credentials
Response: {"message":"Forbidden"}


### ✅ With Valid IAM Authentication
Response:✅ Access granted (Authorized)


---

## 📷 Screenshots

- Authorized request (Postman with AWS Signature)
- Unauthorized request (blocked)

---

## 🎯 Key Learnings

- Implementing Zero Trust in serverless architecture
- Securing APIs using IAM authentication
- Understanding request signing (AWS Signature v4)
- Enforcing least privilege access

---

## 💼 Real-World Relevance

This architecture is similar to enterprise-grade secure API systems where:
- No public endpoints are exposed
- Every request must be authenticated
- Backend services are isolated and protected

---

## 🔗 Related Project

Cloud Security Audit Dashboard (Monitoring + Detection System)
