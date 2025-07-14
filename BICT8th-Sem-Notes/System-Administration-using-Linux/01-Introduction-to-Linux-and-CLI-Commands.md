# 📘 System Administration using Linux — Exam Preparation Notes

**Course Code**: ICT.Ed.486  
**Nature of Course**: Theoretical + Practical  
**Credit Hours**: 3 (1.5 Theory + 1.5 Practical)  
**Level**: Bachelor (BICTE Program)  
**Teaching Hours**: 48 (24 Theory + 24 Practical)  
**Semester**: 8th  

---

## 🎯 Course Learning Outcomes

By the end of this course, students will be able to:

- Understand the foundational principles and advantages of **open-source software** in the modern IT industry.
- Operate and navigate **Linux-based systems** using command-line interface (CLI).
- Perform **text processing**, **file operations**, and **process control** for system administration.
- Manage **Linux file systems** and **install/update software packages** using package managers.
- Apply knowledge through real-life examples like managing web servers, configuring user accounts, or automating tasks.

---

## 🧠 Detailed Exam Preparation Notes with Examples

### 🔹 1. Open Source Software

**Definition**: Software with source code available for anyone to inspect, modify, and enhance.

**Benefits**:
- Cost-effective (Free to use)
- Community support
- Transparency
- Security and flexibility

**Examples**:
- **Linux OS** (Ubuntu, Fedora): Used by Facebook, NASA, Google servers.
- **Apache Web Server**: Hosts over 30% of websites globally.
- **LibreOffice**: An alternative to MS Office in government institutions.

📝 *Real-Life Example*:  
Many startups use **Linux and open-source stack** (LAMP: Linux, Apache, MySQL, PHP) to reduce software costs while hosting their websites.

---

### 🔹 2. Unix/Linux System Architecture & CLI

#### 🧩 Architecture Components:
- **Kernel**: Core system component that interacts with hardware.
- **Shell**: Interface for user commands.
- **File System**: Organizes files into directories.

#### 📟 Common CLI Commands:
| Purpose         | Command Examples                         |
|----------------|-------------------------------------------|
| File Navigation | `cd`, `ls`, `pwd`                         |
| File Handling   | `cp`, `mv`, `rm`, `mkdir`, `touch`        |
| Permissions     | `chmod`, `chown`, `umask`                |

📝 *Real-Life Example*:  
A system admin in a hospital may use `chmod` to restrict access to sensitive patient records on the server (`chmod 700 patient_data.txt`).

---

### 🔹 3. File Management

**Tasks**:
- Create, delete, move, rename files and directories.
- Manage permissions.

```bash
mkdir reports
cd reports
touch jan.txt feb.txt
mv jan.txt archive/
chmod 755 feb.txt
```

📝 *Real-Life Example*:  
Organizing files in a university's server: professors have read/write access, while students only have read access to course materials.

---

### 🔹 4. Shell Commands

**Shell Features**:
- Command chaining (`&&`, `||`)
- Variables: `name="Alice"`
- Quoting: `' '` vs `" "`
- Wildcards: `*.txt`, `file?.log`

```bash
name="John"
echo "Welcome, $name"
ls *.pdf && echo "PDF files listed"
```

📝 *Real-Life Example*:  
Automating daily backups using a shell script and cron job:  
```bash
#!/bin/bash
tar -czf backup_$(date +%F).tar.gz /home/user/docs
```

---

### 🔹 5. Text Processing

**Commands**:
- `grep`: Search for text
- `awk`: Pattern scanning and reporting
- `sed`: Stream editing

```bash
grep "error" server.log
awk '{print $1, $5}' data.csv
sed 's/old/new/g' file.txt
```

📝 *Real-Life Example*:  
Use `grep` to extract failed login attempts from `/var/log/auth.log` for security audits in a bank's server.

---

### 🔹 6. Job Control

**Concepts**:
- Run jobs in background (`&`)
- Monitor (`ps`, `top`)
- Bring jobs to foreground (`fg`, `bg`)
- Kill processes (`kill`, `killall`)

```bash
sleep 300 &
jobs
fg %1
```

📝 *Real-Life Example*:  
Run a system scan in the background while working on other tasks:  
`clamscan / --recursive &`

---

### 🔹 7. File System Concepts

**Structure**:
```
/
/home
/etc
/var
/usr
```

**Commands**:
- View disk usage: `df -h`, `du -sh`
- Mount/unmount: `mount`, `umount`
- Locate files: `find`, `locate`

📝 *Real-Life Example*:  
A university system admin checks available space in `/home` with `df -h` to prevent storage overflow during admission season.

---

### 🔹 8. Package Management

**Debian-based (Ubuntu)**:
```bash
sudo apt update
sudo apt install apache2
```

**RedHat-based (Fedora/CentOS)**:
```bash
sudo dnf install httpd
```

📝 *Real-Life Example*:  
Installing web server software (Apache) on a local development machine for testing school projects.

---

## 🧪 Practical Lab Activities

| Lab | Activity |
|-----|----------|
| Lab 1 | Install Ubuntu on VirtualBox |
| Lab 2 | Use `ls`, `cd`, `mkdir`, `chmod` to manage files |
| Lab 3 | Shell scripting: Automate folder creation with date stamps |
| Lab 4 | Use `grep`, `awk`, `sed` for analyzing `.log` files |
| Lab 5 | Monitor system using `top`, `ps`, and kill unwanted processes |
| Lab 6 | Simulate a software installation using `apt` |
| Lab 7 | Explore `/etc`, `/var`, `/home` and identify real use |
| Lab 8 | Mini Project: Setup a local web server and test site upload |

---

## 📖 Summary Cheatsheet

| Command      | Description                        |
|--------------|------------------------------------|
| `cd`, `ls`   | Navigation                         |
| `cp`, `mv`   | Copy/Move files                    |
| `chmod`, `chown` | Permissions                     |
| `grep`, `awk`, `sed` | Text processing             |
| `ps`, `top`, `kill` | Process/job control          |
| `df`, `du`   | Disk usage                         |
| `apt`, `yum` | Package management                 |

---

## 🧩 Mindmap

```plaintext
System Administration using Linux
│
├── Open Source Software
├── Linux Architecture & Shell
├── File Management
├── Text Processing Tools
├── Process & Job Control
├── Filesystem Hierarchy
└── Software Package Management
```

---

## 💡 Final Tips for Exams

- Practice commands in a Linux environment (e.g., Ubuntu via VirtualBox or WSL on Windows).
- Focus on **syntax** and **use-case**: why and when a command is used.
- Understand the **file system hierarchy** and **permissions logic**.
- Be able to write small **shell scripts** and explain each line.
- Review **real-life use cases** to link theory with practical applications.

---

> _Prepared for students of BICTE 8th Semester — System Administration using Linux_