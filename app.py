from flask import Flask, render_template, request, redirect, url_for
import json

TASKS_FILE = "tasks_data.json"

def load_tasks() -> list:
    try:
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    # Takes our Python list and writes it back to disk as JSON.
    # indent=2 just makes the file human-readable if you open it directly.
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


app = Flask(__name__)

def mgdl_to_mmoll(value):
    return value / 18.0

def mmoll_to_mgdl(value):
    return value * 18.0

def dosage_by_weight(dose_per_kg, weight_kg):
    return dose_per_kg * weight_kg

def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def cm_to_inches(cm):
    return cm / 2.54

def inches_to_cm(inches):
    return inches * 2.54

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
    
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/convert", methods=["GET", "POST"])
def convert():
    result = None
    error = None

    if request.method == "POST":
        conversion_type = request.form.get("conversion_type")

        try:
            if conversion_type == "mgdl_to_mmoll":
                value = float(request.form.get("value"))
                result = f"{mgdl_to_mmoll(value):.2f} mmol/L"

            elif conversion_type == "mmoll_to_mgdl":
                value = float(request.form.get("value"))
                result = f"{mmoll_to_mgdl(value):.2f} mg/dL"

            elif conversion_type == "dosage":
                dose_per_kg = float(request.form.get("dose_per_kg"))
                weight_kg = float(request.form.get("weight_kg"))
                result = f"{dosage_by_weight(dose_per_kg, weight_kg):.2f} mg total dose"

            elif conversion_type == "bmi":
                weight_kg = float(request.form.get("weight_kg_bmi"))
                height_m = float(request.form.get("height_m"))
                bmi_value = calculate_bmi(weight_kg, height_m)
                result = f"BMI: {bmi_value:.1f}"
            
            elif conversion_type == "cm_to_in":
                value = float(request.form.get("height_value"))
                result = f"{cm_to_inches(value):.2f} inches"

            elif conversion_type == "in_to_cm":
                value = float(request.form.get("height_value"))
                result = f"{inches_to_cm(value):.2f} cm"

            elif conversion_type == "c_to_f":
                value = float(request.form.get("temp_value"))
                result = f"{celsius_to_fahrenheit(value):.1f} °F"

            elif conversion_type == "f_to_c":
                value = float(request.form.get("temp_value"))
                result = f"{fahrenheit_to_celsius(value):.1f} °C"
            
        except (TypeError, ValueError):
            error = "Please enter valid numbers in all fields."

    return render_template("convert.html", result=result, error=error)

@app.route("/tasks", methods=["GET", "POST"])
def tasks():
    if request.method == "POST":
        new_task = {
            "title": request.form.get("title"),
            "assignee": request.form.get("assignee"),
            "deadline": request.form.get("deadline"),
            "done": False,
        }
        all_tasks = load_tasks()
        all_tasks.append(new_task)
        save_tasks(all_tasks)

    all_tasks = load_tasks()
    return render_template("tasks.html", tasks=all_tasks)

@app.route("/tasks/toggle/<int:task_index>", methods=["POST"])
def toggle_task(task_index):
    all_tasks = load_tasks()
    if 0 <= task_index < len(all_tasks):
        all_tasks[task_index]["done"] = not all_tasks[task_index]["done"]
        save_tasks(all_tasks)
    return redirect(url_for("tasks"))

@app.route("/tasks/delete/<int:task_index>", methods=["POST"])
def delete_task(task_index):
    all_tasks = load_tasks()
    if 0 <= task_index < len(all_tasks):
        all_tasks.pop(task_index)
        save_tasks(all_tasks)
    return redirect(url_for("tasks"))

@app.route("/tasks/edit/<int:task_index>", methods=["GET", "POST"])
def edit_task(task_index):
    all_tasks = load_tasks()

    if not (0 <= task_index < len(all_tasks)):
        return redirect(url_for("tasks"))

    if request.method == "POST":
        all_tasks[task_index]["title"] = request.form.get("title")
        all_tasks[task_index]["assignee"] = request.form.get("assignee")
        all_tasks[task_index]["deadline"] = request.form.get("deadline")
        save_tasks(all_tasks)
        return redirect(url_for("tasks"))

    # GET request: show the edit form, pre-filled with current values
    task = all_tasks[task_index]
    return render_template("edit_task.html", task=task, task_index=task_index)
    
if __name__ == "__main__":
    app.run(debug=True)