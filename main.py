from modules.screen_observer import ScreenObserver
import threading

def main():
    screen_observer = ScreenObserver()
    
    # Run the screen observer in a separate thread
    observer_thread = threading.Thread(target=screen_observer.run)
    observer_thread.start()

    # Placeholder for stopping the observer (e.g., on a user command)
    input("Press Enter to stop...")
    screen_observer.stop()
    observer_thread.join()

if __name__ == "__main__":
    main()
