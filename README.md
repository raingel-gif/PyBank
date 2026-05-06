---

# 🧪 Example README for your PyBank project

You can use this as a starter:

:::writing{variant="standard" id="readme1"}
# PyBank 🏦

A simple Python file-based database system.

## 📌 Features
- Append values to a file
- Get stored values
- Replace existing values
- Show all stored data

## 🚀 Usage

Copyright (c) 2026 Rain Tolentino

All rights reserved.

This code may not be copied, modified, distributed, or used without explicit permission.
print(pb.get_value('ages.txt', 'Rain Tolentino'))
pb.show_all('ages.txt')


```python
from PyBank import PyBank

pb = PyBank()

pb.append('ages.txt', 'Rain Tolentino', 13)
