from flask import Flask, render_template, request, redirect

app = Flask(__name__)

shopping_list = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        item = request.form.get("item")
        if item:
            shopping_list.append(item)
        return redirect("/")
    return render_template("index.html", items=shopping_list)

if __name__ == "__main__":
    app.run(debug=True)
