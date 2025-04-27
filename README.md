# 🚀 Linux Monitoring Dashboard

<div align="center">
  <img src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/GitHub Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white"/>
</div>

---

## 📖 Overview

This project provides a lightweight **Linux Monitoring Dashboard**, built with:
- **Bash scripting** for system data collection
- **Flask API** for serving JSON and HTML views
- **Docker & Docker Compose** for containerization
- **GitHub Actions** for continuous integration (CI)

---

## 🛠 Tech Stack
- Ubuntu (WSL 2)
- Bash
- Python 3.10 + Flask
- Docker & Docker Compose
- GitHub Actions

---

## 📁 Project Structure

├── app.py # Flask App (API + Dashboard) ├── collect_info.sh # Bash Script (System Info) ├── requirements.txt # Python dependencies ├── Dockerfile # Docker Image setup ├── docker-compose.yml # Docker Compose orchestration ├── data.json # Generated system info (auto) ├── bash_practice/ # Bash exercises └── .github/workflows/ci.yml # GitHub Actions workflow

yaml
Copy
Edit

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/yarinbatat/linux-monitoring-dashboard.git
cd linux-monitoring-dashboard
bash collect_info.sh
docker compose up
Then open:

http://localhost:5000/ ➔ Dashboard (HTML)

http://localhost:5000/api ➔ System Info (JSON)

✅ GitHub Actions - CI
On every push:

Runs collect_info.sh

Validates data.json format using jq

🎯 Bash Practice (bonus)
Practice Linux skills with:

list_files.sh

disk_usage.sh

cpu_load.sh

Located inside /bash_practice/

✨ Author
Yarin Batat — Junior DevOps Engineer in the making 🚀


