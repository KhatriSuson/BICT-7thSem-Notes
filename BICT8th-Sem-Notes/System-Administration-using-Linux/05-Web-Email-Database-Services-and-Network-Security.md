# 🧠 System Administration using Linux — Unit 5: Exam Preparation Notes

**Unit Title**: Web, Email, Database Services, and Network Security  
**Course Code**: ICT.Ed.486  
**Level**: Bachelor (BICTE Program)  
**Semester**: 8th  

---

## 🎯 Specific Objectives

By the end of this unit, students will be able to:

- Configure **Apache**, **MySQL**, **Postfix**, and **Dovecot** for seamless web, email, and database operations.  
- Troubleshoot and resolve common issues in servers and network services.  
- Secure systems using **SSL/TLS encryption**, **SSH**, and **firewalls**.  
- Implement **Access Control Lists (ACLs)** and anti-spam measures for enhanced security.

---

## 🧩 Unit 5 Contents in Detail

### 🔹 5.1 Apache, HTTPD, and Email Operations (SMTP, Postfix, Dovecot)

#### Apache HTTP Server

- **Role**: Host websites by serving HTTP/HTTPS requests.  
- **Basic Configuration**:  
  - Document root (default `/var/www/html`)  
  - Virtual Hosts for multiple sites  
  - Modules (e.g., mod_ssl for HTTPS)  
- **Commands**:  
  - `systemctl start|stop|restart httpd` (or apache2)  
  - `apachectl configtest` for syntax checking

#### Email Services: Postfix and Dovecot

- **Postfix**: SMTP server used to send emails.  
- **Dovecot**: IMAP/POP3 server used for receiving and storing emails.  
- **Key Concepts**:  
  - Configure Postfix for mail routing and delivery.  
  - Use Dovecot to allow mail clients to access mailboxes securely.  
  - Enable authentication mechanisms and SSL/TLS for secure mail transfer.

📝 *Real-Life Example*:  
An organization hosts its own mail server using Postfix and Dovecot to manage internal and external emails securely, reducing dependency on third-party email providers.

---

### 🔹 5.2 MySQL Administration

- **Role**: Manage relational databases for applications and websites.  
- **Basic Tasks**:  
  - Installing and securing MySQL server.  
  - Creating databases and users with proper permissions.  
  - Backup and restore databases using `mysqldump`.  
  - Monitor server status and performance.

📝 *Real-Life Example*:  
A web developer uses MySQL to manage user data for an e-commerce website, ensuring fast and reliable data transactions.

---

### 🔹 5.3 Cryptography, SSH, Firewall Configuration, and ACLs

#### SSH (Secure Shell)

- Secure remote login and command execution.  
- Use of SSH keys for passwordless and secure authentication.  
- Configuring `/etc/ssh/sshd_config` for enhanced security (disabling root login, setting port, etc.).

#### SSL/TLS

- Enables encryption for web (HTTPS) and email services.  
- Use `openssl` to generate certificates or obtain from CA like Let’s Encrypt.  
- Configure Apache and Postfix/Dovecot to use SSL/TLS.

#### Firewalls

- Tools: `iptables`, `firewalld`, or `ufw`.  
- Define rules to allow or block traffic based on ports, protocols, IPs.

#### Access Control Lists (ACLs)

- Fine-grained permission control on files and directories beyond standard UNIX permissions.  
- Commands: `setfacl`, `getfacl`.

---

## 🧪 Practical Activities

| Task                                      | Tools/Commands                               |
|------------------------------------------|----------------------------------------------|
| Setup Apache web server                   | `httpd`/`apache2`, configure virtual hosts   |
| Configure email server with Postfix & Dovecot | `postfix`, `dovecot`, mail clients           |
| Secure server with SSH keys               | `ssh-keygen`, `ssh-copy-id`, `sshd_config`  |
| Configure firewall                        | `iptables`, `firewalld`, `ufw`                |
| Implement ACLs for secure file access     | `setfacl`, `getfacl`                          |

---

## 📝 Cheatsheet

| Command/Tool          | Purpose                                         |
|----------------------|-------------------------------------------------|
| `systemctl`           | Start, stop, restart services                    |
| `apachectl`           | Apache configuration test and control            |
| `postfix`             | Mail transfer agent management                    |
| `dovecot`             | IMAP/POP3 server management                        |
| `mysql`, `mysqldump`  | Database management and backup                     |
| `ssh-keygen`, `ssh-copy-id` | Create and deploy SSH keys                   |
| `iptables`, `firewalld`, `ufw` | Firewall configuration                   |
| `openssl`             | SSL/TLS certificate management                     |
| `setfacl`, `getfacl`  | Manage file access control lists                    |

---

## 💡 Exam Tips

- Practice installing and configuring Apache to host multiple sites using virtual hosts.  
- Setup a basic mail server with Postfix and Dovecot, and test sending/receiving emails.  
- Secure communication by configuring SSL/TLS certificates for web and mail servers.  
- Generate and deploy SSH keys to avoid password-based authentication.  
- Familiarize yourself with firewall rules to allow necessary traffic and block threats.  
- Understand how ACLs extend file permission management for specific users and groups.  

---

> _Prepared for students of BICTE 8th Semester — Unit 5: System Administration using Linux_
