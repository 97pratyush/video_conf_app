from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel
import cv2, subprocess, qimage2ndarray, time, constant as const

class SendandDisplayVideo():
    def __init__(self, image_label : QLabel, meeting_id : str, user_id : str) -> None:
        self.meeting_id = meeting_id
        self.user_id = user_id
        self.label = image_label

        url = f'{const.RTMP_URL}/{self.meeting_id}_{self.user_id}'

        self.send_command_opencv = ['ffmpeg', 
            '-f', 'rawvideo', # Take rawvideo as provided by opencv
            '-pix_fmt', 'bgr24', # Pix format of input video
            '-s', f'{const.FRAME_WIDTH}x{const.FRAME_HEIGHT}', # Video frame size
            '-i', '-', # Takes video input as pipe and opencv later writes in it continuously
            '-f', 'alsa', # Audio device foramt - alsa is for linux
            '-i', 'default', # Default audio input
            '-c:v', 'libx264', # Video encoder
            '-preset', 'veryfast', 
            '-tune', 'zerolatency',
            '-b:v', '100k', # Video bitrate
            '-c:a', 'aac',  # Audio codec
            '-ar', '44100', # Audio rate
            '-ac', '1', # 1 for mono, 2 for stereo
            '-af', 'afftdn', # Noise filtering
            '-maxrate', '3000k', 
            '-bufsize', '300k', # Buffer size
            '-f', f'{const.VIDEO_CODEC}',
            f'{url}' # Output server
        ]

        self.send_command_directly = ['ffmpeg', 
            '-f', 'v4l2', # Video input format for linux as v4l2(video for linux 2)
            '-s', f'{const.FRAME_WIDTH}x{const.FRAME_HEIGHT}', # Video frame size
            '-thread_queue_size', '1024', # Input video thread size
            '-i', '/dev/video0', # Takes input from linux
            '-f', 'alsa', # Audio device foramt - alsa is for linux
            '-thread_queue_size', '1024', # Input audio thread size
            '-i', 'default', # Default audio input
            '-c:v', 'libx264', # Video encoder
            '-preset', 'ultrafast',
            '-tune', 'zerolatency',
            '-b:v', '100k', # Video bitrate
            '-c:a', 'aac', # Audio codec
            '-ar', '44100', # Audio rate
            '-ac', '1', # 1 for mono, 2 for stereo
            '-af', 'afftdn', # Noise filtering
            '-maxrate', '3000k',
            '-bufsize', '300k',
            '-f', f'{const.VIDEO_CODEC}',
            f'{const.RTMP_URL}/{self.meeting_id}_{self.user_id}'
        ]

    def send_video_using_opencv_pipe(self):
        # Open a subprocess to send video
        self.send_process_opencv = subprocess.Popen(self.send_command_opencv, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

        capture = cv2.VideoCapture(0) # 0 means default camera at 0 index
        capture.set(cv2.CAP_PROP_FRAME_WIDTH, const.FRAME_WIDTH)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, const.FRAME_HEIGHT)

        start_time = time.time()
        max_tries = 0
        self.close_called = False

        try:
            while(True):
                if self.close_called == True:
                    break
                ret, frame = capture.read()
                if ret:
                    #Display frame on Meeting Page
                    self.display_video_frame(frame)
                    # Write to open pipe in send command
                    self.send_process_opencv.stdin.write(frame.tobytes())

                    # Flush buffer data after it's sent
                    self.send_process_opencv.stdin.flush()
                else:
                    max_tries += 1
                    if (max_tries >= const.MAX_TRIES and (time.time() - start_time) >= const.MAX_WAIT_TIME_FOR_SERVER): # Wait a maximum of wait time defined or max tries
                        print("Frames not being sent after", const.MAX_TRIES, "tries. Closing operation")
                        if capture:
                            capture.release()
                        if self.send_process_opencv.stdin:
                            self.send_process_opencv.stdin.flush()
                            self.send_process_opencv.stdin.close()
                        self.send_process_opencv.terminate()
                        return
        except Exception as e:
            print("Exception occured while sending video via opencv :", e)
        finally:
            if capture:
                capture.release()
            if self.send_process_opencv.stdin:
                self.send_process_opencv.stdin.close()
            self.send_process_opencv.terminate()

    def display_video_frame(self, frame):
        # Convert the frame from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)

        # Create a QImage from the frame data
        # image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        image = qimage2ndarray.array2qimage(frame)

        # Create a QPixmap from the QImage
        pixmap = QPixmap.fromImage(image)
        self.label.setPixmap(pixmap)

    def stop_sending_video_opencv(self):
        self.close_called = True
        if self.send_process_opencv.stdin:
            self.send_process_opencv.stdin.flush()
            self.send_process_opencv.stdin.close()
        self.send_process_opencv.terminate()

    def send_video_direct(self):
        print("Sending video directly using ffmpeg")
        try:
            send_process_directly = subprocess.Popen(self.send_command_directly, stderr=subprocess.PIPE)
        except Exception as e:
            print("Exception occured while sending video directly. Maybe camera is in use already? :", e)
        finally:
            send_process_directly.terminate()