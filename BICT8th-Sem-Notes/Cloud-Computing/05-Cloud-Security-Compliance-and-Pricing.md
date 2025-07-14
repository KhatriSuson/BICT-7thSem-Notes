## Unit 5: Cloud Security, Compliance, and Pricing

### ✅ Specific Objectives
- Explain the different security challenges in Cloud.
- Implement Identity and Access Management (IAM).
- Know different compliance standards.
- Understand pricing models in Cloud Services.

---

### 🛡️ 5.1 Security Challenges in Cloud Computing

Cloud security involves protecting data, applications, and infrastructure associated with cloud computing.

#### ⚠️ Common Cloud Security Challenges:
- **Data breaches** due to misconfiguration
- **Insider threats** or unauthorized access
- **Insecure APIs**
- **Shared responsibility model confusion**
- **Multi-tenancy risks** in public clouds

#### 🧠 Real-World Example:
A misconfigured S3 bucket in AWS exposed user data from a large company because it was set to public instead of private.

---

### 🔐 5.2 Identity and Access Management (IAM)

IAM is a framework of policies and technologies to ensure the right individuals access the right resources at the right times.

#### 📌 Features of IAM:
- **Authentication**: Confirming user identity
- **Authorization**: Granting access to resources
- **Roles and Policies**: Define what users can do (e.g., read-only, admin)

#### ✅ Example:
- **AWS IAM**: Define users/groups and attach policies (e.g., allow EC2 access)
- **Azure AD**: Integrate with enterprise identities
- **GCP IAM**: Assign roles at project/resource level

---

### 🔐 5.3 Encryption and Data Privacy

Encryption ensures that even if data is accessed, it cannot be read without the key.

#### Types of Encryption:
- **At Rest**: Encrypt data stored on disk (e.g., EBS volumes)
- **In Transit**: Encrypt data over the network (e.g., HTTPS, TLS)

#### Data Privacy:
- Ensure compliance with laws (GDPR, HIPAA) for storing and processing personal data

---

### 📝 5.4 Compliance Standards

Cloud providers must comply with various global security standards and frameworks:

| Standard | Description |
|----------|-------------|
| **ISO/IEC 27001** | Global standard for information security |
| **SOC 2** | Ensures secure handling of customer data |
| **GDPR** | Data protection regulation in the EU |
| **HIPAA** | Health data security standard in the US |

✅ Cloud platforms (AWS, Azure, GCP) offer compliance reports in their security documentation.

---

### 💰 5.5 Pricing Models in Cloud Computing

Cloud pricing varies by provider and service used.

#### ⚙️ Key Pricing Models:
- **Pay-as-you-go**: Pay only for what you use (e.g., EC2 hourly rates)
- **Reserved Instances**: Pay upfront for long-term use (discounted)
- **Free Tier**: Limited usage for free (great for students and testing)
- **Spot Instances**: Use unused compute capacity at lower rates (volatile)

#### 💡 Example:
AWS charges per GB for S3 storage, per vCPU/hour for EC2, and per request for Lambda.

---

### 🛠️ Practical Works

1. **Cloud Platform Security Configurations**:
   - Configure **firewalls or security groups** to restrict incoming/outgoing traffic on ports (e.g., allow HTTP/HTTPS only).
   - Example in AWS:
     ```bash
     aws ec2 authorize-security-group-ingress --group-id sg-123abc --protocol tcp --port 80 --cidr 0.0.0.0/0
     ```

2. **Implement IAM Roles & Permissions**:
   - Create different IAM users:
     - `Admin`: Full access
     - `Developer`: Limited access to deploy apps
     - `Read-Only`: View resources only
   - Assign appropriate **policies** or **roles** in:
     - AWS IAM
     - Azure Active Directory
     - Google Cloud IAM

---

### 📌 Summary

- Cloud security is a shared responsibility; you must secure configurations, identities, and data.
- IAM enables fine-grained access control.
- Encryption protects data privacy.
- Compliance ensures legal and regulatory alignment.
- Cloud pricing varies and should be understood before deploying resources.

> _Prepared for: B.Ed. Eighth Semester – Cloud Computing (ICT.Ed 483), Tribhuvan University_
