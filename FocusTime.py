import time

def focus_timer(minutes):
    seconds = minutes * 60
    for i in range(seconds, 0, -1):
        print("Remaining time: ", i, "seconds")
        time.sleep(1)
    print("Time's up! Focus session complete.")

if __name__ == "__main__":
    focus_timer(25) # 25 minutes focus session
