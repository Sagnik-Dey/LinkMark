from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)
import os
import sqlite3

register_bp = Blueprint("register", __name__, template_folder="templates", url_prefix="/register")
@register_bp.route("/", methods=["GET", "POST"])
def register():
    db_path = os.path.join(os.path.dirname(__file__), 'static', 'databases', 'user-data.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    if request.method == "POST":
        username: str = request.form.get("username-input")
        name: str = request.form.get("name-input")
        password: str = request.form.get("password-input")

        query = """--sql
        SELECT username FROM users WHERE username = ?;
        """
        cursor.execute(query, (username,))
        existing_user = cursor.fetchone()
        
        if existing_user:
            flash("This username is unavailable. Maybe add your initials or numbers?")
            return redirect(url_for("register.register"))
        
        query = """--sql
        INSERT INTO users (username, name, password) VALUES (?, ?, ?);
        """

        cursor.execute(query, (username, name, password))
        
        query = """--sql
        SELECT id FROM users WHERE username = ?;
        """
        cursor.execute(query, (username,))
        user_id = cursor.fetchone()
        id = user_id[0] if user_id else None

        session["userId"] = id
        session["name"] = name
        
        table_name = f"LINKTABLE_{id}"
        query = f"""--sql
                    CREATE TABLE IF NOT EXISTS {table_name} (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        link TEXT NOT NULL,
                        note TEXT NOT NULL,
                        date_ TEXT NOT NULL        
                    );
        """
                
        cursor.execute(query)

        connection.commit()
        connection.close()
        
        flash("Your new account is ready. Welcome aboard!", "success")
        return redirect(url_for("home.home"))
    
    return render_template("register.html")