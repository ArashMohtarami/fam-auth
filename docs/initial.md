## 1. **Project Overview**

### Purpose:
- You are setting up a FastAPI project with a modular architecture where each part of your project (e.g., database, models, repositories, etc.) is clearly organized in the `src` directory.
- This modular design will allow you to scale your project over time and reuse components in other projects if needed.

### Key Decisions:
- **Using `src/` for your code**: This avoids issues where Python accidentally picks up test files, configuration files, or other non-package files from the project root directory. This is a widely adopted convention that separates code from other files like `migrations`, `poetry.lock`, and `pyproject.toml`.

---

## 2. **Folder Structure Breakdown**

Here's an explanation of each folder/file in your proposed structure:

```text
.
├── migrations           # Alembic migrations for database schema changes
├── poetry.lock          # Locked dependencies
├── pyproject.toml       # Project metadata and Poetry configuration
└── src                  # Your main project code
    ├── core             # Core business logic (database, settings, routers)
    │   ├── database.py  # Database connection setup (SQLAlchemy)
    │   ├── __init__.py  # Marks the directory as a package
    │   ├── routers.py   # FastAPI routers for different endpoints
    │   └── settings.py  # Configuration and settings for the app
    ├── dependencies.py  # External dependencies (e.g., shared utilities)
    ├── exceptions.py    # Custom exception classes
    ├── __init__.py      # Marks the directory as a package
    ├── main.py          # FastAPI app initialization and main entry point
    ├── models           # Database models
    │   ├── __init__.py  # Marks the directory as a package
    ├── repository       # Data access layer (managers, queries)
    │   ├── data_access  # Data access modules (queries, business logic)
    │   │   ├── managers # Business logic for interacting with the database
    │   │   └── queries  # Raw SQL queries or query functions
    │   └── __init__.py   # Marks the directory as a package
    ├── routers           # FastAPI routers for modular endpoints
    │   └── __init__.py  # Marks the directory as a package
    └── schemas           # Pydantic models (validation and serialization)
        └── __init__.py  # Marks the directory as a package
```

### **Why `src`?**
- **Isolation of Code**: By using a `src` directory, you're isolating your project code from other files like configuration, virtual environments, and build artifacts. This is a common Python packaging best practice, and it ensures that only the code intended to be packaged is included.
- **Clarity in Imports**: When using `src`, Python will know exactly where to look for your package files, even if the root directory contains other non-package files.
- **Avoid Name Conflicts**: If you don’t use `src`, Python might inadvertently import files that share names with Python standard libraries or third-party packages, causing name conflicts.

---

## 3. **Configuration Files**

### **`pyproject.toml`**:
This is the main configuration file for Poetry. Here's an example of how it would be set up:

```toml
[tool.poetry]
name = "fam-auth"
version = "0.1.0"
description = "A modular authentication package for FastAPI with optional OTP and role features."
authors = ["Arash Mohtarami <arashmohtarami.aa@gmail.com>"]
license = "MIT"
readme = "README.md"
packages = [{ path = "src" }]  # Ensures the code from src is included in the distribution

[tool.poetry.dependencies]
python = "^3.11"
psycopg2-binary = "^2.9.10"
sqlalchemy = "^2.0.37"
alembic = "^1.14.1"
fastapi = "^0.115.8"
uvicorn = "^0.34.0"
pydantic-settings = "^2.7.1"

[tool.poetry.dev-dependencies]
pytest = "^7.0"
black = "^23.0"
flake8 = "^6.0"

[tool.poetry.extras]
otp = ["otp"]
role = ["role"]

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"
```

### **`poetry.lock`**:
Poetry automatically manages this file to lock your dependencies to a specific version. It ensures that anyone who installs the package will get the exact same version of the dependencies.

---

## 4. **Creating a Modular FastAPI Project**

- **Core (`src/core`)**: Contains the central components of your FastAPI application:
  - `database.py`: Handles the connection and configuration of the database (e.g., SQLAlchemy).
  - `routers.py`: Contains FastAPI routes and the logic for handling requests.
  - `settings.py`: Stores environment variables and configuration settings.
  
- **Models (`src/models`)**: This folder will contain your SQLAlchemy models. Each model represents a table in the database.

- **Repository Layer (`src/repository`)**: The repository pattern abstracts data access logic. You can have:
  - **Managers**: Contains business logic related to models (e.g., adding new users).
  - **Queries**: Contains functions that execute specific database queries.

- **Schemas (`src/schemas`)**: Pydantic models used for data validation, serialization, and request/response handling.

- **Routers (`src/routers`)**: Organize your routes into logical sections (e.g., auth, users, etc.).

---

## 5. **Alembic Migrations**

- **`migrations` Folder**: This folder will store your Alembic migration files, which are responsible for tracking and applying database schema changes over time.
- When setting up Alembic, make sure to configure it to connect to your database (in `database.py`) and use the models for schema migrations.

---

## 6. **How to Create This Structure**

1. **Set up your Python environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Linux or macOS
   venv\Scripts\activate  # On Windows
   ```

2. **Install Poetry**:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Create a new Poetry project**:
   ```bash
   poetry new fam-auth --src
   cd fam-auth
   ```

4. **Set up the structure**:
   Create directories (`core`, `models`, `repository`, `schemas`, etc.) under `src/`, and move your existing Python files into these directories.

5. **Configure `pyproject.toml`**: Update the `pyproject.toml` file to include your dependencies, `src` path, and extras (like OTP and role).

---

## 7. **Final Thoughts**

By organizing your project in this way, you ensure that it remains modular, scalable, and easy to maintain. Each component is clearly separated into its domain, allowing for easier testing, reuse, and integration of new features over time.

This setup also follows Python packaging best practices, making it easier for others to contribute and use your project.
