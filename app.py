from flask import Flask, render_template, request, redirect

app = Flask(__name__)

shopping_list = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        item = request.form.get("item")
        if item:
            shopping_list.append({"name": item, "done": False})
        return redirect("/")
    return render_template("index.html", items=shopping_list)

@app.route("/delete/<int:index>") #Usuwanie pozycji z listy
def delete(index):
    shopping_list.pop(index)
    return redirect("/")

@app.route("/toggle/<int:index>") #Oznaczanie jako kupione (checkbox)
def toggle(index):
    shopping_list[index]["done"] = not shopping_list[index]["done"]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)