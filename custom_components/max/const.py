"""Constants for the Max! component."""

DOMAIN = "max"

DISCOVER_BINARY_SENSORS = "max.binary_sensor"
DISCOVER_CLIMATE = "max.climate"
DISCOVER_BATTERY = "max.battery"

ATTR_DISCOVER_DEVICES = "devices"
ATTR_PARAM = "param"
ATTR_CHANNEL = "channel"
ATTR_ADDRESS = "address"
ATTR_DEVICE_TYPE = "device_type"
ATTR_VALUE = "value"
ATTR_VALUE_TYPE = "value_type"
ATTR_INTERFACE = "interface"
ATTR_ERRORCODE = "error"
ATTR_MESSAGE = "message"
ATTR_TIME = "time"
ATTR_UNIQUE_ID = "unique_id"
ATTR_PARAMSET_KEY = "paramset_key"
ATTR_PARAMSET = "paramset"
ATTR_RX_MODE = "rx_mode"
ATTR_DISCOVERY_TYPE = "discovery_type"
ATTR_LOW_BAT = "LOW_BAT"
ATTR_LOWBAT = "LOWBAT"

EVENT_KEYPRESS = "max.keypress"
EVENT_IMPULSE = "max.impulse"
EVENT_ERROR = "max.error"

SERVICE_VIRTUALKEY = "virtualkey"
SERVICE_RECONNECT = "reconnect"
SERVICE_SET_VARIABLE_VALUE = "set_variable_value"
SERVICE_SET_DEVICE_VALUE = "set_device_value"
SERVICE_SET_INSTALL_MODE = "set_install_mode"
SERVICE_PUT_PARAMSET = "put_paramset"

HG_DEVICE_TYPES = {
    DISCOVER_CLIMATE: [
        "MAXThermostat",
        "MAXWallThermostat",
    ],
    DISCOVER_BINARY_SENSORS: [
        "MaxShutterContact",
    ],
}

HG_ATTRIBUTE_SUPPORT = {
    "CONFIG_PENDING": ["config", {1: "Configuration"}],
    "LOWBAT": ["battery", {0: "High", 1: "Low"}],
    "LOW_BAT": ["battery", {0: "High", 1: "Low"}],
    "ERROR": ["error", {0: "No"}],
    "STICKY_UNREACH": ["sticky_unreach", {1: "Unreachable"}],
    "UNREACH": ["unreach", {1: "Unreachable"}],
    "RSSI_PEER": ["rssi_peer", {}],
    "RSSI_DEVICE": ["rssi_device", {}],
    "VALVE_STATE": ["valve", {}],
    "CONTROL_MODE": [
        "mode",
        {0: "Auto", 1: "Manual", 2: "Away", 3: "Boost"},
    ],
    "WINDOW_OPEN_TEMPERATURE": ["window_open_temperature", {}],
}

HG_PRESS_EVENTS = [
    "PRESS_SHORT",
    "PRESS_LONG",
    "PRESS_CONT",
    "PRESS_LONG_RELEASE",
    "PRESS",
]

HG_IMPULSE_EVENTS = ["SEQUENCE_OK"]

CONF_RESOLVENAMES_OPTIONS = ["metadata", "json", "xml", False]

DATA_MAX = "max"
DATA_STORE = "max_store"
DATA_CONF = "max_conf"

CONF_INTERFACES = "interfaces"
CONF_LOCAL_IP = "local_ip"
CONF_LOCAL_PORT = "local_port"
CONF_PORT = "port"
CONF_PATH = "path"
CONF_CALLBACK_IP = "callback_ip"
CONF_CALLBACK_PORT = "callback_port"
CONF_RESOLVENAMES = "resolvenames"
CONF_JSONPORT = "jsonport"
