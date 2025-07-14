# 🧠 System Administration using Linux — Unit 2: Exam Preparation Notes

**Unit Title**: Installation, Boot Process and User Administration  
**Course Code**: ICT.Ed.486  
**Level**: Bachelor (BICTE Program)  
**Semester**: 8th  

---

## 🎯 Specific Objectives

By the end of this unit, students will be able to:

- Perform **Linux installation**, manage the **boot sequence**, and configure the **kernel and boot loaders**.
- Manage **user accounts**, **groups**, enforce **password policies**, and configure **authentication settings**.
- Configure **file permissions** and **Access Control Lists (ACLs)** for secure system resource management.

---

## 🧩 Unit 2 Contents

### 🔹 2.1 Linux Installation & Boot Process

#### 📌 Topics:
- **Linux Installation Methods**:
  - Manual (ISO)
  - Network-based (PXE boot)
- **Boot Sequence**:
  - BIOS → MBR/UEFI → GRUB → Kernel → init/systemd
- **Kernel Initialization**:
  - Loads drivers/modules
  - Initializes system hardware
- **Boot Loaders**:
  - GRUB, LILO
  - Configuration: `/boot/grub/grub.cfg`
- **Kernel Modules**:
  - Dynamically loadable drivers
  - Commands: `lsmod`, `modprobe`, `insmod`, `rmmod`

📝 *Real-Life Example*:  
A school’s IT lab technician installs Ubuntu using a bootable USB and edits GRUB to add boot parameters for enabling legacy hardware support.

---

### 🔹 2.2 User and Permission Management

#### 📌 Topics:
- **User Account Management**:
  - `useradd`, `usermod`, `userdel`
  - Home directories and shell assignment
- **Group Administration**:
  - `groupadd`, `gpasswd`, `groups`
- **Password Policies**:
  - Enforce expiration using `/etc/login.defs`
  - Set password complexity rules via `pam_pwquality.so`
- **Authentication Configuration**:
  - PAM (Pluggable Authentication Modules)
  - File: `/etc/pam.d/*`
- **File Permissions**:
  - `chmod`, `chown`, `umask`
- **Access Control Lists (ACLs)**:
  - `setfacl`, `getfacl`
  - Use ACLs to give user-specific permissions

📝 *Real-Life Example*:  
An admin at a government office sets ACLs on a folder so that one specific user can write reports without changing permissions for others.

---

## 🧪 Practical Activities

| Task | Tools/Commands |
|------|----------------|
| Install Linux and configure GRUB | `grub-install`, `update-grub`, VM setup |
| Create and manage users/groups | `useradd`, `passwd`, `groupadd`, `usermod` |
| Configure file permissions and ACLs | `chmod`, `chown`, `setfacl`, `getfacl` |

---

## 📝 Cheatsheet

| Command            | Use |
|--------------------|-----|
| `useradd`, `passwd`| Add user and set password |
| `groupadd`, `usermod -aG` | Create group and assign users |
| `chmod`, `chown`, `umask` | File permissions |
| `lsmod`, `modprobe` | View/load kernel modules |
| `grub-install`, `update-grub` | Bootloader configuration |
| `setfacl`, `getfacl` | Access control management |

---

## 💡 Exam Tips

- Understand each **stage of the boot process** (BIOS → GRUB → Kernel → init).
- Be familiar with **user management commands and config files**.
- Know how to **enforce password aging and complexity**.
- Practice ACL configuration scenarios.
- Practice installing Linux using a virtual machine and editing GRUB settings.

---

> _Prepared for students of BICTE 8th Semester — Unit 2: System Administration using Linux_