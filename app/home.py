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

home_bp = Blueprint("home", __name__, template_folder="templates", url_prefix="/home")

def get_date():
    today = datetime.now()
    date_str = today.strftime("%d.%m.%y")
    
    return date_str

@home_bp.route("/")
def home():
    date = get_date()
    
    db_path = os.path.join(os.path.dirname(__file__), 'static', 'databases', 'user-data.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    user_id = session.get('userId')
    table_name = f"LINKTABLE_{user_id}"
    
    if user_id == None:
        flash("Looks like you’ve already logged out.", "info")
        return redirect(url_for("landing.landing"))
    
    query = f"""--sql
    SELECT id, title, date_ FROM {table_name};
    """

    cursor.execute(query)
    records = cursor.fetchall() if table_name else []

    name = session.get("name")
    connection.close()

    return render_template("home.html", date=date, records=records, name=name)

@home_bp.route("/logout")
def logout():
    session.clear()
    
    flash("Logged out. We’ll keep things ready for your return!", "success")
    return redirect(url_for("landing.landing"))