from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from io import BytesIO
from fpdf import FPDF
from main import (
    calculate_bmi,
    health_risk,
    workout_plan,
    diet_plan,
    timeframe_suggestion,
    generate_4_week_daily_plan
)

app = Flask(__name__)
CORS(app)  # enable cross-origin requests for frontend

# ----------------- API ENDPOINTS -----------------

@app.route("/api/recommend", methods=["POST"])
def recommend():
    """Return AI healthcare & fitness recommendations."""
    data = request.json

    age = data.get("age")
    gender = data.get("gender")
    weight = float(data.get("weight"))
    height = float(data.get("height"))
    goal = data.get("goal")
    activity_level = data.get("activity_level")

    # Core AI logic from main.py
    bmi = calculate_bmi(weight, height)
    risk = health_risk(bmi)
    workout = workout_plan(goal, activity_level)
    diet = diet_plan(goal)
    timeframe = timeframe_suggestion(goal)
    plan = generate_4_week_daily_plan(goal)

    return jsonify({
        "bmi": bmi,
        "risk": risk,
        "workout": workout,
        "diet": diet,
        "timeframe": timeframe,
        "plan": plan
    })


@app.route("/api/report", methods=["POST"])
def report():
    """Generate a PDF report and send it to the user."""
    data = request.json

    age = data.get("age")
    gender = data.get("gender")
    weight = float(data.get("weight"))
    height = float(data.get("height"))
    goal = data.get("goal")
    activity_level = data.get("activity_level")

    # Core AI logic
    bmi = calculate_bmi(weight, height)
    risk = health_risk(bmi)
    workout = workout_plan(goal, activity_level)
    diet = diet_plan(goal)
    timeframe = timeframe_suggestion(goal)
    plan = generate_4_week_daily_plan(goal)

    # -------- Create PDF --------
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="AI Healthcare & Fitness Report", ln=True, align="C")
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Age: {age} | Gender: {gender}", ln=True)
    pdf.cell(200, 10, txt=f"Weight: {weight} kg | Height: {height} cm", ln=True)
    pdf.cell(200, 10, txt=f"Goal: {goal} | Activity Level: {activity_level}", ln=True)
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"BMI: {bmi} ({risk})", ln=True)
    pdf.cell(200, 10, txt=f"Workout Plan: {workout}", ln=True)
    pdf.cell(200, 10, txt=f"Timeframe Suggestion: {timeframe}", ln=True)
    pdf.ln(10)

    pdf.cell(200, 10, txt="Diet Plan:", ln=True)
    for meal, food in diet.items():
        pdf.multi_cell(0, 10, f"{meal}: {food}")
    pdf.ln(10)

    pdf.cell(200, 10, txt="4-Week Daily Plan (Overview):", ln=True)
    for week, days in plan.items():
        pdf.cell(200, 10, txt=f"{week}:", ln=True)
        for day, activity in days.items():
            pdf.multi_cell(0, 10, f"   {day}: {activity}")
        pdf.ln(5)

    # -------- Fix: Save properly to memory --------
    pdf_bytes = BytesIO()
    pdf.output(pdf_bytes, 'S').encode('latin1')
    pdf_bytes.seek(0)

    return send_file(
        pdf_bytes,
        as_attachment=True,
        download_name="health_fitness_report.pdf",
        mimetype="application/pdf"
    )

# ----------------- RUN SERVER -----------------
if __name__ == "__main__":
    app.run(debug=True)
