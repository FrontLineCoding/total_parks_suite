import pyautogui as ui, sys, keyboard, time    

screenWidth, screenHeight = ui.size()
currentMouseX, currentMouseY = ui.position()


keyboard.on_press_key("esc", lambda _: (_ for _ in ()).throw(ui.FailSafeException))

while True:
    
    print('Still Running')
