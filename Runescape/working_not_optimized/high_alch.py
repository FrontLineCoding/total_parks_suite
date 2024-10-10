import pyautogui as ui, keyboard, time, sys

# Get screen size and initial mouse position
screenWidth, screenHeight = ui.size()
currentMouseX, currentMouseY = ui.position()
counter = 0
total = 0
item_amount = 8088

# Define a function to terminate the loop
terminate = False

def on_escape_key(event):
    global terminate
    terminate = True
    ui.moveTo(0, 0)
    sys.exit("Program Terminated.")  # Exit the entire program when ESC is pressed

# Bind the "Escape" key to terminate the program
keyboard.on_press_key("esc", on_escape_key)

# Wait for the "F1" key to start the main loop
print("Press F1 to start the automation...")
keyboard.wait("f1")  # Wait here until "F1" is pressed

# Main loop
while not terminate:
    counter += 1
    total += item_amount
    print(f'High Alch: {counter:,} Total Money from Run: {total:,}')
    keyboard.press('q')
    time.sleep(1)
    ui.click()
    time.sleep(3)

print("Program Terminated.")
