from functions import *

a = get_images()
count = 0
for i in a:
    x = frame_mask_vid(i)
    x = apply_mask(i, x)
    x = thresholding_vid(x)
    x = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    try:
        x = hough_line_transformation(x, i)
    except TypeError:
        x = i
    cv2.imwrite(f'output/{count}.png', x)
    count += 1


to_video()


cap = cv2.VideoCapture('detected_lane.mp4')
if not cap.isOpened():
    print("Error opening video  file")

while cap.isOpened():

    ret, frame = cap.read()
    if ret:

        cv2.imshow('Frame', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

cap.release()

cv2.destroyAllWindows()
