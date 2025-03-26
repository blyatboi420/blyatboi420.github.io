# Part 1
SPACESHIP_NAME = "gerald"
fuel_level = 100
crew_size = 2
planet = "Earth"

time_to_launch = "T-minus " + 10 + " seconds"
print("🚀 Welcome aboard the", SPACESHIP_NAME, "with", crew_size, "dinosaurs!")

# Part 2
fuel_level = 75  # Value can change

if fuel_level >= 80:
    print("🦖✅ Plenty of fuel! Launching in 3...2...1...🚀")
elif :
    print("🛑⚠️ Fuel low. Consider refueling.")
else:
    print("❌ Not enough fuel! Abort mission!")
    
# Part 3
print("🌟 Counting stars:")
for i in range (1, 11):
    print(i)

# Part 4
fuel = 50  
while fuel > 10:
    print("🛸 Floating through space... Fuel left:", fuel, "%")
    fuel -= 10

print("🚨 Out of fuel! Time to refuel!")

# Part 5
dino_crew = ["T-Rex", "Triceratops", "Velociraptor", "Stegosaurus", "Brachiosaurus"]  

print("👨‍🚀 Meet the Jurassic Space Crew!")
for dino in dino_crew:
    print("🦕 Captain", dino)