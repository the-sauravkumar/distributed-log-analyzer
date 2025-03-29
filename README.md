# **LogMaster: Distributed Log Analyzer for Large-Scale Systems**

![LogMaster](https://img.shields.io/badge/Status-Active-green.svg) ![License](https://img.shields.io/badge/License-MIT-blue.svg)

## **🚀 Overview**
LogMaster is a **high-performance distributed log analysis system** that helps organizations process, analyze, and visualize large-scale log data efficiently. It integrates **FastAPI, Apache Kafka, Dask, PostgreSQL, Elasticsearch, Redis, and React.js** to provide **real-time anomaly detection** and a **dashboard visualization**.

## **🔹 Features**
- **Real-time log ingestion** using Apache Kafka
- **Parallel log processing** with Dask/Spark
- **AI-based anomaly detection** using Isolation Forest
- **Scalable storage** with PostgreSQL & Elasticsearch
- **Fast caching** with Redis
- **Interactive dashboard** built with React.js & Chart.js
- **Fully containerized** using Docker & Docker Compose

---

## **📂 Project Structure**
```plaintext
logmaster/
│── backend/                    # FastAPI Backend
│   ├── main.py                 # API Server
│   ├── log_ingestion.py        # Kafka Producer
│   ├── log_processing.py       # Dask/Spark Processing
│   ├── anomaly_detection.py    # AI Anomaly Detector
│   ├── database.py             # PostgreSQL & Elasticsearch Integration
│   ├── redis_cache.py          # Redis Caching
│── frontend/                   # React.js Dashboard
│   ├── src/
│   │   ├── components/         # UI Components
│   │   ├── pages/              # Dashboard Pages
│   │   ├── App.js
│   │   ├── index.js
│── docker-compose.yml          # Docker Setup
│── .env                        # Environment Variables
│── README.md                   # Documentation
```

---

## **🔧 Installation & Setup**
### **1️⃣ Prerequisites**
Ensure the following are installed:
- **Python 3.8+**
- **Node.js 16+ & npm**
- **Docker & Docker Compose**
- **Kafka, PostgreSQL, Redis** (installed via Docker)

### **2️⃣ Clone the Repository**
```sh
git clone https://github.com/your-username/logmaster.git
cd logmaster
```

### **3️⃣ Setup Backend**
#### **Install Dependencies**
```sh
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### **Run Backend Locally**
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### **4️⃣ Setup Frontend**
#### **Install Dependencies**
```sh
cd frontend
npm install
```

#### **Run Frontend Locally**
```sh
npm start
```
Access the dashboard at **`http://localhost:3000`**

### **5️⃣ Deploy with Docker**
```sh
docker-compose up -d
```

---

## **📡 API Endpoints**
| Method | Endpoint          | Description |
|--------|------------------|-------------|
| `POST` | `/logs`          | Ingest a log |
| `GET`  | `/logs`          | Fetch logs |
| `GET`  | `/process`       | Start log analysis |

### **Example: Send a Log Entry**
```sh
curl -X POST "http://localhost:8000/logs" -H "Content-Type: application/json" \
-d '{"message": "Server error detected", "status_code": 500, "timestamp": 1712000000}'
```

---

## **📊 Dashboard (React.js + Chart.js)**
- Displays real-time logs with status codes
- Visualizes anomalies using line/bar charts
- Refreshes data automatically every few seconds

#### **Frontend Preview**
> Open `http://localhost:3000` in a browser.

---

## **📜 Environment Variables**
Create a **`.env`** file in the **backend/** directory:
```plaintext
KAFKA_BOOTSTRAP_SERVERS=localhost:9092
POSTGRES_DB=logs
POSTGRES_USER=user
POSTGRES_PASSWORD=password
REDIS_HOST=localhost
REDIS_PORT=6379
ELASTICSEARCH_HOST=http://localhost:9200
```

---

## **🚀 Deployment**
To deploy on a **cloud server**, use:
```sh
docker-compose -f docker-compose.prod.yml up -d
```

For **Kubernetes deployment**, create YAML configurations for each service.

---

## **📌 Contributing**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m "Added new feature"`)
4. Push to GitHub (`git push origin feature-name`)
5. Create a pull request

---

## **📜 License**
This project is licensed under the **MIT License**.

---

## **🛠️ Future Enhancements**
✅ Add Role-Based Access Control (RBAC) 🔒
✅ Deploy using Kubernetes 🚀
✅ Implement AI-powered log correlation 🤖

For any issues, contact **thesauravkumar@hotmail.com**

---

> **LogMaster: Simplify Large-Scale Log Analysis with AI & Cloud! 🚀**

