import pyautogui
import screeninfo
import vector

monitorInfo = screeninfo.get_monitors()[0] # Assume used monitor is the first one
MONITOR_RESOLUTION = (monitorInfo.width, monitorInfo.height)
pyautogui.PAUSE = 10**-10

# Tunable params
ACCURACY = 0.1 # The closer to zero, the more accurate the circle is. 
CIRCLE_RADIUS = MONITOR_RESOLUTION[1] / 2

def cartesianToScreen(x: int, y: int):
    return (MONITOR_RESOLUTION[0] / 2 + x, MONITOR_RESOLUTION[1] / 2 - y) # Y axis is flipped

if __name__ == "__main__":
    # Our vector direction is always where we need to move mouse to
    pyautogui.mouseDown(MONITOR_RESOLUTION[0] / 2, MONITOR_RESOLUTION[1] / 2) # Assume website is fullscreen
    angle = ACCURACY
    drawVector = vector.Vector(0, CIRCLE_RADIUS) # (0,0) is the center of circle
    while (angle < 360):
        drawVector.rotate(ACCURACY)
        newDirection = cartesianToScreen(drawVector.x, drawVector.y)
        pyautogui.mouseDown(newDirection[0], newDirection[1])
        angle += ACCURACY


