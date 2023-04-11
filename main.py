from functions import *
from PIL import ImageGrab
import time

last_time = time.time()
while True:

    screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 600)))
    count = 0
    screen1 = screen.copy()
    x = frame_mask(screen)
    x = apply_mask(screen, x)

    x = thresholding(x)
    x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    try:
        x2 = hough_line_transformation(x, screen)

    except TypeError:
        x2 = screen1.copy()
    count += 1

    cv2.imshow('Python Window 2', x2)
    cv2.imshow('Python Window', cv2.cvtColor(x2, cv2.COLOR_BGR2RGB))

    print(f'the screen rate is {(1 / (time.time() - last_time))}')
    last_time = time.time()

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

