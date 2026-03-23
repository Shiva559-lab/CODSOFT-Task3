# CODSOFT-Task3
# 🔐 Task 3 — Password Generator

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=flat-square&logo=python)
![CLI](https://img.shields.io/badge/Interface-CLI-lightgrey?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

A powerful **command-line password generator** built with Python. Generate strong, random passwords with full control over length, complexity, and character composition — with a built-in entropy-based strength meter.

---

## 📸 Preview

```
═════════════════════════════════════════════
        🔐 Python Password Generator
═════════════════════════════════════════════

Enter desired password length (4–128): 16

Select password complexity:
  1. Low       (letters only)
  2. Medium    (letters + digits)
  3. High      (letters + digits + symbols)
  4. Custom    (you choose character types)

─────────────────────────────────────────────
  Complexity : High (letters + digits + symbols)
  Length     : 16 characters
  Strength   : Very Strong
─────────────────────────────────────────────

  Generated Passwords:

    1. tR7#mZ!qW2@kLp9&
    2. Xn$4vB!8rQ#2Yz&K
    3. p@9Lw!3Tk#Zn7$Xq

─────────────────────────────────────────────
  Tip: Store your password in a secure password manager.
─────────────────────────────────────────────
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 📏 **Custom Length** | Set password length from 4 to 128 characters |
| 🔒 **4 Complexity Levels** | Low, Medium, High, and fully Custom modes |
| ⚙️ **Custom Charset** | Pick exactly which character types to include |
| 🔢 **Batch Generation** | Generate 1–10 passwords in a single run |
| 📊 **Strength Meter** | Entropy-based rating: Weak / Fair / Strong / Very Strong |
| 🔄 **Loop Mode** | Generate again without restarting the program |
| ✅ **Input Validation** | Rejects invalid lengths and out-of-range inputs |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- No external packages required

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/python-projects.git
cd python-projects/task3-password-generator

# Run the application
python password_generator.py
```

---

## 🎯 Complexity Levels

| Level | Characters Included | Example Output |
|---|---|---|
| 🟡 **Low** | `a-z`, `A-Z` | `GkRtBmPwLsNqZvCd` |
| 🟠 **Medium** | Letters + `0-9` | `Gk4tBm7wLs2qZv9C` |
| 🔴 **High** | Letters + digits + `!@#$...` | `G#4t!m7@L$2qZ&9C` |
| ⚙️ **Custom** | You choose each type | _user-defined_ |

---

## 📊 Strength Meter

Password strength is calculated using **Shannon entropy** (`length × log₂(charset size)`):

| Entropy | Rating |
|---|---|
| < 40 bits | 🔴 Weak |
| 40 – 59 bits | 🟡 Fair |
| 60 – 79 bits | 🟠 Strong |
| 80+ bits | 🟢 Very Strong |

---

## 📁 Project Structure

```
task3-password-generator/
│
└── password_generator.py   # Main application (single file)
```

---

## 🛡 Security Notes

- Uses Python's `random` module with `random.shuffle()` for character randomization
- For cryptographically secure use cases, the `random` calls can be replaced with `secrets.choice()`
- Passwords are **never stored or logged** — displayed only on screen

---

## 🛠 Built With

- **Python 3** — Core language
- **`random`** — Random character selection & shuffle
- **`string`** — Built-in character set constants
- **`math`** — Entropy calculation

---

## 📜 License

This project is licensed under the MIT License.
