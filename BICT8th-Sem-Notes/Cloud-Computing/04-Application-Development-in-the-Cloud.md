## Unit 4: Application Development in the Cloud

### ✅ Specific Objectives
- Develop cloud-native applications.
- Explain containers and automate container deployment using Kubernetes.

---

### 🧠 4.1 Basics of Cloud-Native Development

**Cloud-native development** refers to building applications specifically for cloud environments that are:
- **Scalable**
- **Resilient**
- **Agile**
- **Observable**

#### 🌐 Key Principles:
- **Microservices Architecture**: Breaks down applications into small, independent services that communicate over APIs (e.g., REST or gRPC).
- **Containers**: Isolated environments for running applications consistently across platforms.
- **CI/CD Pipelines**: Automate testing and deployment.
- **DevOps Culture**: Bridges the gap between development and operations teams.

#### 🔍 Real-World Example:
Netflix uses microservices and cloud-native principles to manage thousands of services independently, ensuring fault-tolerance and high availability.

---

### ⚙️ 4.2 Introduction to Containers and Kubernetes

#### 🐳 Containers:
- A lightweight, portable unit of software packaging application code and dependencies.
- **Popular tools**: Docker
- **Benefits**:
  - Isolation
  - Portability
  - Fast boot time

#### ☸️ Kubernetes (K8s):
- An open-source container orchestration platform that automates deployment, scaling, and management of containerized applications.

#### 🌐 Core Concepts of Kubernetes:
- **Pod**: Smallest deployable unit (1 or more containers)
- **Service**: Exposes pods to external/internal network
- **Deployment**: Manages replica sets and rolling updates
- **Ingress**: Manages external access to services (e.g., via domain names)

#### 🧑‍💻 Tools for Local Setup:
- [Minikube](https://minikube.sigs.k8s.io/docs/) – for running K8s locally
- [K3s](https://k3s.io/) – lightweight K8s distribution

---

### 🛠️ Practical Works

#### 1. Develop a Simple Cloud-Native Application:
- Create a **microservices** app with:
  - `User Service` (handles user authentication)
  - `Product Service` (displays products)
- Use **REST APIs** or **gRPC** for service-to-service communication.
- Deploy to:
  - AWS (e.g., ECS, EKS)
  - Azure (e.g., Azure Kubernetes Service)
  - GCP (e.g., Google Kubernetes Engine)

##### ✅ Demonstrate:
- **Scalability**: Auto-scale services based on load
- **Resilience**: Use health checks and failovers

#### 2. Kubernetes Deployment:
- Install **Minikube** on local machine
- Build Docker images for `frontend` and `backend` services
- Create K8s `Deployment` and `Service` YAML files
- Expose services using `LoadBalancer` or `NodePort`

##### Example Deployment Command:
```bash
kubectl apply -f user-service-deployment.yaml
kubectl apply -f product-service-deployment.yaml
kubectl get services
