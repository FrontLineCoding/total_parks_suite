import pyautogui as ui, sys, keyboard, time

terminate = False

def stop_execution():
    global terminate
    terminate = True
    

keyboard.on_press_key("esc", lambda _: stop_execution())

while not terminate:
    if terminate:
        print("Escape key pressed. Exiting loop.")
        break

    screenWidth, screenHeight = ui.size()
    print('width:', screenWidth, 'Height:', screenHeight)

    currentMouseX, currentMouseY = ui.position()
    print('mouseX:', currentMouseX, 'mouseY:', currentMouseY)

    ui.moveTo(1019, 1079, duration=0.25)

    time.sleep(3)
