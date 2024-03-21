# drone_camera
raspi drone camera stream

# 라즈베리파이

## 카메라 켜기
```bash
sudo raspi-config
3 Interface Options    Configure connections to peripherals
I1 Legacy Camera Enable/disable legacy camera support
<Yes>
```
```bash
sudo raspi-config
3 Interface Options    Configure connections to peripherals
I6 Serial Port   Enable/disable shell messages on the serial connection 
# 처음 질문에선 No
<No>
# 다음 질문에선 Yes
<Yes>
```

```bash
python3 1.http_camera.py
```
다른 인터넷 창을 열고 아래의 주소를 입력하면 실시간 스트리밍 가능
http://<Your_Pi_IP_Address>:8000

# 컴퓨터에 설치할 것들

pip3 install opencv-python
sudo apt install python3-opencv

pip3 install cvzone
pip3 install meidapipe

