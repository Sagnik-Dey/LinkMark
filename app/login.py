from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)
import sqlite3
import os

login_bp = Blueprint("login", __name__, template_folder="templates", url_prefix="/login")
@login_bp.route("/", methods=["GET", "POST"])
def login():
    db_path = os.path.join(os.path.dirname(__file__), 'static', 'databases', 'user-data.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    if request.method == "POST":
        username = request.form.get("username-input")
        password = request.form.get("password-input")
        
        query = """--sql
        SELECT 1 FROM users WHERE username = ? LIMIT 1;
        """
        
        cursor.execute(query, (username,))
        user_exists = cursor.fetchone()
        if not user_exists:
            flash("User not found. Please check and try again.", "warning")
            return redirect(url_for("login.login"))

        query = """--sql
        SELECT password FROM users WHERE username = ? LIMIT 1;
        """
        
        cursor.execute(query, (username,))
        stored_password = cursor.fetchone()
        
        if not stored_password or stored_password[0] != password:
            flash("Looks like the password doesn’t match. Please re-enter.", "error")
            return redirect(url_for("login.login"))
        
        query = """--sql
        SELECT name FROM users WHERE username = ? LIMIT 1;
        """
        
        cursor.execute(query, (username,))
        name = cursor.fetchone()
        session['name'] = name[0] if name else "Guest"
        
        query = """--sql
        SELECT id FROM users WHERE username = ?;
        """
        cursor.execute(query, (username,))
        user_id = cursor.fetchone()
        
        id = user_id[0] if user_id else None
        session['userId'] = id
        
        flash("Login successful. Good to see you again!", "success")
        return redirect(url_for("home.home"))
    
    connection.close()
    
    return render_template("login.html")