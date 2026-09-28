import json
from pathlib import Path

def load_workouts():
    try:
        file_path = Path("GymTracker")/'data'/'workouts.json'
        content = file_path.read_text()
        workouts = json.loads(content)
        return workouts
    except FileNotFoundError:
        return []
        
def save_workouts(workouts):
    file_path = Path("GymTracker")/'data'/'workouts.json'
    content = json.dumps(workouts,indent=4)
    file_path.write_text(content)
