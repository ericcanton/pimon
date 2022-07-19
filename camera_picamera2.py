import io

from picamera2 import Picamera2
from base_camera import BaseCamera


class Camera(BaseCamera):
    @staticmethod
    def frames():
        stream = io.BytesIO()
        with Picamera2() as camera:
            camera.configure(camera.create_still_configuration(main={"size": (800, 600)}))
            camera.start(show_preview=False)
            stream.seek(0)

            while True:
                next_frame = camera.capture_image()
                next_frame.save(stream, format='JPEG')
                yield stream.getvalue()
                stream.seek(0)
