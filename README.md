# NSClient++ Privilege Escalation Exploit (EDB-ID: 46802)

## 📌 Description

This exploit targets a vulnerability in **NSClient++** when the **Web Server** is enabled.

A local low-privileged user can:

- 🕵️‍♂️ Read the web interface administrator password in **cleartext** from the configuration file.
- 🔐 Use the credentials to **log in to the Web UI**.
- ⚙️ Enable the **external script execution** module.
- 📅 Schedule arbitrary scripts to run as **SYSTEM** via the Web API.

> **Note:** A **reboot** may be required for the configuration changes to take effect.

---

## 👤 Author

- **Author:** Z3R0x30  
- **Exploit Database ID:** [46802](https://www.exploit-db.com/exploits/46802)

---

## 🖥️ Affected Software

- **NSClient++** (when installed with the Web Server module enabled)

---

## 🚀 Usage

```bash
./NSClient_Z3R0x30_exploit.py <command> <host> <password>
