# Expense Tracker Application

A full-stack Expense Tracker web application built using:

* **Frontend:** Streamlit
* **Backend:** FastAPI
* **Database:** MySQL
* **Deployment:** Render + Streamlit Cloud

---

# Features

* Add Expenses
* View Expenses
* Update Expenses
* Delete Expenses
* Search Expenses by Category
* Sort Expenses by Amount

---

# Tech Stack

## Frontend

* Python
* Streamlit
* Pandas
* Requests

## Backend

* FastAPI
* MySQL Connector
* Uvicorn

## Database

* MySQL

---

# Project Structure

```bash
expense-tracker/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   └── .streamlit/
│       └── secrets.toml
│
└── README.md
```

---

# Backend Setup (FastAPI)

## Step 1: Install Dependencies

```bash
pip install fastapi uvicorn mysql-connector-python python-dotenv
```

---

## Step 2: Create `.env` File

Create a `.env` file inside backend folder.

```env
db_host=your_host
db_user=your_username
db_password=your_password
db_name=your_database_name
db_port=3306
```

---

## Step 3: Run Backend Server

```bash
uvicorn main:app --reload
```

Backend will run on:

```bash
http://127.0.0.1:8000
```

---

# Frontend Setup (Streamlit)

## Step 1: Install Dependencies

```bash
pip install streamlit pandas requests
```

---

## Step 2: Create Streamlit Secrets File

Create file:

```bash
.streamlit/secrets.toml
```

Add:

```toml
server_url = "YOUR_BACKEND_URL"
```

Example:

```toml
server_url = "https://expense-tracker-api.onrender.com"
```

---

## Step 3: Run Streamlit App

```bash
streamlit run app.py
```

---

# MySQL Database Setup

## Create Database

```sql
CREATE DATABASE expense_tracker;
```

The application automatically creates the `expenses` table.

---

# API Endpoints

| Method | Endpoint                     | Description       |
| ------ | ---------------------------- | ----------------- |
| GET    | /                            | Home Route        |
| POST   | /add_expense                 | Add Expense       |
| GET    | /view_expenses               | View All Expenses |
| DELETE | /delete_expense/{expense_id} | Delete Expense    |
| PUT    | /update_expense/{expense_id} | Update Expense    |
| GET    | /search_expense/{category}   | Search Expenses   |
| GET    | /sort_expense/{sort_type}    | Sort Expenses     |

---

# Deployment on Render (Backend)

## Step 1: Push Code to GitHub

Push your backend code to GitHub repository.

---

## Step 2: Create Render Account

Go to Render website and login.

---

## Step 3: Create New Web Service

* Click **New +**
* Select **Web Service**
* Connect GitHub Repository

---

## Step 4: Configure Service

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
uvicorn main:app --host 0.0.0.0 --port 10000
```

---

## Step 5: Add Environment Variables

In Render dashboard:

* Go to **Environment**
* Add:

| Key         | Value         |
| ----------- | ------------- |
| db_host     | your_host     |
| db_user     | your_user     |
| db_password | your_password |
| db_name     | your_database |
| db_port     | 3306          |

---

## Step 6: Deploy

Click **Create Web Service**

Render will generate backend URL like:

```bash
https://your-app-name.onrender.com
```

---

# Deployment on Streamlit Cloud (Frontend)

## Step 1: Push Frontend Code to GitHub

Upload frontend files to GitHub.

---

## Step 2: Open Streamlit Cloud

Login with GitHub account.

---

## Step 3: Create New App

* Click **New App**
* Select Repository
* Select branch
* Select `app.py`

---

## Step 4: Add Secrets

Open:

```bash
Advanced Settings → Secrets
```

Add:

```toml
server_url = "https://your-render-backend-url.onrender.com"
```

---

## Step 5: Deploy App

Click **Deploy**

Your Streamlit app will be live.

---

# requirements.txt

## Backend

```txt
fastapi
uvicorn
mysql-connector-python
python-dotenv
```

## Frontend

```txt
streamlit
pandas
requests
```

---

# Future Improvements

* User Authentication
* Expense Analytics Dashboard
* Monthly Reports
* Pie Charts & Graphs
* Export Expenses to Excel/PDF

