from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QSize
from Meeting.meeting import MeetingPage
from PySide6.QtWidgets import QWidget, QMainWindow
from api_requests import end_meeting
import cv2, qimage2ndarray, numpy, subprocess, threading, constant as const, time
from Client import VideoConferencingHomePage

# Define the dimensions of the video frames
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Define the IP address and port number of the server
SERVER_IP = '10.0.0.248'
SERVER_PORT = 4000

# Video Codec
VIDEO_CODEC = 'flv'

# send_command = ['ffmpeg', 
#             '-f', 'rawvideo', 
#             '-pix_fmt', 'bgr24',
#             '-s', f'{FRAME_WIDTH}x{FRAME_HEIGHT}', 
#             '-i', '-',
#             '-f', 'alsa',
#             '-i', 'default',
#             '-c:v', 'libx264',
#             '-preset', 'veryfast',
#             '-tune', 'zerolatency',
#             '-b:v', '100k',
#             '-c:a', 'aac', 
#             '-ar', '44100',
#             '-ac', '1',
#             '-af', 'afftdn',
#             '-maxrate', '3000k',
#             '-bufsize', '100k',
#             '-f', f'{VIDEO_CODEC}',
#             f'rtmp://{SERVER_IP}/live/stream'
# ]




recv_command = ['ffmpeg',
            '-i', f'rtmp://{SERVER_IP}/live/test_test',
            '-f', 'rawvideo',
        #    '-fflags', 'nobuffer',
            '-pix_fmt', 'bgr24',
            '-bufsize', '100k',
            '-'
]

class StartMeeting(QMainWindow):
    def __init__(self, user_details, meeting_id, parent=None):
        super(StartMeeting, self).__init__(parent)

        self.video_size = QSize(FRAME_WIDTH, FRAME_HEIGHT, alignment = Qt.AlignCenter)
        self.user_id = user_details['id']
        self.user_name = user_details['name']
        self.meeting_id = int(meeting_id)
        self.meeting_page = MeetingPage()                
        self.meeting_page.end_call_button.clicked.connect(self.end_call)
        
        self.setCentralWidget(self.meeting_page)
        self.setWindowTitle(f"{self.user_name} - {self.meeting_id}")
        self.resize(700, 500)
        self.setAutoFillBackground(True)
        self.setStyleSheet("QMainWindow" "{" "background : #313a46;" "}")

        self.send_default_audio_video_command = ['ffmpeg', 
            '-f', 'v4l2',
            '-s', f'{const.FRAME_WIDTH}x{const.FRAME_HEIGHT}', 
            '-thread_queue_size', '1024',
            '-i', '/dev/video0',
            '-f', 'alsa',
            '-thread_queue_size', '1024',
            '-i', 'default',
            '-c:v', 'libx264',
            '-preset', 'ultrafast',
            '-tune', 'zerolatency',
            '-b:v', '100k',
            '-c:a', 'aac', 
            '-ar', '44100',
            '-ac', '1',
            '-af', 'afftdn',
            '-maxrate', '3000k',
            '-bufsize', '300k',
            '-f', f'{const.VIDEO_CODEC}',
            f'{const.RTMP_URL}/{self.meeting_id}_{self.user_id}'
        ]
        self.stream = subprocess.Popen(self.send_default_audio_video_command, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        print("Send started")
        time.sleep(20)
        self.home_page = VideoConferencingHomePage()
        # self.home_page.display_video_frame_using_ffmpeg_subprocess(self.meeting_page.labels[0], self.meeting_id, self.user_id)

        thread_ffmpeg_display = threading.Thread(target=self.home_page.display_video_frame_using_ffmpeg_subprocess, args=(self.meeting_page.labels[0], self.meeting_id, self.user_id), daemon=True)
        thread_ffmpeg_display.start()

        # # Send Video
        # self.stream = subprocess.Popen(self.send_command, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        # self.thread_send_video_frame = threading.Thread(target=self.setup_camera)
        # self.thread_send_video_frame.start()

        # # Recieve Video
        # thread_display_stream_frame = threading.Thread(target=self.display_stream_frame, daemon=True)
        # thread_display_stream_frame.start()

    def setup_camera(self):
        
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.video_size.width())
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.video_size.height())

        # thread_display_video_frame = threading.Thread(target=self.display_video_frame, args=(self.frame))
        # thread_display_video_frame.start()

        _, frame = self.capture.read()

        # self.timer = QTimer()
        # self.timer.timeout.connect(self.start_capturing)
        # self.timer.start(30)

        while(True):
            _, frame = self.capture.read()
            self.send_video_frame(frame)
            self.display_video_frame(frame)
        
    def send_video_frame(self, frame):
        # print("Sending Frame to Server")

        # Write the frame to the network stream
        self.stream.stdin.write(frame.tobytes())

        # Throw away data to pipe buffer
        self.stream.stdin.flush()
        

    def display_video_frame(self, frame):
        # print("Displaying Local Frame")
        # Convert the frame from BGR to RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.flip(frame, 1)

        # Create a QImage from the frame data
        # image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
        image = qimage2ndarray.array2qimage(frame)

        # Create a QPixmap from the QImage
        pixmap = QPixmap.fromImage(image)

        # Set the pixmap in the video frame label
        self.meeting_page.labels[0].setPixmap(pixmap)
        self.meeting_page.labels[0].setFixedSize(self.video_size)

    def end_call(self):
        try:
            end_meeting(self.user_id, self.meeting_id)
            self.close()
            print("Stopping ffmpeg sending command")
            # self.stream.terminate()
            # self.stream.kill()
            # self.stream.wait()
        except:
            self.close()

    def display_stream_frame(self):
        print("Reading Frame from Server")

        self.recv_process = subprocess.Popen(recv_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        limit = 0

        try:
            while(True):
                # Read a frame from the network stream
                frame_data = self.recv_process.stdout.read(FRAME_WIDTH * FRAME_HEIGHT * 3)

                if len(frame_data) != FRAME_WIDTH * FRAME_HEIGHT * 3:
                    print("Incorrect Frame Data : " + frame_data.decode("utf-8"))
                    return

                if frame_data:
                    print("Received a frame from server")
                    # Convert the frame data to a numpy array
                    frame = numpy.frombuffer(frame_data, dtype=numpy.uint8)
                    frame = frame.reshape((FRAME_HEIGHT, FRAME_WIDTH, 3))

                    # Convert the frame from BGR to RGB
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame = cv2.flip(frame, 1)

                    # Create a QImage from the frame data
                    # image = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                    image = qimage2ndarray.array2qimage(frame)
                    
                    # Create a QPixmap from the QImage
                    pixmap = QPixmap.fromImage(image)

                    # Set the pixmap in the stream frame label
                    self.meeting_page.labels[1].setPixmap(pixmap)
                    self.meeting_page.labels[1].setFixedSize(self.video_size)
                else:
                    limit += 1

                if(limit >= 5):
                    print("Not receiving any frame from the server. Closing read operation.")
                    self.recv_process.stdin.close()
                    self.recv_process.wait()
                    return
        except:
            self.recv_process.stdin.close()
            self.recv_process.wait()