# Django Application Containerization & Deployments on AWS EC2

This project demonstrates how a **legacy Django application** is containerized using **Docker**, published to **Docker Hub**, and deployed on an **AWS EC2 instance** to make it accessible from anywhere via a public IP.

---

## 📌 Project Overview

- **Framework**: Django 1.11.17
- **Language**: Python 3.7
- **Forms**: django-crispy-forms 1.7.2
- **Database**: SQLite
- **Containerization**: Docker
- **Image Registry**: Docker Hub
- **Cloud Platform**: AWS EC2 (Ubuntu)
- **Access**: Public IP

---

## ⚙️ Technology Stack

| Component | Used |
|--------|------|
| Python | 3.7 |
| Django | 1.11.17 |
| Docker | Yes |
| Docker Hub | Public Repository |

| AWS EC2 | Ubuntu Instance |
| Database | SQLite |

---

## 📂 Application Structure


project-root/
├── manage.py
├── requirements.txt
├── Dockerfile
├── db.sqlite3
├── app/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ └── templates/
└── project/
└── settings.py

---

##  Requirements

txt
Django==1.11.17
django-crispy-forms==1.7.2

#Dockerfile
FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]


#DOCKER HUB repo
sain143/sai-repo1:latest

#how to run the image

docker build -t nandu-image .

docker tag nandu-image:latest sain143/sai-repo1:latest

docker push sain143/sai-repo1:latest


# Deployment on AWS EC2
EC2 Details

OS: Ubuntu

Docker installed and enabled

Security Group allows inbound traffic on port 8081

#Running the Application on EC2
Pull Image
docker pull sain143/sai-repo1:latest

#Run Container
docker run -d \
  --restart unless-stopped \
  -p 8081:8080 \
  --name sai-app \
  sain143/sai-repo1:latest

#Accessing the Application
http://<EC2-PUBLIC-IP>:8081

#Django Production Fix

To avoid DisallowedHost error, the following change was made:

ALLOWED_HOSTS = ['*']

📌 Key Learnings

Docker ensures environment consistency

Docker Hub allows easy image sharing

EC2 provides public access via IP

Django requires ALLOWED_HOSTS configuration in production

Containers must be running for the app to be accessible

Restart policies help keep containers alive after reboot

📈 Current Limitations

Single EC2 instance

Django development server (runserver)

SQLite database

Limited concurrent users




🔮 Future Improvements

Replace runserver with Gunicorn + Nginx

Use Elastic IP for static public IP

Move image to AWS ECR

Deploy using Kubernetes (EKS)

Add CI/CD using Jenkins or GitHub Actions




✅ Conclusion

This project successfully demonstrates a real-world DevOps workflow:

Legacy Django app

Dockerized

Published to Docker Hub

Deployed on AWS EC2

Accessible globally via public IP

👤 Author

Sai



