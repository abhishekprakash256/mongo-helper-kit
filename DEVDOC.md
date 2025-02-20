### **📌 Development Documentation**

## **1. Requirements**
To set up and run this project, ensure you meet the following requirements:

- **MongoDB Installation**  
  - Install MongoDB **bare-metal** or run it using Docker:  
    ```bash
    # Run MongoDB in Docker (recommended)
    docker run -d --name mongo-db -p 27017:27017 mongo
    ```
  - Ensure the MongoDB server is running before testing or development.

- **MongoDB Connection Setup**
  - Configure the **MongoDB client** in `Helper_Fun` class:
    - Use `"localhost"` if running MongoDB **locally**.
    - Use `"mongo"` if running **inside Docker**.

- **Install Required Dependencies**
  ```bash
  pip install -r requirements.txt
  ```

---

## **2. Project Structure**
```
mongo-helper-kit/
├── mongo_helper_kit/
│   ├── __init__.py
│   ├── connection.py           # Handles MongoDB connections
│   ├── mongo_crud_operations.py # Provides CRUD operations
│   ├── utils.py                # Helper functions (e.g., logging, utility functions)
│   └── config.py               # Configuration management
├── tests/                      # Unit tests for each module
│   ├── test_connection.py      # Tests for MongoDB connection
│   ├── test_crud.py            # Tests for CRUD operations
├── examples/                   # Example usage scripts
├── requirements.txt            # Package dependencies
├── .github/workflows/          # CI/CD pipeline configuration
│   ├── ci.yml              # GitHub Actions for automated testing
└── README.md                   # Project documentation
```

---

## **3. Development & Branching Strategy**
This project follows a **structured Git workflow** with three main branch categories:  

### **🔹 `main` (Production)**
- The most **stable** branch containing **production-ready** code.  
- Only **tested and reviewed** changes are merged here.  
- **Deployment to production happens from `main`**.

### **🔹 `test` (Staging/Testing)**
- Used for **integration testing** before merging into `main`.  
- Acts as a **buffer** between `feature` branches and `main`.  
- **Continuous Integration (CI)** runs automated tests on this branch.  

### **🔹 `feature/*` (Feature Development)**
- Used for **new features, bug fixes, or improvements**.  
- **Naming Convention:**  
  - `feature/<feature-name>` (e.g., `feature/authentication`, `feature/api-refactor`)  
  - `bugfix/<bug-name>` (e.g., `bugfix/payment-error`)  
- Merged into `test` after development is complete.  

---

## **4. Git Workflow: Step-by-Step Guide**
### **🔹 Step 1: Creating a New Feature Branch**
Every new feature or bug fix starts from the latest `test` branch.

```bash
git checkout test
git pull origin test  # Ensure latest updates
git checkout -b feature/new-feature  # Create a new branch
```

Work on your feature, commit changes, and push to remote:

```bash
git add .
git commit -m "Added new feature: X"
git push origin feature/new-feature
```

---

### **🔹 Step 2: Merging Feature Branch into `test`**
Once development is complete, **create a Pull Request (PR)** from `feature/new-feature` → `test`.

- ✅ Ensure **all tests pass** before merging.
- ✅ Conduct **code reviews** for quality control.

If everything is fine, **merge into `test`**:

```bash
git checkout test
git pull origin test
git merge feature/new-feature
git push origin test
```

After merging, delete the feature branch:

```bash
git branch -d feature/new-feature
git push origin --delete feature/new-feature
```

---

### **🔹 Step 3: Merging `test` into `main`**
After multiple features are tested in `test`, merge into `main` for release.

```bash
git checkout main
git pull origin main
git merge test
git push origin main
```

🚀 **Deploy the `main` branch to production after merging!**

---

## **5. Best Practices for Git Workflow**
✅ **Keep `main` clean** → Never push directly to `main`; always merge from `test`.  
✅ **Frequent sync** → Regularly update `feature` branches from `test` to prevent merge conflicts.  
✅ **Use descriptive branch names** → Example: `feature/user-auth`, `bugfix/payment-error`.  
✅ **Delete merged branches** → Keep the repository clean by removing feature branches after merging.  
✅ **Code reviews & CI/CD** → Run automated tests on `test` before merging into `main`.  

---

## **6. Example Git Workflow**
```bash
# Create and work on a feature branch
git checkout test
git pull origin test
git checkout -b feature/new-api

# Work on code...
git add .
git commit -m "Implemented new API feature"
git push origin feature/new-api

# Merge into test after review
git checkout test
git pull origin test
git merge feature/new-api
git push origin test

# Merge tested code into main
git checkout main
git pull origin main
git merge test
git push origin main
```

---

## **7. Running Tests with Pytest**
To run **unit tests** locally:
```bash
pytest --maxfail=5 --disable-warnings -v
```
- **`--maxfail=5`** → Stops execution after **5 failures**.  
- **`--disable-warnings`** → Suppresses warnings for cleaner output.  
- **`-v`** → Enables **verbose output** for better debugging.  

---

## **8. Automated Testing with GitHub Actions**
The project uses **GitHub Actions** to run tests on every push or pull request.

### **📌 GitHub Actions Workflow (`.github/workflows/ci.yml`)**
```yaml
name: Run Pytest

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
      - test

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'  # Change to match your project

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run pytest
        run: pytest --maxfail=5 --disable-warnings -v
```

🚀 **Now, every commit gets tested automatically!**  

---

## **9. Deployment Strategy**
- **Staging (`test`)**: Run CI/CD tests before merging to `main`.  
- **Production (`main`)**: After merging from `test`, deploy the latest stable code.  

---

### **📌 Summary**
✅ **Structured Git workflow** with `main`, `test`, and `feature` branches.  
✅ **Automated testing** with `pytest` and GitHub Actions.  
✅ **Best practices** for feature development, merging, and deployment.  
✅ **Easy setup** with MongoDB (bare-metal or Docker).  

