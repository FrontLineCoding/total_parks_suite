# NOTES: create local system variables to allow for accurate item counts whilst pausing 

import pyautogui as ui, keyboard, time, sys

# Get screen size and initial mouse position
screenWidth, screenHeight = ui.size()
currentMouseX, currentMouseY = ui.position()
counter = 0
total = 0
item_amount = 27
bank_amt_leather = 5863
bank_amt_bodies = 14690
time_remaining = ((bank_amt_leather / item_amount) * (17.5))
hours = int(time_remaining // 3600)
minutes = int((time_remaining % 3600) // 60)
seconds = int(time_remaining % 60)
formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"

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
    bank_amt_leather -= 27
    bank_amt_bodies += 27
    time_remaining = ((bank_amt_leather / item_amount) * (17.5))
    hours = int(time_remaining // 3600)
    minutes = int((time_remaining % 3600) // 60)
    seconds = int(time_remaining % 60)
    formatted_time = f"{hours:02}:{minutes:02}:{seconds:02}"
    print(f'Cast Count: {counter:,}     Bank Leather: {bank_amt_leather}     Bank Bodies: {bank_amt_bodies}     Time Remaining: {formatted_time}' )


    ui.click(button='right', x=1542, y=324)
    time.sleep(.5)
    ui.click(button='left', x=1542, y=398)
    time.sleep(.75)
    ui.keyDown('q')
    ui.keyUp('q')
    time.sleep(.75)
    ui.keyDown('space')
    ui.keyUp('space')
    time.sleep(15.5)

print("Program Terminated.")
