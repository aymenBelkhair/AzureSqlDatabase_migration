
## 📄 Project Structure
```
EmploiPublic‑Solution/
├── app/
│   ├── __init__.py
│   ├── db.py
    ├── modules.py
│   └── settings.py
├── run.py
├── requirements.txt
└── .gitignore
```

## ✨ Overview
# AzureSqlDatabase_migration
A data migration project using Python to transfer data from local files such as .xlsx and .csv into an Azure SQL Database. The solution ensures clean, structured import and supports large datasets efficiently.


## 🔧 Prerequisites
- **Python 3.10**
- Pip (included with Python)

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aymenBelkhair/EmploiPublic-Solution.git
   cd EmploiPublic-Solution
   ```

2. (Optional but recommended) Set up a virtual environment:
   ```bash
   py-3.10 -m venv venv
   source venv/bin/activate   # macOS/Linux
   .\venv\Scripts\activate    # Windows
   py -m pip install -U pip setuptools     
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Usage
Be sure to create the file  app/settings.py :
```bash
mkdir app/settings.py
```
This file containes all neccesary parameter to get login to the database (DB_SERVER,DB_DATABASE,DB_USERNAME,DB_PASSWORD)

Run the main script:

```bash
python run.py
```

This may:
- Start a web service or background process
- Fetch data from external sources
- Perform data processing
- Export results to console or file


## 📝 Contribution

Contributions are welcome! To contribute:

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/YourFeatureName`
3. Commit your changes: `git commit -m "Add feature X"`
4. Push branch: `git push origin feature/YourFeatureName`
5. Open a pull request describing your changes

## 📄 License

MIT License  
© 2025 Aymen Belkhair

## ✅ Summary of Steps

| Step | Command |
|------|---------|
| Clone repository | `git clone …` |
| Create virtual environment | `py -3.10 -m venv venv` |
| Install dependencies | `pip install -r requirements.txt` |
| Run the app | `python run.py` |


