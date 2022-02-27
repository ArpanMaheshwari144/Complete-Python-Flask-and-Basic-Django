import time
from functools import lru_cache
inp=int(input("Enter the number of values you want to cache: "))
@lru_cache(maxsize=inp)
def video_streaming(n):
    # for first time video takes n time for streaming
    time.sleep(n)
    return (n)

if __name__ == '__main__':
    print("Start the video and watch to the end")
    video_streaming(5)
    video_streaming(4)
    video_streaming(3)
    video_streaming(2)
    video_streaming(1)
    print("Start the video again from beginning")
    input()
    video_streaming(5)
    print("Start the video from mid")




