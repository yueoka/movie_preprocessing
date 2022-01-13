# > python 4panel.py 1min_20211117_09-38-40-W06L_sample.mp4 
# みたいな感じで使う。
import cv2
import sys

args = sys.argv

def getCaps():
    global cap
    global cap_width
    global cap_height
    global fps
    global count
    global fourcc
    cap = cv2.VideoCapture(args[1])
    cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    count = round(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')

def cropGray(prefix, y1, y2, x1, x2):
    getCaps()
    # グレイスケール化の準備（一番右の0ってやつ）
    writer = cv2.VideoWriter(str(prefix) + args[1], fourcc, fps, (cap_width//2, cap_height//2),0)
    for i in range(count):
        ret, frame = cap.read()
        if ret:
            # クロップ
            frame = frame[y1:y2, x1:x2]
            # グレースケール化
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            writer.write(frame)
    writer.release()
    cap.release()

def main():
    getCaps()
    cropGray('crop1LU_', 0, cap_height//2, 0, cap_width//2)
    cropGray('crop2RU_', 0, cap_height//2, cap_width//2, cap_width)
    cropGray('crop3LB_', cap_height//2, cap_height, 0, cap_width//2)
    cropGray('crop4RB_', cap_height//2, cap_height, cap_width//2, cap_width)

if __name__ == '__main__':
    main()