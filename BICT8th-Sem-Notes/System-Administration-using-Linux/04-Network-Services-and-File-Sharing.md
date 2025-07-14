# 🧠 System Administration using Linux — Unit 3: Exam Preparation Notes

**Unit Title**: Disk Quotas, Storage Management, and Network Configuration  
**Course Code**: ICT.Ed.486  
**Level**: Bachelor (BICTE Program)  
**Semester**: 8th  

---

## 🎯 Specific Objectives

By the end of this unit, students will be able to:

- Configure and manage **disk quotas** to control user storage usage.  
- Implement **RAID** levels for data redundancy and performance optimization.  
- Create and manage **logical volumes** for flexible storage allocation.  
- Configure and manage **IPv4 and IPv6 addressing** and routing.  
- Diagnose and resolve **network connectivity issues** using troubleshooting tools.

---

## 🧩 Unit 3 Contents

### 🔹 3.1 Disk Quotas, RAID, and Logical Volumes

- **Disk Quotas**:
  - Limit user/group disk usage to avoid storage abuse.
  - Commands: `quota`, `edquota`, `repquota`, `quotaon`, `quotaoff`.
  - Edit `/etc/fstab` to enable quotas on partitions.
- **RAID (Redundant Array of Independent Disks)**:
  - Levels: RAID 0, RAID 1, RAID 5, RAID 10.
  - Focus on **RAID 1** (mirroring) for redundancy.
  - Tools: `mdadm` for software RAID management.
- **Logical Volume Management (LVM)**:
  - Create flexible storage pools.
  - Commands: `pvcreate`, `vgcreate`, `lvcreate`, `lvextend`, `lvreduce`.
- **Disk and Inode Limits**:
  - Monitor with `df`, `du`, and `df -i`.

📝 *Real-Life Example*:  
An organization uses RAID 1 to mirror critical data disks, ensuring data availability in case one disk fails.

---

### 🔹 3.2 IPv4 and IPv6 Addressing & Network Troubleshooting

- **IP Addressing**:
  - Static vs Dynamic IP configuration.
  - Tools: `ifconfig`, `ip addr`, `nmcli`.
  - IPv4 and IPv6 fundamentals.
- **Routing**:
  - View and configure routing tables (`route`, `ip route`).
- **Network Troubleshooting Tools**:
  - `ping` — test connectivity.
  - `traceroute` — trace packet path.
  - `netstat` / `ss` — socket statistics.
  - `tcpdump` — capture network packets.
- **Diagnose connectivity issues** using these tools and logs.

📝 *Real-Life Example*:  
A network admin troubleshoots why a server cannot reach the internet using `ping` and fixes the static IP misconfiguration.

---

## 🧪 Practical Activities

| Task                                | Tools/Commands                              |
|------------------------------------|---------------------------------------------|
| Configure and manage disk quotas   | `quota`, `edquota`, `repquota`, enable quotas in `/etc/fstab` |
| Implement RAID 1 with mdadm        | `mdadm --create`, `mdadm --detail`          |
| Create and manage logical volumes  | `pvcreate`, `vgcreate`, `lvcreate`, `lvextend` |
| Configure static/dynamic IP        | `ifconfig`, `ip addr`, `nmcli`              |
| Network troubleshooting            | `ping`, `traceroute`, `netstat`, `tcpdump` |

---

## 📝 Cheatsheet

| Command                  | Purpose                               |
|--------------------------|-------------------------------------|
| `quota`, `edquota`       | Set and edit disk quotas             |
| `mdadm`                  | Manage software RAID arrays          |
| `pvcreate`, `vgcreate`, `lvcreate` | Manage LVM storage                |
| `ifconfig`, `ip addr`    | Network interface configuration      |
| `route`, `ip route`      | View/manage routing tables            |
| `ping`, `traceroute`     | Connectivity testing and troubleshooting |
| `netstat`, `ss`          | Network connection stats              |
| `tcpdump`                | Packet capture for network analysis  |

---

## 💡 Exam Tips

- Understand the **purpose and setup** of disk quotas and RAID levels.  
- Practice creating and managing logical volumes with LVM commands.  
- Be able to configure static and dynamic IP addresses on Linux systems.  
- Familiarize yourself with key **network troubleshooting tools** and how to interpret their outputs.  
- Try hands-on labs using virtual machines or physical hardware for better retention.

---

> _Prepared for students of BICTE 8th Semester — Unit 3: System Administration using Linux_
