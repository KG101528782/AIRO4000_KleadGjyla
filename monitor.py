# Function to check speed
def check_speed(speed):
    if speed < 10:
        return "Too slow"
    elif speed > 50:
        return "Too fast"
    else:
        return "Speed OK"

# Ask user how many robots to check
while True:
    try:
        num_robots = int(input("How many robots do you want to check (1-5)? "))
        if 1 <= num_robots <= 5:
            break
        else:
            print("Please enter a number between 1 and 5.")
    except ValueError:
        print("Please enter a valid integer.")

# Loop through each robot and check its speed
for i in range(1, num_robots + 1):
    while True:
        try:
            speed = float(input(f"Enter speed of robot {i} (cm/s): "))
            break
        except ValueError:
            print("Please enter a valid number.")
    
    result = check_speed(speed)
    print(f"Robot {i}: {result}")

