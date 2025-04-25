from flask import Flask, render_template, request

app = Flask(__name__)

# Pamięć na wszystkie wiadomości (działa tylko do czasu restartu serwera)
messages = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        text = request.form.get("message")
        if name and text:
            messages.append(f"{name} says: {text}")
    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
