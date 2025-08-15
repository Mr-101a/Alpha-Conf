
# Convertـconf - Installation Guide

Welcome! This guide will walk you through installing and running the **convertـconf** program on your Linux system.

This tool converts `.conf` configuration files into usable C++ code .

---

## 📁 Files Required

Make sure the following three files are placed in the **same directory**:

1. `convertـconf`  *(binary executable)*  
2. `install_tools.sh`  
3. `install_conf.sh`  

**⚠️ All files must be in the same folder before starting installation.**

---

## 🧩 Step-by-Step Installation

### 1️⃣ Make `install_tools.sh` executable

Open your terminal, navigate to the folder containing the files, and run:

```bash
chmod +x install_tools.sh
```

---

### 2️⃣ Run `install_tools.sh`

This script installs required dependencies :

```bash
./install_tools.sh
```

---

### 3️⃣ Run `install_conf.sh`

This script copies the main binary to a system-wide path:

```bash
./install_conf.sh
```

It will search for the file `convertـconf` or variants, and move it to:

```
/usr/local/bin/convertـconf
```

> ✅ No need to use `chmod` manually. The script will handle permissions.

---

##  How to Run the Program

Once installed, you can simply type the following in the terminal to launch the converter:

```bash
convertـconf
```

This will open the graphical interface for selecting `.conf` files and converting them.

---

##  What It Does

- Reads structured `.conf` files.
- Converts key-value pairs to valid C++ variable declarations.
- Useful for simulation environments that require C++ configuration code.

---

## 💬 Notes

- If any errors occur during installation, try running the scripts with `sudo`.

---

Enjoy using _convertـconf_!  
Created by **Mr.101 | Alpha Team** – Tehran, Iran  
Contact: emadshojaee.sh@gmail.com  
Channel: [t.me/Alpha_Development_Team](https://t.me/Alpha_Development_Team)
