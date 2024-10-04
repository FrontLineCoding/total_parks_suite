import pyautogui as ui
import time

# Open a file to write the coordinates (optional)
try:
    while True:
        # Get current mouse position
        currentMouseX, currentMouseY = ui.position()

        # Print the coordinates
        print(f"Mouse Coordinates: X={currentMouseX}, Y={currentMouseY}")

        # Wait for 1 second before logging again
        time.sleep(1)

except KeyboardInterrupt:
    # Stop logging when user interrupts (Ctrl+C)
    print("\nLogging stopped.")
