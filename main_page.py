import mysql.connector
from flask import Flask, render_template, request

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="myntra"
)

app = Flask(_name_, template_folder="D:/OneDrive/Mukta_OneDrive/Mukta_exploration/Myntra_2024/Database/templates")

# Create a database cursor
database = mydb
mycursor = database.cursor()

@app.route('/')
def login_page():
    return render_template("login.html")

@app.route("/form_login", methods=["POST"])
def login():
    user = request.form["username"]
    pwd = request.form["password"]

    # Check if user exists
    mycursor.execute("SELECT password FROM users WHERE username=%s", (user,))
    result = mycursor.fetchone()

    if result:
        stored_pass = result[0]
        if stored_pass != pwd:
            # Debugging statement
            print(f"Invalid password for user: {user}")
            return render_template("login.html", info="Invalid Password")
        else:
            # Debugging statement
            print(f"User {user} logged in successfully.")
            return render_template("home8.html")
    else:
        # Debugging statement
        print(f"User not found: {user}")
        return render_template("login.html", info="User not found")
@app.route('/aesthetic')
def aesthetic_page():
	return render_template("aesthetic8.html")

@app.route('/lead6.html')
def lead_page():
	return render_template("lead6.html")

@app.route('/profile.html')
def profile_page():
	return render_template("profile1.html")

@app.route('/index.html')
def build_aesthetic():
        return render_template("index.html")

if _name_ == "_main_":
    app.run(debug=True, port=5002, use_reloader=False)
