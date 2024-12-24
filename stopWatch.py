import time

def stopwatch():
    print("Press ENTER to start the stopwatch. Press Ctrl+C to stop it.")
    input()  # Wait for the user to press Enter
    print("Stopwatch started...")
    start_time = time.time()
    
    try:
        while True:
            elapsed_time = time.time() - start_time
            mins, secs = divmod(int(elapsed_time), 60)
            hours, mins = divmod(mins, 60)
            print(f"\rElapsed time: {hours:02}:{mins:02}:{secs:02}", end="")
            time.sleep(1)  # Update the display every second
    except KeyboardInterrupt:
        print("\nStopwatch stopped.")
        total_time = time.time() - start_time
        mins, secs = divmod(int(total_time), 60)
        hours, mins = divmod(mins, 60)
        print(f"Total time: {hours:02}:{mins:02}:{secs:02}")

# Run the stopwatch
stopwatch()
