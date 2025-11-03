# 🗓️ Meeting Overlap Checker

A simple Python-based meeting scheduler that prevents overlapping meetings for each user.  
It allows adding, viewing, and checking meeting overlaps through a clean console interface.

---

## 🚀 Features

- Add meetings for specific users  
- Detect and prevent overlapping meetings  
- View all meetings of a user  
- Check if a user has any overlapping slots  
- Simple interactive menu system  

---

## 🧠 How It Works

- Each user’s meetings are stored in a dictionary.
- When a new meeting is added, the system checks existing time intervals.
- If the new meeting overlaps with any existing one, it’s rejected.

---

## 🖥️ Example Usage

```bash
Enter your choice (1:Add, 2:Get, 3:Check overlap, 4:Exit): 1
user_name: Nandha
start_time: 10
end_time: 12
addMeeting(Nandha) at 10 - 12 -> True

Enter your choice: 1
user_name: Nandha
start_time: 11
end_time: 13
addMeeting(Nandha) at 11 - 13 -> False (Overlaps with [10, 12])
