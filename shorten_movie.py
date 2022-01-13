# ref :  https://qiita.com/satsukiya/items/9647e20c4e27b3d0362a
# OpenCVがあるのでAnaconda環境とかでやるべし

import cv2

if __name__ == '__main__':
    cap = cv2.VideoCapture('sample_movie.mp4')

    cap_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    cap_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
    writer = cv2.VideoWriter('1min_sample_movie.mp4',fourcc, fps, (cap_width, cap_height))

    # 抽出したい開始or終了時間
    begin = 30
    end = 90

    fps=round(fps)
    # floatだったので、intにしておく。
    # print(fps)

    for i in range(end * fps):
        ret, frame = cap.read()
        if ret:
            if begin * fps < i:
                writer.write(frame)

    writer.release()
    cap.release()

