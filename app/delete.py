from flask import (
    Blueprint,
    redirect,
    url_for,
    request,
    session,
    flash
)
import sqlite3
import os

delete_bp = Blueprint("delete", __name__, template_folder="templates", url_prefix="/delete")
@delete_bp.route("/")
def delete():
    db_path = os.path.join(os.path.dirname(__file__), 'static', 'databases', 'user-data.db')
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    
    user_id = session.get("userId")
    table_name = f"LINKTABLE_{user_id}"
    card_id = request.args.get("id")

    query = f"""--sql
    DELETE FROM {table_name} WHERE id = {card_id}
    """
    
    cursor.execute(query)
    connection.commit()

    connection.close()

    flash("Done! That one won’t bug you anymore.", "success")
    return redirect(url_for("home.home"))