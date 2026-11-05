import cv2
cap = cv2.VideoCapture(0)
logo = cv2.imread('logo.png')
while True:
    ret, frame = cap.read()
    if not ret:
        break
    height, width = frame.shape[:2]
    cx = width // 2
    cy = height // 2
    cv2.circle(frame, (cx, cy), 60, (0, 255, 0), 3)
    if logo is not None:
        small_logo = cv2.resize(logo, (40, 40))
        frame[cy-20:cy+20, cx-20:cx+20] = small_logo
    cv2.imshow('Webcam Project', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()