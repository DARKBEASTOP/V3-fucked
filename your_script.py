import time

def your_task():
    print("Running your task...")
    # Simulate work here
    time.sleep(10)  # Replace with actual task logic

if __name__ == "__main__":
    while True:
        try:
            your_task()
        except Exception as e:
            print(f"Error: {e}. Restarting task...")
        time.sleep(60)  # Wait for 60 seconds before restarting