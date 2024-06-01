from flask import Flask, render_template, session, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Mock user data (replace with actual user data)
user_data = {
    "username": "user1",
    "total_data_collected": {
        "cookies": 100,
        "device_info": 50,
        "user_data": 200
    },
    "tracking_metrics": {
        "tracking_cookies": 20,
        "device_fingerprinting": "High",
        "data_sharing": "Moderate"
    },
    "privacy_score": 75,  # out of 100
    "privacy_recommendations": [
        "Enable browser's Do Not Track (DNT) feature.",
        "Use a reputable VPN for anonymous browsing."
    ]
}

@app.route("/")
def index():
    if "username" in session:
        return render_template("dashboard.html", user=user_data)
    return redirect(url_for("login"))

@app.route("/login")
def login():
    session["username"] = user_data["username"]
    flash("Login successful!", "success")
    return redirect(url_for("index"))

@app.route("/logout")
def logout():
    session.pop("username", None)
    flash("Logged out successfully!", "success")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
