# SARVAR_FINAL_WEBAPP_CONTRACT_MANAGER

A full-stack contract management web application with a Flask API backend, PostgreSQL database, and a responsive Bootstrap frontend.

---

## 📌 Overview

This application allows users to:

- **Add** new contracts
- **Delete** existing contracts
- **View** all current contracts

The project is composed of:

- `index_sarvar.html` — A Bootstrap 5 frontend (hosted on S3)
- `app.py` — Flask API backend (hosted on EC2)
- PostgreSQL database — Hosted on AWS RDS

---

## ✅ Features

- RESTful API with Flask
- PostgreSQL integration (via psycopg2)
- CORS-enabled for S3 communication
- Hosted frontend on Amazon S3
- Hosted backend on EC2

---

## 📁 Folder Structure

```
SARVAR_FINAL_WEBAPP_CONTRACT_MANAGER/
├── frontend/
│   └── index_sarvar.html           # Frontend UI
├── webapp_sarvar_backend/
│   ├── app.py                      # Flask API
│   └── requirements.txt            # Python dependencies
└── README.md                       # Project documentation
```

---

## 🔗 Deployed Resources

- 🌐 **Frontend (S3):** [CLICK](http://2t-sarvar-final.s3-website.ap-south-1.amazonaws.com/)
- 🖥️ **Backend (EC2):** [CLICK](http://13.232.36.214:5000/contracts)
- 🗄️ **Database (RDS):** Integrated with the Flask app

---

## 🛠️ Running the Application

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/SARVAR_FINAL_WEBAPP_CONTRACT_MANAGER.git
cd SARVAR_FINAL_WEBAPP_CONTRACT_MANAGER
```

### 2. Backend Setup (EC2)

```bash
cd webapp_sarvar_backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

> ⚠️ Make sure:
>
> - You've set your RDS database credentials in `app.py`
> - You're running the Flask app with `host='0.0.0.0'`
> - Port 5000 is allowed in the EC2 instance's Security Group

---

## 🧾 API Reference

### `GET /contracts`

Returns all contract records.

### `POST /contracts`

Adds a contract.  
**JSON Body:**

```json
{
  "name": "Example Contract",
  "amount": 1000.0
}
```

### `DELETE /contracts/<id>`

Deletes a contract by ID.

---

## 📄 requirements.txt

```
Flask>=2.3.0
flask-cors>=3.0.10
psycopg2-binary>=2.9.0
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🧰 Tech Stack

- **Frontend:** HTML, JavaScript, Bootstrap 5
- **Backend:** Flask, Flask-CORS
- **Database:** PostgreSQL (AWS RDS)
- **Hosting:** Amazon EC2, S3

---

## 📫 Author

Developed by **Sarvar**
