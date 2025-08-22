from flask import (
    Blueprint,
    render_template,
    session,
    request,
    redirect,
    url_for,
    flash
)
from datetime import datetime
import sqlite3
import os

def get_date():
    today = datetime.now()
    date_str = today.strftime("%d.%m.%y")
    
    return date_str

add_bp = Blueprint("add", __name__, template_folder="templates", url_prefix="/add")
@add_bp.route("/", methods=["GET", "POST"])
def add():
    db_path = os.path.join(os.path.dirname(__file__), 'static', 'databases', 'user-data.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    userId = session.get("userId")
    if userId == None:
        flash("Looks like you’ve already logged out.", "info")
        return redirect(url_for("landing.landing"))
    
    if request.method == "POST":
        
        title_input = request.form.get("title-input")
        link_input = request.form.get("link-input")
        note_input = request.form.get("note-input")
        date = get_date()
        
        table_name = f"LINKTABLE_{userId}"
        
        query = f"""--sql
        INSERT INTO {table_name} (title, link, note, date_) VALUES (?, ?, ?, ?) 
        """
        cursor.execute(query, (title_input, link_input, note_input, date))       

        connection.commit()
        connection.close()
        
        flash("Your link has been saved to your collection.", "success")
        return redirect(url_for("home.home"))
    
    connection.close()

    return render_template("add.html")