import cv2 as cv
import numpy as np
import pyautogui
camera = cv.VideoCapture(0, cv.CAP_DSHOW)


while 1:
    _, frame = camera.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    close = False

    # Mover seta AZUL
    lowerBlue = np.array([98, 73, 121])
    upperBlue = np.array([179, 255, 255])
    mask = cv.inRange(hsv, lowerBlue, upperBlue)
    result = cv.bitwise_and(frame, frame, mask=mask)
    gray = cv.cvtColor(result, cv.COLOR_BGR2GRAY)
    _, borda = cv.threshold(gray, 3, 255, cv.THRESH_BINARY)

    contornos, _ = cv.findContours(
        borda, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    for contorno in contornos:
        area = cv.contourArea(contorno)
        if area > 800:
            (x, y, w, h) = cv.boundingRect(contorno)
            cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 1)
            cv.putText(
                frame,
                str(f"x: {x} y: {y}"),
                (x, y-20),
                cv.FONT_HERSHEY_SIMPLEX,
                1, 1
            )
    
    # Clique Esquerdo LARANJA
    lowerOrange = np.array([0, 88, 214])
    upperOrange = np.array([179, 255, 255])
    mask_orange = cv.inRange(hsv, lowerOrange, upperOrange)
    orange = cv.bitwise_and(frame, frame, mask=mask_orange)

    gray_orange = cv.cvtColor(orange, cv.COLOR_BGR2GRAY)
    _, borda_orange = cv.threshold(gray_orange, 3, 255, cv.THRESH_BINARY)
    contornos_orange, _ = cv.findContours(
    borda_orange, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    for contorno_orange in contornos_orange:
        area_orange = cv.contourArea(contorno_orange)
        if area_orange > 800:
            pyautogui.click(button='left')
            
    # Clique Direito ROSA
    lowerPink = np.array([164, 16, 139])
    upperPink = np.array([179, 255, 255])
    mask_pink = cv.inRange(hsv, lowerPink, upperPink)
    pink = cv.bitwise_and(frame, frame, mask=mask_pink)

    gray_pink = cv.cvtColor(pink, cv.COLOR_BGR2GRAY)
    _, borda_pink = cv.threshold(gray_pink, 3, 255, cv.THRESH_BINARY)
    contornos_pink, _ = cv.findContours(
    borda_pink, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)


    for contorno_pink in contornos_pink:
        area_pink = cv.contourArea(contorno_pink)
        if area_pink > 800:
            pyautogui.click(button='right')
    

    # Fechar janela VERDE
    lowerGreen = np.array([36,25,25])
    upperGreen = np.array([70, 255, 255])
    mask_green = cv.inRange(hsv, lowerGreen, upperGreen)
    green = cv.bitwise_and(frame, frame, mask=mask_green)

    gray_green = cv.cvtColor(green, cv.COLOR_BGR2GRAY)
    _, borda_green = cv.threshold(gray_green, 3, 255, cv.THRESH_BINARY)
    contornos_green, _ = cv.findContours(
        borda_green, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    for contorno_green in contornos_green:
        area_green = cv.contourArea(contorno_green)
        if area_green > 800:
              close = True

    pyautogui.moveTo(x * 3, y * 3)
    
    if close == True:
        break

    cv.imshow("result", frame)
    k = cv.waitKey(60)
    if k == 27:
        break

camera.release()
cv.destroyAllWindows()