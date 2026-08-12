from flask import Flask, render_template, request
import json

TASKS_FILE = "tasks_data.json"

def load_tasks():
    # Opens the JSON file and turns it back into a Python list of dicts.
    # If the file doesn't exist yet, start with an empty list instead of crashing.
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

        except (TypeError, ValueError):
            error = "Please enter valid numbers in all fields."

    return render_template("convert.html", result=result, error=error)

@app.route("/tasks")
def tasks():
    all_tasks = load_tasks()
    return render_template("tasks.html", tasks=all_tasks)

if __name__ == "__main__":
    app.run(debug=True)