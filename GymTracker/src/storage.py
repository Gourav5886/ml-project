import json
from pathlib import Path

def load_workouts():
    file_path = Path("GymTracker")/'data'/'workouts.json'
    content = file_path.read_text()
    workouts = json.loads(content)
    return workouts

def save_workouts(workouts):
    file_path = Path("GymTracker")/'data'/'workouts.json'
    content = json.dumps(workouts,indent=4)
    file_path.write_text(content)

workouts = load_workouts()

workouts[0]["workout"] = "Back and Biceps"

save_workouts(workouts)