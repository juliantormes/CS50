import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    # Initialize an error message variable
    error_message = None

    if request.method == "POST":
        # Validate submission
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        if not name or not month or not day:
            error_message = "Name, month, or day cannot be empty!"
        elif int(month) not in range(1, 13) or int(day) not in range(1, 32):
            error_message = "Invalid month or day!"
        else:
            db.execute(
                "INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)",
                name,
                month,
                day,
            )
            return redirect("/")

    # This part is executed for both "GET" requests and "POST" requests with errors
    birthdays = db.execute("SELECT name, month, day FROM birthdays")
    return render_template("index.html", birthdays=birthdays, error=error_message)