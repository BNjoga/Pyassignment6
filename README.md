# 🌍 Ubuntu-Inspired Image Fetcher

> **"I am because we are" – Ubuntu Philosophy**

This project is a Python script that connects to the global web community, fetches images from given URLs, and organizes them into a dedicated folder. It’s built with Ubuntu principles in mind: **community, respect, sharing, and practicality**.

---

## ✨ Features
- Prompts the user for an image URL  
- Creates a `Fetched_Images` folder automatically if it doesn’t exist  
- Downloads the image and saves it with an appropriate filename  
- Handles HTTP errors gracefully without crashing  
- Organizes images for later sharing  

---

## 📦 Requirements
- Python 3.7+  
- Libraries:
  - `requests`  
  - (standard library) `os`  
  - (standard library) `urllib.parse`  

Install `requests` with:
```bash
pip install requests
