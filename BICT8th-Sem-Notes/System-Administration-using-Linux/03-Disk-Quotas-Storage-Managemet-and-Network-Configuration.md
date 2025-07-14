# 🧠 System Administration using Linux — Unit 3: Exam Preparation Notes

**Unit Title**: Disk Quotas, Storage Management, and Network Configuration  
**Course Code**: ICT.Ed.486  
**Level**: Bachelor (BICTE Program)  
**Semester**: 8th  

---

## 🎯 Specific Objectives

By the end of this unit, students will be able to:

- Configure and manage **disk quotas** to control user storage usage effectively and prevent misuse of disk space.  
- Implement different **RAID levels** focusing on redundancy and performance optimization.  
- Create and manage **Logical Volumes** for flexible and efficient storage allocation.  
- Configure and manage **IPv4 and IPv6 addresses** including static and dynamic IP settings.  
- Diagnose and resolve **network connectivity issues** using various network troubleshooting tools.

---

## 🧩 Unit 3 Contents in Detail

### 🔹 3.1 Disk Quotas, RAID Implementation, and Logical Volumes

#### Disk Quotas

- **Purpose**: Limit the amount of disk space and number of files (inodes) that users or groups can consume to prevent a single user from filling up the disk and affecting others.
- **How it works**: Disk quotas can be enabled on file systems and configured to specify soft and hard limits for storage.
- **Key Commands**:
  - `quota` — Display current quotas.
  - `edquota` — Edit quota limits for users/groups.
  - `repquota` — Report quota usage.
  - `quotaon` / `quotaoff` — Enable or disable quotas on file systems.
- **Configuration**:
  - Enable quotas in `/etc/fstab` by adding `usrquota` and/or `grpquota` options.
  - Initialize quota database files with `quotacheck`.

📝 *Real-Life Example*:  
In a university computer lab, disk quotas are set so that students can only use up to 5 GB of disk space. This prevents one student from monopolizing storage and ensures fair resource use for all.

---

#### RAID (Redundant Array of Independent Disks)

- **Purpose**: Provides data redundancy and/or performance improvement by combining multiple disks into a single logical unit.
- **Common RAID Levels**:
  - **RAID 0**: Striping (performance boost, no redundancy)
  - **RAID 1**: Mirroring (data copied identically on two disks — redundancy)
  - **RAID 5**: Striping with parity (balance of performance and redundancy)
- **Software RAID in Linux**: Managed by `mdadm` tool.
- **Important Commands**:
  - `mdadm --create` — Create RAID arrays.
  - `mdadm --detail` — Show RAID status.
  - `mdadm --assemble` — Assemble existing RAID devices.

📝 *Real-Life Example*:  
A small business uses RAID 1 mirroring to protect critical customer data on two hard drives. If one disk fails, data is still available on the other.

---

#### Logical Volume Management (LVM)

- **Purpose**: Provides flexible disk management by abstracting physical storage into logical volumes that can be resized and moved easily.
- **Components**:
  - **Physical Volumes (PV)**: Actual physical disks or partitions.
  - **Volume Groups (VG)**: Pools of physical volumes.
  - **Logical Volumes (LV)**: Created from volume groups and used like traditional partitions.
- **Key Commands**:
  - `pvcreate` — Initialize physical volumes.
  - `vgcreate` — Create a volume group.
  - `lvcreate` — Create logical volumes.
  - `lvextend` / `lvreduce` — Resize logical volumes.

📝 *Real-Life Example*:  
An IT admin needs to increase the disk space allocated to a database server. Instead of repartitioning disks, they extend the logical volume dynamically using LVM commands without downtime.

---

### 🔹 3.2 IPv4 and IPv6 Addressing, IP Configuration & Network Troubleshooting

#### IP Addressing and Configuration

- **IPv4 vs IPv6**:
  - IPv4 uses 32-bit addresses (e.g., 192.168.1.10).
  - IPv6 uses 128-bit addresses (e.g., 2001:0db8::1).
- **Static IP**: Manually assigned IP addresses.
- **Dynamic IP**: Assigned automatically by DHCP.
- **Common Tools**:
  - `ifconfig` or `ip addr` — Show and configure network interfaces.
  - `nmcli` — Manage NetworkManager connections.
  - Configuration files like `/etc/network/interfaces` or `/etc/netplan/*.yaml`.

📝 *Real-Life Example*:  
In a data center, servers use static IPs for consistency, configured manually or via automation tools. Client machines often use DHCP to get dynamic IP addresses from the router.

---

#### Routing and Troubleshooting

- **Routing**:
  - View routing table: `route` or `ip route`.
  - Modify routes to direct traffic.
- **Troubleshooting Tools**:
  - `ping`: Check connectivity between hosts.
  - `traceroute`: Show path packets take to a destination.
  - `netstat` / `ss`: Display network connections, sockets, and ports.
  - `tcpdump`: Capture network packets for deep analysis.

📝 *Real-Life Example*:  
When a remote office cannot access the main company server, the network admin uses `ping` and `traceroute` to identify network hops causing delays and fixes routing configuration.

---

## 🧪 Practical Activities

| Task                                  | Commands / Tools                                 |
|--------------------------------------|-------------------------------------------------|
| Configure and manage disk quotas     | `quota`, `edquota`, `repquota`, `quotacheck`    |
| Implement RAID 1 using mdadm          | `mdadm --create`, `mdadm --detail`              |
| Manage logical volumes with LVM      | `pvcreate`, `vgcreate`, `lvcreate`, `lvextend`  |
| Configure static and dynamic IP      | `ifconfig`, `ip addr`, `nmcli`, edit config files |
| Diagnose network issues              | `ping`, `traceroute`, `netstat`, `tcpdump`      |

---

## 📝 Quick Command Reference

| Command              | Purpose                                      |
|----------------------|----------------------------------------------|
| `quota`, `edquota`   | Set and edit user/group disk quotas          |
| `mdadm`              | Manage software RAID arrays                   |
| `pvcreate`, `vgcreate`, `lvcreate` | Create and manage LVM components      |
| `ifconfig`, `ip addr`| View/configure network interfaces             |
| `route`, `ip route`  | View/manage routing tables                     |
| `ping`               | Test network connectivity                      |
| `traceroute`         | Trace packet path to diagnose network routes  |
| `netstat`, `ss`      | Display network sockets and connections        |
| `tcpdump`            | Capture network traffic packets                |

---

## 💡 Exam Tips

- Practice setting up **disk quotas** on virtual machines and observe quota limits in action.  
- Understand the **benefits and setup steps** for RAID 1 and how to monitor RAID status.  
- Try creating, extending, and reducing **logical volumes** using LVM commands.  
- Get comfortable with **IPv4 and IPv6 configuration**, both static and DHCP.  
- Use network troubleshooting tools to analyze common network issues and interpret their outputs.  
- Relate each topic to real-life scenarios for better retention.

---

> _Prepared for students of BICTE 8th Semester — Unit 3: System Administration using Linux_
