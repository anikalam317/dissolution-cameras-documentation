import os 
import yaml
import json
import paho.mqtt.client as mqtt
import helper_functions

__author__ = "Brent Maranzano"
__license__ = "MIT"


logger = helper_functions.setup_logger("dissocam.api")


class DissoCam():

    def __init__(self, camera_files_path="/app/camera_files"):
        self._state = {
                "basename": "dissolution_recording",
                "interval": 300,
                "duration": 3600*4,
                "vessels": [1, 2, 3, 4, 5]
            }
        self._isPreview = False
        self._isTimelapse = False
        self._isRecording = False
        self._files_path = camera_files_path
        self.mqttc = None
        logger.info("instantiated Dissocam")

    @classmethod
    def from_env_file(cls, env_file=".env"):
        """Create instance of class from a YAML file.

        Arguments
        env_file (str): Name of environment file.
        """
        with open(env_file, "rt") as file_obj:
            ENV = yaml.safe_load(file_obj.read())

        dissocam = cls(camera_files_path=ENV["camera_files_path"])
        dissocam.mqttc = dissocam._start_mqtt(ENV["mqtt"]["ip"])
        return dissocam

    @staticmethod
    def _start_mqtt(ip, port=1883):
        """Start the MQTT service.

        Arguments:
        ip (str): IP address of the MQTT broker.
        port (int): port number of the MQTT broker.
        """
        def on_connect(client, userdata, flags, rc):
            logger.debug("connected")

        def on_message(client, userdata, msg):
            payload = msg.payload.decode("utf-8", "strict")
            logger.debug(f"topic:{msg.topic}, payload:{payload}")

        def on_disconnect(client, userdata, rc=0):
            logger.debug(f"disconnect {str(rc)}")
            client.loop_stop()

        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.on_disconnect = on_disconnect
        client.connect(ip, port, 60)
        logger.debug("test")
        client.loop_start()
        logger.info(f"started MQTT server: {ip}")
        return client

    def get_state(self):
        """Read the current state from the database.

        Return dict of state information
        """
        return self._state

    def set_state(self, **kwargs):
        """Set the value in the database of column "key"
        to value "value"

        Arguments
            kwargs (dict): dictionary of key state parameters to set
        """
        self._state.update(kwargs)

    def get_recordings(self):
        """Return all the recording files.
        """
        files = []
        for num in [str(num).zfill(2) for num in range(1, 7)]:
            for pos in ["top", "bottom"]:
                path = f"{self._files_path}/vessel{num}-{pos}/recordings"
                tmp = os.listdir(path)
                for file in tmp:
                    files.append(f"{path}/{file}")
        return files

    def _make_topics(self):
        """Create the topics for the MQTT using vessels passed or
        the class state attribute that defines the vessels selected.

        Return (list): topics
        """
        topics = []
        # TODO This probably needs to be padded.
        for number in self._state["vessels"]:
            for position in ["top", "bottom"]:
                topics.append(
                    f"spBv1.0/dissocam/NCMD/vessel{str(number).zfill(2)}-{position}"
                )
        return topics

    def _publish_command(self, topic, command, *args, **kwargs):
        """Send a command

        Arguments
        topic (str): MQTT topic
        command (str): Command name to be sent.
        """
        message = {"command": command,
                   "args": args,
                   "kwargs": kwargs
                   }
        logger.debug(f"publishing: {topic}, {message}")
        message = json.dumps(message).encode("utf-8")
        self.mqttc.publish(topic, message)

    def start_preview(self):
        """Start preview for cameras.
        """
        for topic in self._make_topics():
            self._publish_command(topic, "start_preview")

    def stop_preview(self):
        """Stop preview for cameras.
        """
        for topic in self._make_topics():
            self._publish_command(topic, "stop_preview")

    def start_timelapse(self):
        """Start the cameras for timelapse recording.
        """
        for topic in self._make_topics():
            self._publish_command(
                topic, "start_timelapse", self._state["basename"],
                self._state["interval"], self._state["duration"]
            )

    def stop_timelapse(self):
        """Stop the timelapse recordings by cameras.
        """
        for topic in self._make_topics():
            self._publish_command(topic, "stop_timelapse")


if __name__ == "__main__":
    disso = DissoCam.from_env_file(".env")
