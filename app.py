from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

def save():
    with open("data.json", "w") as f:
        json.dump(shopping_list, f)

def load():
    global shopping_list
    if os.path.exists("data.json"):
        with open("data.json", "r") as f:
            shopping_list = json.load(f)
    else:
        shopping_list = []

load()  # wczytaj przy starcie

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        item = request.form.get("item")
        category = request.form.get("category")
        if item:
            shopping_list.append({"name": item, "category": category, "done": False})
            save()
        return redirect("/")
    return render_template("index.html", items=shopping_list)

@app.route("/delete/<int:index>") #Usuwanie pozycji z listy
def delete(index):
    shopping_list.pop(index)
    save()
    return redirect("/")

@app.route("/toggle/<int:index>") #Oznaczanie jako kupione (checkbox)
def toggle(index):
    shopping_list[index]["done"] = not shopping_list[index]["done"]
    save()
    return redirect("/")

# Edycja pozycji
@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    item = shopping_list[index]
    if request.method == "POST":
        new_name = request.form.get("item")
        new_category = request.form.get("category")
        if new_name:
            shopping_list[index]["name"] = new_name
            shopping_list[index]["category"] = new_category
        return redirect("/")
    return render_template("edit.html", item=item, index=index)

if __name__ == "__main__":
    app.run(debug=True)