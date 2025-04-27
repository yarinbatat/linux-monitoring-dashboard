# 🚀 Linux Monitoring Dashboard | Flask + Docker + Grafana + Ansible

<div align="center">
  <img src="https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
  <img src="https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white"/>
  <img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white"/>
  <img src="https://img.shields.io/badge/Ansible-000000?style=for-the-badge&logo=ansible&logoColor=white"/>
</div>

---

## 📖 Overview

Linux Monitoring System including:
- **Flask** app serving a dashboard with real-time Linux metrics (CPU, Memory, Disk).
- **Docker & Docker Compose** orchestration.
- **Prometheus** for metrics scraping.
- **Grafana** for professional visualization.
- **Ansible** for automatic deployment.

---

## 🛠 Tech Stack
- Ubuntu WSL 2 (local)
- Bash Scripting
- Python 3.10
- Docker + Docker Compose
- Prometheus + Grafana
- Ansible Automation
- GitHub Actions (CI/CD)

---

## 📁 Project Structure

├── app.py # Flask web app ├── metrics.py # Prometheus exporter ├── collect_info.sh # System info collector ├── Dockerfile # For app container ├── Dockerfile.metrics # For metrics exporter ├── docker-compose.yml # Services orchestration ├── prometheus.yml # Prometheus config ├── deploy.yml # Ansible Playbook ├── inventory.ini # Ansible Inventory ├── ansible.cfg # Ansible Config └── README.md # This file

yaml
Copy
Edit

---

## 🚀 How to Run Locally

```bash
# Clone the project
git clone https://github.com/yarinbatat/linux-monitoring-dashboard.git
cd linux-monitoring-dashboard

# Deploy using Ansible
ansible-playbook deploy.yml

# or manually:
docker-compose up --build
Then visit:

http://localhost:5000 ➔ Monitoring Dashboard

http://localhost:9090 ➔ Prometheus UI

http://localhost:3000 ➔ Grafana Dashboard

🎯 Features
Realtime Linux system monitoring

Auto-refresh dashboard (every 10 seconds)

Grafana beautiful dashboards

Fully containerized (multi-service setup)

Full Ansible automation (install & deploy)

✨ Author
Yarin Batat — Junior DevOps Engineer 🚀

🔗 GitHub | 🔗 LinkedIn

