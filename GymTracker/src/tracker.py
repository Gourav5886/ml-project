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
            try:
                weight = int(input("enter weight: ")) 
                reps = int(input("enter reps: "))
            except ValueError:
                print("Invalid input. Enter numeric values.")
                continue 
            sets.append({"weight":weight,'reps':reps})
            while True:
                add_more = input("add another set? (y/n) ").lower()
                if add_more =='y':
                    break
                elif add_more =="n":
                    break
                else:
                    print("Invalid output")
                    continue
            if add_more=="n":
                break

        exercises.append({'name':exercise_name,'sets':sets})
        while True:
            add_exercise = input("add another exercise? (y/n) ").lower()
            if add_exercise == 'y':
                break
            elif add_exercise =="n":
                break
            else:
                print("Invalid input")
                continue
        if add_exercise =="n":
            break
            

    new_workout = {'id':new_id,'date':date,'workout':workout,'exercises':exercises}
    workouts.append(new_workout)
    save_workouts(workouts)
    return workouts


current_workouts = load_workouts()
# current_workouts = add_workout(current_workouts)
# save_workouts(current_workouts)
def view_workouts(workouts):
    for workout in workouts:
        print("ID:",workout['id'])
        print("Date:",workout['date'])
        print("Workout:",workout['workout'])
        for exercise in workout['exercises']:
            print("Exercise:",exercise['name'])
            for n,sets in enumerate(exercise['sets'],start=1):
                print(f"Set {n}: {sets['weight']} kg x {sets['reps']}")
        print()
# view_workouts(current_workouts)

def search_workouts(workouts,workout_type):
        matching_workouts =[]
        for workout in workouts:
            if workout_type == workout["workout"]:
                matching_workouts.append(workout)
        return matching_workouts

    
# res = search_workouts(current_workouts,"cardio")
# view_workouts(res) if res else print("No workout found.")

def find_workout_by_id(workouts, workout_id):
    for workout in workouts:
        if workout_id == workout['id']:
            return workout
    return None

# found_workout = find_workout_by_id(current_workouts, 99)
# print(found_workout)

def update_workout(workouts):
    workout_id = int(input("Enter workout ID to update: "))
    workout = find_workout_by_id(workouts, workout_id)
    if workout is not None:
        print(workout["date"],workout["workout"])
        while True:
            question = input("To update date press(d), To update workout press(w), for both press (b): ").lower()
            if question == "d":
                new_date = input("Enter new date: ")
                workout["date"]= new_date
                break
            elif question=="w":
                new_workout = input("Enter new workout name: ")
                workout["workout"]= new_workout
                break
            elif question=="b":
                new_date = input("Enter new date: ")
                new_workout = input("Enter new workout name: ")
                workout["date"],workout["workout"]=new_date,new_workout
                break
            else:
                print("Please press valid option")
                continue
        print("Workout updated successfully.")
        save_workouts(workouts)
    else:
        print("No workout find check the details again")
    return workouts

def delete_workout(workouts):
    try:
        workout_id = int(input("Enter workout ID to delete: "))
    except ValueError:
        print('Invalid input. Please enter a numeric workout ID.')
        return workouts
    workout = find_workout_by_id(workouts, workout_id)
    if workout is not None:
        print(workout["date"],workout["workout"])
        confirm = input("Are you sure to delete this workout? (y/n)").lower()
        if confirm !="y":
            print("No changes")
        else:
            workouts.remove(workout)
            save_workouts(workouts)
            print("Workout delete sucessfully")
    else:
        print("No workout find check the details again")
    return workouts
# current_workouts = delete_workout(current_workouts)
# save_workouts(current_workouts)

def total_workouts(workouts):
    return len(workouts)

# print(total_workouts(current_workouts))

def count_workout_type(workouts, workout_type):
    count = 0
    for workout in workouts:
        if workout_type == workout["workout"]:
            count+=1
    return count

# print(count_workout_type(current_workouts,"Legs"))

def total_exercises(workouts):
    total = 0
    for workout in workouts:
        total+=len(workout["exercises"])
    return total

# print(total_exercises(current_workouts))

def total_set(workouts):
    total = 0
    for workout in workouts:
        for exercise in workout["exercises"]:
            total+=len(exercise['sets'])
    return total

# print(total_set(current_workouts))

def show_statistics(workouts):
    print("Total workouts:", total_workouts(workouts))
    print("Total exercises:", total_exercises(workouts))
    print("Total sets:", total_set(workouts))

# show_statistics(current_workouts)

def workout_type_counts(workouts):
    counts = {}

    for workout in workouts:
        workout_type = workout["workout"]
        if workout_type not in counts:
            counts[workout_type] = 1
        else:
            counts[workout_type]+=1

    return counts

# print(workout_type_counts(current_workouts))

# add_workout(current_workouts)
# delete_workout(current_workouts)
# update_workout(current_workouts)
# view_workouts(current_workouts)