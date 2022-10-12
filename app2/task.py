import threading
import pyautogui
import cv2
import numpy as np
from django.core.files.base import File
from .models import Ticket
from celery import shared_task, Celery
app = Celery()

@shared_task
def scrn(id, user_id):
    resolution = (1920, 1080)

    # Specify video codec
    codec = cv2.VideoWriter_fourcc(*"mp4v")

    # Specify name of Output file
    filename = str(user_id)+str(id)+".mp4"

    # Specify frames rate. We can choose any
    # value and experiment with it
    fps = 3.0

    # Creating a VideoWriter object
    out = cv2.VideoWriter(filename, codec, fps, resolution)

    # Create an Empty window
    cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

    # Resize this window
    cv2.resizeWindow("Live", 480, 270)

    def stop():
        ticket = Ticket.objects.get(id=id)
        ticket.video_stop = True
        ticket.save()

    timer = threading.Timer(60.0, stop)
    timer.start()

    while True:
        # Take screenshot using PyAutoGUI
        img = pyautogui.screenshot()

        # Convert the screenshot to a numpy array
        frame = np.array(img)

        # Convert it from BGR(Blue, Green, Red) to
        # RGB(Red, Green, Blue)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Write it to the output file
        out.write(frame)
        
        # Optional: Display the recording screen
        # cv2.imshow('Live', frame)
        ticket = Ticket.objects.get(id=id)
        # Stop recording when we press 'q'
        if ticket.video_stop == True:
            break

    # Release the Video writer
    out.release()

    # Destroy all windows
    cv2.destroyAllWindows()
    ticket = Ticket.objects.get(id=id)
    video = open(filename, 'rb')
    a = File(video)
    ticket.file_video.save(filename, a)
    # os.remove(filename)
    # data = {'user': str(ticket.user), 'screen_id': ticket.screen_id, 'screen_name': ticket.screen_name,
    #         'subject': ticket.subject, 'from_project': ticket.from_project}

    # files = []
    # file = 'document', (ticket.video.name, open(ticket.video.path, 'rb'))
    # files.append(file)
    # requests.post(url='http://127.0.0.1:8089/ticket-to-sperentes', data=data, files=files)
    return out
