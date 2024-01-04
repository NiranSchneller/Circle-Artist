import pyautogui
import screeninfo
import vector

# Assume used monitor is the first one
monitorInfo = screeninfo.get_monitors()[0]
MONITOR_RESOLUTION = (monitorInfo.width, monitorInfo.height)
pyautogui.PAUSE = 10**-2

# Tunable params
ACCURACY = 0.7  # The closer to zero, the more accurate the circle is.
CIRCLE_RADIUS = MONITOR_RESOLUTION[1] / 2


def cartesianToScreen(x: int, y: int):
    # Y axis is flipped
    return (MONITOR_RESOLUTION[0] / 2 + x, MONITOR_RESOLUTION[1] / 2 - y)


if __name__ == "__main__":
    # Our vector direction is always where we need to move mouse to
    # Assume website is fullscreen
    pyautogui.mouseDown(MONITOR_RESOLUTION[0] / 2, MONITOR_RESOLUTION[1] / 2)
    angle = ACCURACY
    # (0,0) is the center of circle
    drawVector = vector.Vector(0, CIRCLE_RADIUS)
    while (angle < 360):
        drawVector.rotate(ACCURACY)
        newDirection = cartesianToScreen(drawVector.x, drawVector.y)
        pyautogui.mouseDown(newDirection[0], newDirection[1])
        angle += ACCURACY