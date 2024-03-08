import cv2

# 스트림 URL 설정
stream_url = 'http://192.168.0.227:8000/stream.mjpg'

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(stream_url)

while True:
    # 프레임별로 비디오 캡처
    ret, frame = cap.read()

    # 프레임 캡처가 성공했는지 확인
    if not ret:
        print("스트림에서 프레임을 받아오는데 실패했습니다.")
        break

    # 프레임을 화면에 표시
    cv2.imshow('Video Stream', frame)

    # 'q'를 누르면 루프에서 빠져나옴
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()