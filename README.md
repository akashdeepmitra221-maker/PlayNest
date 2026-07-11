# Flask Login / Signup App (MySQL)

A full-stack authentication system: HTML/CSS/JS front end + Flask back end + MySQL storage.

## 1. Set up the database

Open **MySQL Workbench**, connect to your local server, open `schema.sql`, and run it
(lightning-bolt icon). This creates:

- Database: `auth_app_db`
- Table: `users` (id, full_name, email, password (hashed), created_at)

Or from a terminal:
```bash
mysql -u root -p < schema.sql
```

## 2. Configure credentials

Open `config.py` and update:
```python
MYSQL_USER = "root"
MYSQL_PASSWORD = "your_password"   # <-- your actual MySQL password
```
Change `SECRET_KEY` to any random string (used to sign session cookies).

## 3. Install dependencies

It's best to use a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS/Linux

pip install -r requirements.txt
```

## 4. Run the app

```bash
python app.py
```

Visit **http://127.0.0.1:5000** — you'll land on the login page.
Click "Create an account" to sign up first, then log in.

## How it works

- **Frontend**: `templates/*.html` (Jinja2) + `static/css/style.css` + `static/js/script.js`
  for lightweight client-side validation (password match, empty-field checks).
- **Backend**: `app.py` — Flask routes for `/signup`, `/login`, `/dashboard`, `/logout`.
- **Database**: `mysql-connector-python` talks to your local MySQL server. Passwords are
  hashed with Werkzeug's `generate_password_hash` before being stored — never stored in plain text.
- **Sessions**: Flask's built-in signed-cookie sessions track the logged-in user; `/dashboard`
  redirects to `/login` if there's no active session.

## Project structure

```
flask_auth_app/
├── app.py              # Flask routes + MySQL logic
├── config.py           # DB credentials + secret key
├── schema.sql          # Run this in MySQL Workbench first
├── requirements.txt
├── templates/
│   ├── login.html
│   ├── signup.html
│   └── dashboard.html
└── static/
    ├── css/style.css
    └── js/script.js
```

## Common issues

- **`Access denied for user 'root'@'localhost'`** → wrong password in `config.py`.
- **`Unknown database 'auth_app_db'`** → run `schema.sql` first.
- **`ModuleNotFoundError: mysql`** → run `pip install -r requirements.txt` inside your active virtual environment.
