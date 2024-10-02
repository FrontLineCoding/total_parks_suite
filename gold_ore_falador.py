import pyautogui, sys, keyboard, time


while True:
    # Get screen width and height
    screenWidth, screenHeight = pyautogui.size()
    print('width:', screenWidth, 'Height:', screenHeight)

    # Get current mouse position
    currentMouseX, currentMouseY = pyautogui.position()
    print('mouseX:', currentMouseX, 'mouseY:', currentMouseY)

    # Move mouse to a specified position
    pyautogui.moveTo(1019, 1079, duration=0.25)


    # Check for 'esc' key press to break the loop
    if keyboard.is_pressed('esc'):
        print("Escape key pressed. Exiting loop.")
        break

    time.sleep(3)