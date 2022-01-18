#!/usr/bin/env python
import logging
from flask import Flask, render_template, jsonify, request, send_file, Response
from flask_cors import CORS
from dissocam import DissoCam
import imghdr
import helper_functions
from time import sleep


__author__ = "Brent Maranzano"
__license__ = "MIT"

logger = logging.getLogger("dissocam")

app = Flask(__name__)
CORS(app)

logger = helper_functions.setup_logger("dissocame.api")
app.logger.setLevel(logging.DEBUG)


# disso = DissoCam.from_env_file()


@app.route('/')
def index():
    return render_template('index.html')


def send_image(number, position):
    """Send the image of the camera attached to a vessel.

    Arguments:
        number (int): Vessel number (e.g. 01, 02, 03, ...etc)
        pos (str): Vessel position ("top" | "bottom")
    """
    path = f"/camera_files/vessel{number.zfill(2)}-{position}/preview/preview.jpg"
    file_type = ""
    while file_type != "jpeg":
        try:
            file_type = imghdr.what(path)
        except Exception:
            pass
    logger.debug(path)
    return send_file(path, mimetype="image/jpeg")


@app.route('/getImage')
def get_image():
    return send_image(request.args["number"], request.args["position"])


def gen_frame(number, position):
    while True:
        path = f"/camera_files/vessel{number.zfill(2)}-{position}/preview/preview.jpg"
        while True:
            with open(path, mode='rb') as fObj:
                frame = fObj.read()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            sleep(5)


@app.route('/getVideo')
def get_video():
    return Response(gen_frame(request.args["number"], request.args["position"]),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/getState')
def get_state():
    setup = disso.get_state()
    return jsonify(setup)


@app.route('/setState', methods=['POST'])
def save_state():
    """Expected POST elements:
    setup (dictionary): Setup parameters
    """
    params = request.get_json()
    disso.set_state(**params)
    return "OK: setState"


@app.route('/startPreview', methods=['GET'])
def start_preview():
    disso.start_preview()
    return "OK: startPreview"


@app.route('/stopPreview', methods=['GET'])
def stop_preview():
    disso.stop_preview()
    return "OK: stopPreview"


@app.route('/startTimelapse', methods=['GET'])
def start_timelapse():
    disso.start_timelapse()
    return "OK: startTimelapse"


@app.route('/stopTimelapse', methods=['GET'])
def stop_timelapse():
    disso.stop_timelapse()
    return "OK: stopTimelapse"


@app.route('/getRecordings')
def get_recordings():
    recordings = disso.get_recordings()
    return jsonify(recordings)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
