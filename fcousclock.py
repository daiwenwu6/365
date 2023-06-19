import time

def focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        print(f"Remaining time: {remaining_time // 60}:{remaining_time % 60:02d}", end="\r", flush=True)
        time.sleep(1)

    print("Focus time is over!")

focus_minutes = int(input("Enter focus time in minutes: "))
focus_timer(focus_minutes)
