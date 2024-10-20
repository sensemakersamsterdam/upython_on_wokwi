import binascii
import machine
import network
import time
from umqtt.simple import MQTTClient

BROKER = "broker.hivemq.com"

_mqtt_client = None  # Object holds our MQTT stuff.
_wifi = None  # Object represents the WiFi.


def wifi_connect(ssid, password=""):
    """Connect the board to WiFi as a station.

    Args:
        ssid (str): The SSID of the WiFi network.
        password (str, optional): The password for the WiFi network. Defaults to an empty string.

    Returns:
        None
    """
    global _wifi

    print("Connecting to WiFi...", end="")
    if _wifi:
        # Dispose of existing WiFi connection, if any.
        _wifi.active(False)

    _wifi = network.WLAN(network.STA_IF)  # Become a station
    _wifi.active(True)
    _wifi.connect(ssid, password)
    while not _wifi.isconnected():
        # Wait for connection
        time.sleep(0.5)
        print(".", end="")
    print(f"\nConnected to WiFi, ip={_wifi.ifconfig()[0]}")


def mqtt_connect(listen_topic, on_incoming, my_id=None):
    """Attach the board over WiFi to an MQTT broker.

    Args:
        listen_topic (str): The topic to listen to.
        on_incoming (function): The callback function to handle incoming messages.
        my_id (str, optional): The client ID for the MQTT connection. Defaults to None.

    Returns:
        None
    """
    global _mqtt_client

    print(f"Connecting to MQTT broker: {BROKER}.")
    assert _wifi.isconnected(), "WiFi is not connected."

    if my_id is None:
        # Provide default id from mac address
        my_id = b"SensAms-" + binascii.hexlify(machine.unique_id())

    _mqtt_client = MQTTClient(my_id, BROKER)

    if on_incoming is not None:
        _mqtt_client.set_callback(on_incoming)

    _mqtt_client.connect()
    _mqtt_client.subscribe(listen_topic)
    print(f"MQTT connected to {BROKER} and subscribed to {listen_topic} !")


def mqtt_loop(forever=False):
    """Check MQTT and run the callback when a message is waiting.

    Args:
        forever (bool, optional): If True, the loop will run indefinitely. Defaults to False.

    Returns:
        None
    """
    assert _mqtt_client is not None, f"Connect to {BROKER} first."
    _mqtt_client.check_msg()
    while forever:
        _mqtt_client.wait_msg()


def connect_mqtt_on_wifi(
    ssid, password="", listen_topic="#", on_incoming=None, my_id=None
):
    """Connect to WiFi and attach to MQTT in one call.

    Args:
        ssid (str): The SSID of the WiFi network.
        password (str, optional): The password for the WiFi network. Defaults to an empty string.
        listen_topic (str, optional): The topic to listen to. Defaults to "#".
        on_incoming (function, optional): The callback function to handle incoming messages. Defaults to None.
        my_id (str, optional): The client ID for the MQTT connection. Defaults to None.

    Returns:
        None
    """
    wifi_connect(ssid, password)
    mqtt_connect(listen_topic, on_incoming, my_id)
