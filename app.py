from flask import Flask, render_template, request, redirect, session, jsonify
import sqlite3

from database.database import init_db
from code_executor.code_executor import run_code

from tutor import (
    explain_concept,
    generate_practice,
    chat_with_tutor,
    generate_roadmap,
    generate_task
)

app = Flask(__name__)
app.secret_key = "secret123"

init_db()


def log_usage(user, feature):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO usage(user_id,feature) VALUES (?,?)",
        (user, feature)
    )

    cur.execute(
        "UPDATE users SET points = points + 10 WHERE id=?",
        (user,)
    )

    conn.commit()
    conn.close()


@app.route("/")
def home():

    if "user" not in session:
        return redirect("/login")

    return render_template("index.html")


@app.route("/dashboard")
def dashboard():

    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT feature,COUNT(*) FROM usage WHERE user_id=? GROUP BY feature",
        (session["user"],)
    )

    stats = cur.fetchall()

    cur.execute(
        "SELECT points,streak FROM users WHERE id=?",
        (session["user"],)
    )

    user = cur.fetchone()

    conn.close()

    return render_template(
        "dashboard.html",
        stats=stats,
        points=user[0],
        streak=user[1]
    )


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO users(username,email,password) VALUES(?,?,?)",
            (username, email, password)
        )

        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("database.db")
        cur = conn.cursor()

        cur.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )

        user = cur.fetchone()
        conn.close()

        if user:
            session["user"] = user[0]
            return redirect("/dashboard")

    return render_template("login.html")


@app.route("/logout")
def logout():

    session.clear()
    return redirect("/login")


@app.route("/editor")
def editor():
    return render_template("editor.html")


@app.route("/run_code", methods=["POST"])
def execute():

    code = request.json["code"]
    output = run_code(code)

    return jsonify({"output": output})


# AI FEATURES

@app.route("/explain", methods=["POST"])
def explain():

    concept = request.json["concept"]
    level = request.json["level"]

    result = explain_concept(concept, level)

    log_usage(session["user"], "explain")

    return jsonify({"result": result})


@app.route("/practice", methods=["POST"])
def practice():

    concept = request.json["concept"]
    level = request.json["level"]

    result = generate_practice(concept, level)

    log_usage(session["user"], "practice")

    return jsonify({"result": result})


@app.route("/task", methods=["POST"])
def task():

    concept = request.json["concept"]
    level = request.json["level"]

    result = generate_task(concept, level)

    log_usage(session["user"], "task")

    return jsonify({"result": result})


@app.route("/roadmap", methods=["POST"])
def roadmap():

    topic = request.json["topic"]

    result = generate_roadmap(topic)

    log_usage(session["user"], "roadmap")

    return jsonify({"result": result})


@app.route("/chat", methods=["POST"])
def chat():

    question = request.json["question"]

    result = chat_with_tutor(question)

    log_usage(session["user"], "chat")

    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)