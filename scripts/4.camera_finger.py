import cv2
from cvzone.HandTrackingModule import HandDetector
import time

detector = HandDetector(maxHands=1, detectionCon=0.8)

stream_url = 'http://192.168.0.227:8000/stream.mjpg'

video = cv2.VideoCapture(stream_url)

while True:
    _, img = video.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, draw=False)  # hands는 검출된 손에 대한 정보를 담은 리스트
    fingerup = []  # 손이 검출되지 않았을 경우를 위해 기본값을 빈 리스트로 설정
    if hands:  # 손이 검출되었는지 확인
        hand1 = hands[0]  # 첫 번째 검출된 손의 정보
        lmlist = hand1['lmList']  # 첫 번째 손의 랜드마크 리스트
        fingerup = detector.fingersUp(hand1)  # hand1 사전을 인자로 전달
    
    # print(fingerup)
    
    if fingerup == [1, 1, 1, 1, 1]:  # 모든 손가락이 올라갔을 때
        print("All fingers up!")
    

    # cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.1)

video.release()
# cv2.destroyAllWindows()
