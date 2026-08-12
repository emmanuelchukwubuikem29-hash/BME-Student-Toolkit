from flask import Flask, render_template

app = Flask(__name__)

def mgdl_to_mmoll(value):
    # Standard clinical conversion factor for glucose.
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

@app.route("/convert")
def convert():
    return render_template("convert.html", result=None, error=None)

@app.route("/tasks")
def tasks():
    return "Tasks page coming next."

if __name__ == "__main__":
    app.run(debug=True)