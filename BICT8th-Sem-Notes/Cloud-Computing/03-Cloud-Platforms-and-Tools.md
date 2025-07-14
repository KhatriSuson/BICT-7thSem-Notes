# ☁️ Unit 3: Cloud Platforms and Tools

## ✅ Unit Objectives

- Understand the core services and ecosystems of **AWS**, **Microsoft Azure**, and **Google Cloud Platform (GCP)**.
- Explore essential **cloud tools**: compute, storage, and database services.
- Gain practical experience with **account creation, storage setup**, and **SQL queries** using cloud platforms.

---

## 3.1 🌐 Introduction to Major Cloud Platforms

### 🔶 Amazon Web Services (AWS)
- Market leader in cloud services.
- Highly flexible, scalable, and vast service offerings.
- Free-tier available for 12 months (e.g., EC2, S3, Lambda, RDS).

📝 *Example:* Use AWS S3 to host static websites or backup files.

---

### 🔷 Microsoft Azure
- Best suited for businesses already using Windows-based infrastructure.
- Strong integration with **Active Directory**, **Office 365**, and hybrid environments.

📝 *Example:* Use Azure App Service to deploy .NET applications.

---

### 🔴 Google Cloud Platform (GCP)
- Known for **big data**, **machine learning**, and **AI services**.
- Offers serverless options and fast global networking.

📝 *Example:* Use BigQuery for large-scale data analytics.

---

## 3.2 🔧 Overview of Cloud Tools

Cloud tools are categorized into core services that most applications require:

---

### 🖥️ 3.2.1 Compute

Used to run applications and workloads.

| Provider | Compute Service           | Description                              |
|----------|---------------------------|------------------------------------------|
| AWS      | EC2 (Elastic Compute Cloud) | Virtual machine instances                |
| Azure    | Virtual Machines           | Windows/Linux VMs                        |
| GCP      | Compute Engine             | Customizable and scalable VMs            |

📝 *Use Case:* Host a Node.js server on EC2 or Azure VM.

---

### 💾 3.2.2 Storage

Used to store and retrieve unstructured data like files, backups, and media.

| Provider | Storage Service            | Features                                 |
|----------|----------------------------|------------------------------------------|
| AWS      | S3 (Simple Storage Service) | Object storage with versioning           |
| Azure    | Blob Storage                | Good for large unstructured datasets     |
| GCP      | Cloud Storage               | Offers nearline, coldline storage tiers  |

📝 *Use Case:* Store image and video files for a web app.

---

### 🗃️ 3.2.3 Database

Used to store structured data in SQL or NoSQL format.

| Provider | Database Service          | Type        |
|----------|---------------------------|-------------|
| AWS      | Amazon RDS                | Relational (MySQL, PostgreSQL, etc.) |
| Azure    | Azure SQL Database        | Relational |
| GCP      | Cloud SQL                 | Relational |
|          | Firestore / BigTable      | NoSQL       |

📝 *Use Case:* Store customer data, run queries for reporting and analytics.

---

## 🛠️ Practical Works

### 1️⃣ Set Up Free-Tier Accounts

| Task | AWS | Azure | GCP |
|------|-----|-------|-----|
| Sign-up | aws.amazon.com | portal.azure.com | cloud.google.com |
| Free Tier Includes | EC2 (750 hrs/month), S3 (5 GB) | VMs, Blob, SQL DB (limited) | Compute, Storage, SQL |
| Limitations | Limited to 12 months; billing required | Credit-based, then pay-as-you-go | Requires card; 90-day free trial |

📝 *Student Task:* Document the steps to create a free account and list what’s included in each platform.

---

### 2️⃣ Cloud Storage Setup and File Upload

| Provider | Steps |
|----------|-------|
| AWS S3 | Create bucket → Set permissions → Upload file → Share link |
| Azure Blob | Create storage account → Create container → Upload blob |
| GCP Storage | Create bucket → Upload file via console or CLI → View file |

📝 *Sample File:* Upload a `.txt` file or `.jpg` image and access it via URL.

---

### 3️⃣ Perform Basic SQL Queries

Set up cloud-based database services and perform basic operations like:

```sql
-- Create table
CREATE TABLE Students (id INT, name VARCHAR(50));

-- Insert data
INSERT INTO Students VALUES (1, 'Sita');

-- Select query
SELECT * FROM Students;
