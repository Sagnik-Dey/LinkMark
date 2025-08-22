from flask import (
    Blueprint,
    render_template,
    request,
    session,
    redirect,
    url_for,
    flash
)
import sqlite3
import os

view_bp = Blueprint("view", __name__, template_folder="templates", url_prefix="/view")
@view_bp.route("/")
def view():
    db_path = os.path.join(os.path.dirname(__file__), 'static', 'databases', 'user-data.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    card_id = request.args.get("id")
    user_id = session.get("userId")
    table_name = f"LINKTABLE_{user_id}"
    if user_id == None:
        flash("Looks like you’ve already logged out.", "info")
        return redirect(url_for("landing.landing"))

    query = f"""--sql
    SELECT title, link, note FROM {table_name} WHERE id = {card_id}
    """
    cursor.execute(query)

    records = cursor.fetchall()
    record = records[0]
        
    return render_template("view.html", title=record[0], link=record[1], note=record[2])
