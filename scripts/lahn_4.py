import time
import os
import keyboard

def start_camera():
    command = "libcamera-vid -t 0 -b 9000000 --vflip --hflip --autofocus-mode=manual --lens-position=0.0 --width 1920 --height 1080 --framerate 30 --codec libav -o Flight"+str(int(time.time()))+".mp4 &"
    os.system(command)

def stop_camera():
    os.system("pkill -SIGINT libcamera-vid")

# 카메라 시작
start_camera()

try:
    # 'q' 키가 눌릴 때까지 대기
    keyboard.wait('q')
    # 카메라 종료 및 라즈베리파이 종료
    stop_camera()
    os.system("sudo poweroff")

except KeyboardInterrupt:
    # Ctrl+C로 인터럽트 받을 경우 종료
    stop_camera()