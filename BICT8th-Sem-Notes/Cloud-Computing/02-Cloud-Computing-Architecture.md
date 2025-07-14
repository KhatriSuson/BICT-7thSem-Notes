# ☁️ Unit 2: Cloud Computing Architecture

## ✅ Unit Objectives

- Understand and differentiate the **three main cloud service models**: IaaS, PaaS, SaaS.
- Explain the **four types of cloud deployment models**.
- Describe the concept of **virtualization** and its role in cloud computing.
- Gain practical experience using **cloud services**.

---

## 2.1 Cloud Service Models

Cloud services are delivered in **three key models**, each offering different levels of control and abstraction:

### 🧱 2.1.1 Infrastructure as a Service (IaaS)

- Provides **virtualized computing resources** over the internet.
- Includes servers, storage, networking, and operating systems.
- User manages everything above the virtualization layer.

🔧 **Examples:**
- Amazon EC2
- Google Compute Engine (GCE)
- Microsoft Azure Virtual Machines

📝 *Use case:* Hosting a custom website or application where you manage your OS, runtime, and app.

---

### 🧰 2.1.2 Platform as a Service (PaaS)

- Provides **development and deployment platforms**.
- Developers can focus on building applications without managing infrastructure.
- Includes OS, runtime, and middleware.

🔧 **Examples:**
- AWS Elastic Beanstalk
- Azure App Service
- Google App Engine

📝 *Use case:* Deploying a Python Flask app without worrying about OS-level setup.

---

### 💼 2.1.3 Software as a Service (SaaS)

- Delivers **fully functional software** over the internet.
- Users simply log in and use the software.
- Everything is managed by the service provider.

🔧 **Examples:**
- Google Workspace (Docs, Drive, Gmail)
- Microsoft 365 (Word, Excel, Teams)
- Salesforce (CRM)

📝 *Use case:* Collaborating on a shared Google Doc in real time.

---

## 2.2 Deployment Models

Deployment refers to **how the cloud services are made available** to users.

### 🌐 2.2.1 Public Cloud

- Services offered to the general public over the internet.
- Managed by third-party providers.

📝 *Example:* Google Cloud Platform, Microsoft Azure

---

### 🏢 Private Cloud

- Used exclusively by a single organization.
- Offers greater **control, security, and customization**.

📝 *Example:* Government data center cloud

---

### 🔀 Hybrid Cloud

- Combines **public and private** clouds.
- Data and apps can move between them.

📝 *Example:* Banking apps storing sensitive data privately, but using public cloud for frontend services.

---

### 👥 Community Cloud

- Shared by multiple organizations with **common concerns** (e.g., security, compliance).
- Often managed by a third-party or consortium.

📝 *Example:* Multiple hospitals sharing a cloud to store health records under common regulations.

---

## 2.3 🖥️ Virtualization and its Role in Cloud Computing

- **Virtualization** allows multiple virtual machines (VMs) to run on a single physical machine.
- Enables **resource pooling**, **cost-efficiency**, and **isolation** in the cloud.
- Hypervisors like **VMware, KVM, Hyper-V** manage VMs.

📝 *Example:* One physical server can run multiple Linux and Windows VMs using a hypervisor — each acting like a separate computer.

---

## 🛠️ Practical Works

### 1️⃣ PaaS Deployment Task
- Use a platform like:
  - 🟢 AWS Elastic Beanstalk
  - 🔵 Azure App Service
  - 🔴 Google App Engine

📌 *Objective:* Deploy a basic
