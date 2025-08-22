from flask import (
    render_template,
    Blueprint,
    session,
    flash,
    redirect,
    url_for
)

landing_bp = Blueprint("landing", __name__, template_folder="templates", url_prefix="/")
@landing_bp.route("/")
def landing():
    userId = session.get("userId") 
    
    if userId:
        flash("Looks like you’re already signed in — continue exploring!", "info")
        return redirect(url_for("home.home"))
    
    return render_template("landing.html")