from storage import load_workouts,save_workouts

def get_next_id(workouts):
    largest_id = 0
    for workout in workouts:
        if largest_id < workout['id']:
            largest_id = workout['id']
    return largest_id+1

def add_workout(workouts):
    new_id = get_next_id(workouts)
    date = input("enter workout date: ")
    workout = input("enter workout name: ")
    exercises = []
    
    while True:
        exercise_name = input("Enter exercise name: ")
        sets = []
        
        while True:
            weight = int(input("enter weight: ")) 
            reps = int(input("enter reps: ")) 
            sets.append({"weight":weight,'reps':reps})
            add_more = input("add another set? (y/n)").lower()
            if add_more !='y':
                break
        
        exercises.append({'name':exercise_name,'sets':sets})
        add_exercise = input("add another exercise? (y/n)").lower()
        if add_exercise != 'y':
            break

    new_workout = {'id':new_id,'date':date,'workout':workout,'exercises':exercises}
    workouts.append(new_workout)
    return workouts

current_workouts = load_workouts()
current_workouts = add_workout(current_workouts)
save_workouts(current_workouts)