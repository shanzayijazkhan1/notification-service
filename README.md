# Notification Service (FastAPI + Queue)

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Tests](https://img.shields.io/badge/tests-pytest-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)


Accepts notification jobs (email/SMS stubs) and processes them asynchronously with an in-memory queue. Replace with RabbitMQ in production.

## Run
```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
