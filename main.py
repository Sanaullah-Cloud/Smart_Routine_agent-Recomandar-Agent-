import json
import os

memory_file = "memory.json"

# Load memory
if os.path.exists(memory_file):
    with open(memory_file, "r") as file:
        memory = json.load(file)
else:
    memory = {
        "morning_study": 0,
        "night_study": 0,
        "gym_yes": 0,
        "gym_no": 0
    }

print("🤖 Smart Daily Routine Agent")

# User Input
study = input("Best Study Time? (morning/night): ").lower()
gym = input("Do you go Gym? (yes/no): ").lower()

# Learning Update
if study == "morning":
    memory["morning_study"] += 1
elif study == "night":
    memory["night_study"] += 1

if gym == "yes":
    memory["gym_yes"] += 1
elif gym == "no":
    memory["gym_no"] += 1

# Save memory
with open(memory_file, "w") as file:
    json.dump(memory, file)

# Decide Best Routine
best_study = "Morning" if memory["morning_study"] >= memory["night_study"] else "Night"
best_gym = "Yes" if memory["gym_yes"] >= memory["gym_no"] else "No"

print("\n📊 Learned Preferences:")
print(memory)

print("\n📅 Recommended Daily Routine")

if best_study == "Morning":
    print("7 AM - Wake Up")
    print("8 AM - Study Time")
else:
    print("8 AM - Wake Up")
    print("9 PM - Study Time")

if best_gym == "Yes":
    print("5 PM - Gym Time")

print("11 PM - Sleep")

print("\n✅ Routine Generated & Memory Saved")