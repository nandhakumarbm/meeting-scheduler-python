users = {}

def addMeeting(user_id, start_time, end_time):
    if user_id not in users:
        users[user_id] = {"meetings": [[start_time, end_time]], "hasOverlap": False}
        print(f"addMeeting({user_id}) at {start_time} - {end_time} -> True")
        return True

    for meet in users[user_id]["meetings"]:
        if not (end_time <= meet[0] or start_time >= meet[1]):
            print(f"addMeeting({user_id}) at {start_time} - {end_time} -> False (Overlaps with {meet})")
            users[user_id]["hasOverlap"] = True
            return False

    users[user_id]["meetings"].append([start_time, end_time])
    users[user_id]["meetings"].sort(key=lambda x: x[0])
    print(f"addMeeting({user_id}) at {start_time} - {end_time} -> True")
    return True


def getMeeting(user_id):
    if user_id not in users:
        print("User not found!")
        return
    print("Meetings:", users[user_id]["meetings"])


def hasOverlap(user_id):
    if user_id not in users:
        print("User not found!")
        return
    print("overlapping ->", users[user_id]["hasOverlap"])


while True:
    opt = int(input("\nEnter your choice (1:Add, 2:Get, 3:Check overlap, 4:Exit): "))

    if opt == 1:
        user_id = input("user_name: ")
        start_time = int(input("start_time: "))
        end_time = int(input("end_time: "))
        if start_time < end_time:
            addMeeting(user_id, start_time, end_time)
        else:
            print("Ensure start_time < end_time")

    elif opt == 2:
        user_id = input("user_name: ")
        getMeeting(user_id)

    elif opt == 3:
        user_id = input("user_name: ")
        hasOverlap(user_id)

    elif opt == 4:
        print("Exited!")
        break

    else:
        print("Invalid choice! Try again.")
