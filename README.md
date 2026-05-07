# CI/CD Pipeline: Deploy a Containerized Web App to AWS EC2

---

## 📌 Project Overview

This project demonstrates an **end‑to‑end DevOps pipeline** that automatically deploys a Python Flask web application to an AWS EC2 instance. Every time code is pushed to the `main` branch, GitHub Actions:

- Builds a Docker image of the app
- Pushes the image to Docker Hub
- Provisions an EC2 instance and a security group using **Terraform**
- Deploys the container and makes the app publicly accessible

The entire infrastructure is defined as code, and the deployment is fully automated – essential skills for a Cloud DevOps Engineer.

---

## 🛠️ Technologies & Tools

| Category       | Tools                                                                 |
|----------------|-----------------------------------------------------------------------|
| **Cloud**      | AWS (EC2, Security Groups, IAM, Free Tier)                            |
| **IaC**        | Terraform                                                             |
| **Container**  | Docker, Docker Hub                                                    |
| **CI/CD**      | GitHub Actions                                                        |
| **Language**   | Python 3.9 + Flask                                                    |
| **Version Ctrl**| Git                                                                  |

---

## 🏗️ Architecture Diagram

```text
[Git Push] → [GitHub Actions] → [Docker Build & Push] → [Docker Hub]
                    ↓
            [Terraform Apply]
                    ↓
    [AWS EC2 Instance + Security Group]
                    ↓
         [Container runs on port 80]
                    ↓
            [Public IP → Browser]
```

<img width="1907" height="568" alt="Screenshot 2026-05-07 150109" src="https://github.com/user-attachments/assets/1bc316c8-dff3-415b-9a80-3acb96881268" />


---

## 🚀 Live Demo

- The app was successfully deployed to AWS EC2 using Terraform and GitHub Actions.  
*(Instance terminated to avoid charges – can be redeployed anytime)*

## 🧪 How to Redeploy

- 1. Clone the repo
- 2. Add your secrets (Docker Hub token, AWS keys)
- 3. Push to `main` – the pipeline will deploy automatically
 
---

# 🚀 PowerShell Command to Run & Deploy 
1.
```
cd C:\devops-project
```
2.
```
echo "" >> README.md
git add README.md
git commit -m "trigger new deployment"
git push
```

---

# 🐳 Test the Docker container locally (without deploying to AWS)

```
cd C:\devops-project
docker build -t my-first-container .
docker run -p 5000:5000 my-first-container
```
---

# 🏗️ Run Terraform locally (to preview or apply infrastructure)

```
cd C:\devops-project\terraform
terraform init
terraform plan
terraform apply -auto-approve
```
To destroy everything:
```
terraform destroy -auto-approve
```



