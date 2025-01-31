

# Fam-Auth

Fam-Auth is a modular authentication package designed for FastAPI. It provides essential authentication functionality for users, along with optional features for OTP (One-Time Password) and role-based access control.

## Features

- **User Authentication**: Basic functionality to authenticate users with their credentials.
- **OTP Authentication**: Optional feature to enhance security with OTP support for user login.
- **Role-based Access Control**: Optional feature that enables role assignments and enforces permissions based on roles.

## Installation

You can install Fam-Auth using [Poetry](https://python-poetry.org/) or by using pip:

### Using Poetry

```bash
poetry add fam-auth
```

### Using pip

```bash
pip install fam-auth
```

## Quick Start

### 1. Import the Module

In your FastAPI application, import and initialize the Fam-Auth package:

```python
from fam_auth import init_auth
from fastapi import FastAPI

app = FastAPI()

# Initialize Fam-Auth
init_auth(app)
```

### 2. Add User Authentication

To set up basic user authentication, you can define your user model and use the authentication methods provided by Fam-Auth.

### 3. Enable OTP (Optional)

Enable OTP for additional security by including the `otp` feature in your FastAPI app:

```python
from fam_auth import otp
otp.enable(app)
```

### 4. Enable Role-based Access (Optional)

If your application needs roles for user access control, enable the role feature:

```python
from fam_auth import role
role.enable(app)
```

## Configuration

Fam-Auth uses a modular approach, which allows you to configure various authentication settings via the `settings.py` file. You can enable or disable OTP and role features based on your requirements.

### Example Configuration:

```python
# settings.py
OTP_ENABLED = True
ROLE_ENABLED = True
```

## Contributing

If you want to contribute to Fam-Auth, please fork the repository and submit a pull request. We welcome bug fixes, features, and documentation improvements.
