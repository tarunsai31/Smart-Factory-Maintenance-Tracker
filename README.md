# 🏭 digital Factory Maintenance Tracker

A web-based application to automate and manage maintenance activities for factory equipment. It enables factory staff or administrators to register machines, track last maintenance dates, and receive visual alerts for due or overdue servicing — all with a clean, intuitive dashboard.

---

## 🚀 Features

- 📋 **Add & Manage Machines**  
  Register factory machines with type, last maintenance date, and maintenance frequency.

- ⏱️ **Automated Status Tracking**  
  Color-coded status indicators (OK, Due, Overdue) based on maintenance frequency.

- 🛠️ **Log Maintenance Records**  
  One-click maintenance logging that updates the last maintenance date.

- 🌐 **Attractive UI with Background Images**  
  Fully responsive and visually enhanced with background imagery.

- 🔐 **Optional Role-based Access (Can be added)**  
  Future enhancement: login system for authorized users only.

---

## 🧑‍💻 Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript  
- **Backend**: Python (Flask)  
- **Database**: MySQL

---

## 🧩 Project Structure

```

factory\_maintenance\_system/
├── app.py
├── templates/
│   ├── index.html
│   ├── add\_machine.html
│   └── log\_maintenance.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│       └── background.jpg
├── database/
│   └── init\_db.sql
└── README.md

````

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/factory-maintenance-tracker.git
cd factory-maintenance-tracker
````

### 2. Install Dependencies

Make sure you have Python and pip installed.

```bash
pip install flask mysql-connector-python
```

### 3. Setup MySQL Database

* Open MySQL Workbench or CLI and run:

```sql
SOURCE database/init_db.sql;
```

* Or manually:

```sql
CREATE DATABASE maintenance_db;
USE maintenance_db;

CREATE TABLE machines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    last_maintenance DATE,
    frequency INT
);
```

### 4. Update `app.py` Database Credentials

```python
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sureshmd515",  # <-- Your MySQL password
    database="maintenance_db"
)
```

### 5. Run the App

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

---

## 💡 Future Improvements

* Add user login system for access control
* Store maintenance remarks in a separate log table
* Export reports as PDF or CSV
* Enable email notifications for due maintenance
* Add Japanese translation toggle for localization

---

## 📜 License

This project is open-source and free to use under the MIT License.

```
