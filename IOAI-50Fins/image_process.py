import cv2
img = cv2.imread('photo.jpg')
if img is None:
    print("Фото не знайдено")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Color', img)
    cv2.imshow('Gray', gray)
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()