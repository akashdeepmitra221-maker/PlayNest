"""
Flask Auth App
--------------
A simple full-stack login/signup system backed by MySQL (Community Server + Workbench).

Run:
    1. Create the database & table using schema.sql in MySQL Workbench (or `mysql < schema.sql`)
    2. Update config.py with your MySQL username/password
    3. pip install -r requirements.txt
    4. python app.py
    5. Visit http://127.0.0.1:5000
"""

from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from mysql.connector import Error
import re

import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY  # needed for session/flash messages


# ---------------------------------------------------------------------------
# Database helper
# ---------------------------------------------------------------------------
def get_db_connection():
    """Create and return a new MySQL connection using settings from config.py"""
    try:
        connection = mysql.connector.connect(
            host=config.MYSQL_HOST,
            user=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD,
            database=config.MYSQL_DB,
            port=config.MYSQL_PORT,
            ssl_verify_cert=True,
            ssl_ca=config.CA
        )
        return connection
    except Error as e:
        print(f"[DB ERROR] Could not connect to MySQL: {e}")
        return None


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.route("/")
def home():
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        full_name = request.form.get("full_name", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")
        u_type = request.form.get("type", "").strip()

        # ---- Server-side validation ----
        if not full_name or not email or not password or not confirm_password or not type :
            flash("Please fill in all fields.", "error")
            return redirect(url_for("signup"))

        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            flash("Please enter a valid email address.", "error")
            return redirect(url_for("signup"))

        if len(password) < 8:
            flash("Password must be at least 8 characters long.", "error")
            return redirect(url_for("signup"))

        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return redirect(url_for("signup"))

        connection = get_db_connection()
        if connection is None:
            flash("Could not connect to the database. Please try again later.", "error")
            return redirect(url_for("signup"))

        try:
            cursor = connection.cursor()

            # Check if email already exists
            cursor.execute("SELECT id FROM users WHERE email = %s", (email,))
            if cursor.fetchone():
                flash("An account with this email already exists.", "error")
                return redirect(url_for("signup"))

            # Hash the password before storing it -- never store plain text passwords
            hashed_password = generate_password_hash(password)

            cursor.execute(
                "INSERT INTO users (full_name, email, password, type) VALUES (%s, %s, %s, %s)",
                (full_name, email, hashed_password, u_type))
            connection.commit()

            flash("Account created successfully! Please log in.", "success")
            return redirect(url_for("login"))

        except Error as e:
            print(f"[DB ERROR] {e}")
            flash("Something went wrong while creating your account.", "error")
            return redirect(url_for("signup"))

        finally:
            cursor.close()
            connection.close()

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not email or not password:
            flash("Please enter both email and password.", "error")
            return redirect(url_for("login"))

        connection = get_db_connection()
        if connection is None:
            flash("Could not connect to the database. Please try again later.", "error")
            return redirect(url_for("login"))

        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()

            if user and check_password_hash(user["password"], password):
                session["user_id"] = user["id"]
                session["full_name"] = user["full_name"]
                session["type"] = user["type"]
                flash(f"Welcome back, {session['full_name']}!")
                if (session["type"]=="SOLO"):
                    return render_template("solo.html")
                else:
                    return render_template("team.html")

            else:
                flash("Invalid email or password.", "error")
                return redirect(url_for("login"))

        except Error as e:
            print(f"[DB ERROR] {e}")
            flash("Something went wrong while logging in.", "error")
            return redirect(url_for("login"))

        finally:
            cursor.close()
            connection.close()

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        flash("Please log in to view your dashboard.", "error")
        return redirect(url_for("login"))
    return render_template("dashboard.html", full_name=session.get("full_name"))


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
