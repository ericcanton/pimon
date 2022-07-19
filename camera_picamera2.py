from picamera2 import Picamera2
from base_camera import BaseCamera


class Camera(BaseCamera):
    @staticmethod
    def frames():
        with Picamera2() as camera:
            camera.configure(camera.create_still_configuration())
            camera.start(show_preview=False)

            while True:
                yield camera.capture_image()
