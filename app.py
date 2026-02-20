from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Function to generate 7-day fitness plan
def generate_fitness_plan(age, gender, goal, preference, time):
    goal_lower = goal.lower()

    if "weight" in goal_lower:
        plan = {
            "Day 1": "30 mins brisk walking + light stretching",
            "Day 2": f"{time} mins cardio + 15 mins core workout",
            "Day 3": "HIIT workout (20 mins)",
            "Day 4": "Yoga + 30 mins jogging",
            "Day 5": "Full body strength training",
            "Day 6": "Cycling or skipping",
            "Day 7": "Active rest + stretching"
        }
    elif "muscle" in goal_lower:
        plan = {
            "Day 1": "Chest & Triceps workout",
            "Day 2": "Back & Biceps workout",
            "Day 3": "Leg day workout",
            "Day 4": "Shoulders & Abs",
            "Day 5": "Upper body heavy workout",
            "Day 6": "Lower body + Core",
            "Day 7": "Rest & recovery"
        }
    else:
        plan = {
            "Day 1": "Light cardio + stretching",
            "Day 2": "Full body workout",
            "Day 3": "Core exercises",
            "Day 4": "Active recovery walk",
            "Day 5": "Strength training basics",
            "Day 6": "Endurance training",
            "Day 7": "Rest & recovery"
        }

    advice = (
        "💡 Lifestyle Tips:\n"
        "- Drink plenty of water\n"
        "- Get 7-8 hours sleep\n"
        "- Maintain balanced diet\n"
        "- Warm-up before exercise and cool down after\n"
        "- Listen to your body and avoid injury"
    )

    return plan, advice



# Home route - show input form

@app.route("/")
def home():
    return render_template("index.html")



# Generate plan route

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        age = data.get("age")
        gender = data.get("gender")
        goal = data.get("goal")
        preference = data.get("preference")
        time = data.get("time")

        # Basic validation
        if not all([age, gender, goal, preference, time]):
            return jsonify({"error": "Please fill all fields"}), 400

        # Generate plan and lifestyle advice
        plan, advice = generate_fitness_plan(age, gender, goal, preference, time)

        # Combine plan and advice as string
        plan_text = ""
        for day, workout in plan.items():
            plan_text += f"{day}: {workout}\n"
        plan_text += "\n" + advice

        return jsonify({"plan": plan_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500



# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)