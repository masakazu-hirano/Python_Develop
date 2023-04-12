import cv2

if __name__ == '__main__':
    cv2.imread('画像ファイル')
    cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    print(cv2.CascadeClassifier('haarcascade_frontalface_default.xml').detectMultiScale(cv2.imread('画像ファイル')))
