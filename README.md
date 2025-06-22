
# STREAM: Secure Theatrical Retrieval Endpoint API Management

A secure, scalable microservices-based web application for retrieving movie data. STREAM uses modern DevOps tools and service orchestration technologies including **Kubernetes**, **Docker**, **Flask**, **MySQL**, **Kong API Gateway**, **Prometheus** and **Grafana** to build a robust, observable, and secure API ecosystem.

---

## Features

- Microservices architecture with Flask and MySQL
- API gateway security via Kong with key-based role-based access control
- Kubernetes for container orchestration and service scaling
- Monitoring and alerting using Prometheus and Grafana
- RESTful API design for clean and efficient communication between services
- Fully containerized using Docker for portability and ease of deployment

---

## Tech Stack

| Category           | Tools & Frameworks                      |
|--------------------|-----------------------------------------|
| Backend            | Flask, Python                           |
| Database           | MySQL                                   |
| Containerization   | Docker                                  |
| Orchestration      | Kubernetes                              |
| API Management     | Kong API Gateway                        |
| Monitoring         | Prometheus, Grafana                     |
| Security           | Key authentication                      |

---

## Project Structure

```bash
.
├── services/
│   ├── movie-service/          # Flask app for movie retrieval
│   └── user-auth-service/      # (Optional) authentication microservice
├── kong/                       # Kong API Gateway configuration
├── k8s/                        # Kubernetes manifests
├── monitoring/                 # Prometheus and Grafana configs
├── docker-compose.yml          # For local multi-container setup
└── README.md
````

---

## Setup Instructions

### Prerequisites

* Docker
* Kubernetes (Minikube or any K8s cluster)
* Helm (optional, for Prometheus & Grafana)

## Security

* Kong API Gateway with key-based authentication
* Role-Based Access Control (RBAC) to manage access to API endpoints
* Secure communication and authentication headers

---

## Monitoring Dashboard

* Prometheus: Collects real-time metrics from services
* Grafana: Visualizes service health and usage trends
* Alerts configured for service downtime or abnormal behavior

## Skills Demonstrated

* Cloud-native development with Kubernetes and Docker
* API Management and observability with Kong, Prometheus, and Grafana
* RESTful service design and secure deployment patterns
* Scalable backend architecture using microservices
