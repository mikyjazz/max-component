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
        {0: "Auto", 1: "Manual", 2: "Party", 3: "Boost"},
    ],
    "ECO_TEMPERATURE": ["eco_temperature", {}],
    "COMFORT_TEMPERATURE": ["comfort_temperature", {}],
    "WINDOW_OPEN_TEMPERATURE": ["window_open_temperature", {}],
    "DECALCIFICATION_TIME": ["decalcification_time", {}],
    "DECALCIFICATION_WEEKDAY": [
        "decalcification_weekday",
        {0: "Saturday", 1: "Sunday", 2: "Moonday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday"},
    ],
    "PARTY_STOP_DAY": ["party_stop_day", {}],
    "PARTY_STOP_MONTH": ["party_stop_month", {}],
    "PARTY_STOP_YEAR": ["party_stop_year", {}],
    "PARTY_STOP_TIME": ["party_stop_time", {}],
    "ENDTIME_SATURDAY_1": ["endtime_saturday_1", {}],
    "ENDTIME_SATURDAY_2": ["endtime_saturday_2", {}],
    "ENDTIME_SATURDAY_3": ["endtime_saturday_3", {}],
    "ENDTIME_SATURDAY_4": ["endtime_saturday_4", {}],
    "ENDTIME_SATURDAY_5": ["endtime_saturday_5", {}],
    "ENDTIME_SATURDAY_6": ["endtime_saturday_6", {}],
    "ENDTIME_SATURDAY_7": ["endtime_saturday_7", {}],
    "ENDTIME_SATURDAY_8": ["endtime_saturday_8", {}],
    "ENDTIME_SATURDAY_9": ["endtime_saturday_9", {}],
    "ENDTIME_SATURDAY_10": ["endtime_saturday_10", {}],
    "ENDTIME_SATURDAY_11": ["endtime_saturday_11", {}],
    "ENDTIME_SATURDAY_12": ["endtime_saturday_12", {}],
    "ENDTIME_SATURDAY_13": ["endtime_saturday_13", {}],
    "TEMPERATURE_SATURDAY_1": ["temperature_saturday_1", {}],
    "TEMPERATURE_SATURDAY_2": ["temperature_saturday_2", {}],
    "TEMPERATURE_SATURDAY_3": ["temperature_saturday_3", {}],
    "TEMPERATURE_SATURDAY_4": ["temperature_saturday_4", {}],
    "TEMPERATURE_SATURDAY_5": ["temperature_saturday_5", {}],
    "TEMPERATURE_SATURDAY_6": ["temperature_saturday_6", {}],
    "TEMPERATURE_SATURDAY_7": ["temperature_saturday_7", {}],
    "TEMPERATURE_SATURDAY_8": ["temperature_saturday_8", {}],
    "TEMPERATURE_SATURDAY_9": ["temperature_saturday_9", {}],
    "TEMPERATURE_SATURDAY_10": ["temperature_saturday_10", {}],
    "TEMPERATURE_SATURDAY_11": ["temperature_saturday_11", {}],
    "TEMPERATURE_SATURDAY_12": ["temperature_saturday_12", {}],
    "TEMPERATURE_SATURDAY_13": ["temperature_saturday_13", {}],
    "ENDTIME_SUNDAY_1": ["endtime_sunday_1", {}],
    "ENDTIME_SUNDAY_2": ["endtime_sunday_2", {}],
    "ENDTIME_SUNDAY_3": ["endtime_sunday_3", {}],
    "ENDTIME_SUNDAY_4": ["endtime_sunday_4", {}],
    "ENDTIME_SUNDAY_5": ["endtime_sunday_5", {}],
    "ENDTIME_SUNDAY_6": ["endtime_sunday_6", {}],
    "ENDTIME_SUNDAY_7": ["endtime_sunday_7", {}],
    "ENDTIME_SUNDAY_8": ["endtime_sunday_8", {}],
    "ENDTIME_SUNDAY_9": ["endtime_sunday_9", {}],
    "ENDTIME_SUNDAY_10": ["endtime_sunday_10", {}],
    "ENDTIME_SUNDAY_11": ["endtime_sunday_11", {}],
    "ENDTIME_SUNDAY_12": ["endtime_sunday_12", {}],
    "ENDTIME_SUNDAY_13": ["endtime_sunday_13", {}],
    "TEMPERATURE_SUNDAY_1": ["temperature_sunday_1", {}],
    "TEMPERATURE_SUNDAY_2": ["temperature_sunday_2", {}],
    "TEMPERATURE_SUNDAY_3": ["temperature_sunday_3", {}],
    "TEMPERATURE_SUNDAY_4": ["temperature_sunday_4", {}],
    "TEMPERATURE_SUNDAY_5": ["temperature_sunday_5", {}],
    "TEMPERATURE_SUNDAY_6": ["temperature_sunday_6", {}],
    "TEMPERATURE_SUNDAY_7": ["temperature_sunday_7", {}],
    "TEMPERATURE_SUNDAY_8": ["temperature_sunday_8", {}],
    "TEMPERATURE_SUNDAY_9": ["temperature_sunday_9", {}],
    "TEMPERATURE_SUNDAY_10": ["temperature_sunday_10", {}],
    "TEMPERATURE_SUNDAY_11": ["temperature_sunday_11", {}],
    "TEMPERATURE_SUNDAY_12": ["temperature_sunday_12", {}],
    "TEMPERATURE_SUNDAY_13": ["temperature_sunday_13", {}],
    "ENDTIME_MONDAY_1": ["endtime_monday_1", {}],
    "ENDTIME_MONDAY_2": ["endtime_monday_2", {}],
    "ENDTIME_MONDAY_3": ["endtime_monday_3", {}],
    "ENDTIME_MONDAY_4": ["endtime_monday_4", {}],
    "ENDTIME_MONDAY_5": ["endtime_monday_5", {}],
    "ENDTIME_MONDAY_6": ["endtime_monday_6", {}],
    "ENDTIME_MONDAY_7": ["endtime_monday_7", {}],
    "ENDTIME_MONDAY_8": ["endtime_monday_8", {}],
    "ENDTIME_MONDAY_9": ["endtime_monday_9", {}],
    "ENDTIME_MONDAY_10": ["endtime_monday_10", {}],
    "ENDTIME_MONDAY_11": ["endtime_monday_11", {}],
    "ENDTIME_MONDAY_12": ["endtime_monday_12", {}],
    "ENDTIME_MONDAY_13": ["endtime_monday_13", {}],
    "TEMPERATURE_MONDAY_1": ["temperature_monday_1", {}],
    "TEMPERATURE_MONDAY_2": ["temperature_monday_2", {}],
    "TEMPERATURE_MONDAY_3": ["temperature_monday_3", {}],
    "TEMPERATURE_MONDAY_4": ["temperature_monday_4", {}],
    "TEMPERATURE_MONDAY_5": ["temperature_monday_5", {}],
    "TEMPERATURE_MONDAY_6": ["temperature_monday_6", {}],
    "TEMPERATURE_MONDAY_7": ["temperature_monday_7", {}],
    "TEMPERATURE_MONDAY_8": ["temperature_monday_8", {}],
    "TEMPERATURE_MONDAY_9": ["temperature_monday_9", {}],
    "TEMPERATURE_MONDAY_10": ["temperature_monday_10", {}],
    "TEMPERATURE_MONDAY_11": ["temperature_monday_11", {}],
    "TEMPERATURE_MONDAY_12": ["temperature_monday_12", {}],
    "TEMPERATURE_MONDAY_13": ["temperature_monday_13", {}],
    "ENDTIME_TUESDAY_1": ["endtime_tuesday_1", {}],
    "ENDTIME_TUESDAY_2": ["endtime_tuesday_2", {}],
    "ENDTIME_TUESDAY_3": ["endtime_tuesday_3", {}],
    "ENDTIME_TUESDAY_4": ["endtime_tuesday_4", {}],
    "ENDTIME_TUESDAY_5": ["endtime_tuesday_5", {}],
    "ENDTIME_TUESDAY_6": ["endtime_tuesday_6", {}],
    "ENDTIME_TUESDAY_7": ["endtime_tuesday_7", {}],
    "ENDTIME_TUESDAY_8": ["endtime_tuesday_8", {}],
    "ENDTIME_TUESDAY_9": ["endtime_tuesday_9", {}],
    "ENDTIME_TUESDAY_10": ["endtime_tuesday_10", {}],
    "ENDTIME_TUESDAY_11": ["endtime_tuesday_11", {}],
    "ENDTIME_TUESDAY_12": ["endtime_tuesday_12", {}],
    "ENDTIME_TUESDAY_13": ["endtime_tuesday_13", {}],
    "TEMPERATURE_TUESDAY_1": ["temperature_tuesday_1", {}],
    "TEMPERATURE_TUESDAY_2": ["temperature_tuesday_2", {}],
    "TEMPERATURE_TUESDAY_3": ["temperature_tuesday_3", {}],
    "TEMPERATURE_TUESDAY_4": ["temperature_tuesday_4", {}],
    "TEMPERATURE_TUESDAY_5": ["temperature_tuesday_5", {}],
    "TEMPERATURE_TUESDAY_6": ["temperature_tuesday_6", {}],
    "TEMPERATURE_TUESDAY_7": ["temperature_tuesday_7", {}],
    "TEMPERATURE_TUESDAY_8": ["temperature_tuesday_8", {}],
    "TEMPERATURE_TUESDAY_9": ["temperature_tuesday_9", {}],
    "TEMPERATURE_TUESDAY_10": ["temperature_tuesday_10", {}],
    "TEMPERATURE_TUESDAY_11": ["temperature_tuesday_11", {}],
    "TEMPERATURE_TUESDAY_12": ["temperature_tuesday_12", {}],
    "TEMPERATURE_TUESDAY_13": ["temperature_tuesday_13", {}],
    "ENDTIME_WEDNESDAY_1": ["endtime_wednesday_1", {}],
    "ENDTIME_WEDNESDAY_2": ["endtime_wednesday_2", {}],
    "ENDTIME_WEDNESDAY_3": ["endtime_wednesday_3", {}],
    "ENDTIME_WEDNESDAY_4": ["endtime_wednesday_4", {}],
    "ENDTIME_WEDNESDAY_5": ["endtime_wednesday_5", {}],
    "ENDTIME_WEDNESDAY_6": ["endtime_wednesday_6", {}],
    "ENDTIME_WEDNESDAY_7": ["endtime_wednesday_7", {}],
    "ENDTIME_WEDNESDAY_8": ["endtime_wednesday_8", {}],
    "ENDTIME_WEDNESDAY_9": ["endtime_wednesday_9", {}],
    "ENDTIME_WEDNESDAY_10": ["endtime_wednesday_10", {}],
    "ENDTIME_WEDNESDAY_11": ["endtime_wednesday_11", {}],
    "ENDTIME_WEDNESDAY_12": ["endtime_wednesday_12", {}],
    "ENDTIME_WEDNESDAY_13": ["endtime_wednesday_13", {}],
    "TEMPERATURE_WEDNESDAY_1": ["temperature_wednesday_1", {}],
    "TEMPERATURE_WEDNESDAY_2": ["temperature_wednesday_2", {}],
    "TEMPERATURE_WEDNESDAY_3": ["temperature_wednesday_3", {}],
    "TEMPERATURE_WEDNESDAY_4": ["temperature_wednesday_4", {}],
    "TEMPERATURE_WEDNESDAY_5": ["temperature_wednesday_5", {}],
    "TEMPERATURE_WEDNESDAY_6": ["temperature_wednesday_6", {}],
    "TEMPERATURE_WEDNESDAY_7": ["temperature_wednesday_7", {}],
    "TEMPERATURE_WEDNESDAY_8": ["temperature_wednesday_8", {}],
    "TEMPERATURE_WEDNESDAY_9": ["temperature_wednesday_9", {}],
    "TEMPERATURE_WEDNESDAY_10": ["temperature_wednesday_10", {}],
    "TEMPERATURE_WEDNESDAY_11": ["temperature_wednesday_11", {}],
    "TEMPERATURE_WEDNESDAY_12": ["temperature_wednesday_12", {}],
    "TEMPERATURE_WEDNESDAY_13": ["temperature_wednesday_13", {}],
    "ENDTIME_THURSDAY_1": ["endtime_thursday_1", {}],
    "ENDTIME_THURSDAY_2": ["endtime_thursday_2", {}],
    "ENDTIME_THURSDAY_3": ["endtime_thursday_3", {}],
    "ENDTIME_THURSDAY_4": ["endtime_thursday_4", {}],
    "ENDTIME_THURSDAY_5": ["endtime_thursday_5", {}],
    "ENDTIME_THURSDAY_6": ["endtime_thursday_6", {}],
    "ENDTIME_THURSDAY_7": ["endtime_thursday_7", {}],
    "ENDTIME_THURSDAY_8": ["endtime_thursday_8", {}],
    "ENDTIME_THURSDAY_9": ["endtime_thursday_9", {}],
    "ENDTIME_THURSDAY_10": ["endtime_thursday_10", {}],
    "ENDTIME_THURSDAY_11": ["endtime_thursday_11", {}],
    "ENDTIME_THURSDAY_12": ["endtime_thursday_12", {}],
    "ENDTIME_THURSDAY_13": ["endtime_thursday_13", {}],
    "TEMPERATURE_THURSDAY_1": ["temperature_thursday_1", {}],
    "TEMPERATURE_THURSDAY_2": ["temperature_thursday_2", {}],
    "TEMPERATURE_THURSDAY_3": ["temperature_thursday_3", {}],
    "TEMPERATURE_THURSDAY_4": ["temperature_thursday_4", {}],
    "TEMPERATURE_THURSDAY_5": ["temperature_thursday_5", {}],
    "TEMPERATURE_THURSDAY_6": ["temperature_thursday_6", {}],
    "TEMPERATURE_THURSDAY_7": ["temperature_thursday_7", {}],
    "TEMPERATURE_THURSDAY_8": ["temperature_thursday_8", {}],
    "TEMPERATURE_THURSDAY_9": ["temperature_thursday_9", {}],
    "TEMPERATURE_THURSDAY_10": ["temperature_thursday_10", {}],
    "TEMPERATURE_THURSDAY_11": ["temperature_thursday_11", {}],
    "TEMPERATURE_THURSDAY_12": ["temperature_thursday_12", {}],
    "TEMPERATURE_THURSDAY_13": ["temperature_thursday_13", {}],
    "ENDTIME_FRIDAY_1": ["endtime_friday_1", {}],
    "ENDTIME_FRIDAY_2": ["endtime_friday_2", {}],
    "ENDTIME_FRIDAY_3": ["endtime_friday_3", {}],
    "ENDTIME_FRIDAY_4": ["endtime_friday_4", {}],
    "ENDTIME_FRIDAY_5": ["endtime_friday_5", {}],
    "ENDTIME_FRIDAY_6": ["endtime_friday_6", {}],
    "ENDTIME_FRIDAY_7": ["endtime_friday_7", {}],
    "ENDTIME_FRIDAY_8": ["endtime_friday_8", {}],
    "ENDTIME_FRIDAY_9": ["endtime_friday_9", {}],
    "ENDTIME_FRIDAY_10": ["endtime_friday_10", {}],
    "ENDTIME_FRIDAY_11": ["endtime_friday_11", {}],
    "ENDTIME_FRIDAY_12": ["endtime_friday_12", {}],
    "ENDTIME_FRIDAY_13": ["endtime_friday_13", {}],
    "TEMPERATURE_FRIDAY_1": ["temperature_friday_1", {}],
    "TEMPERATURE_FRIDAY_2": ["temperature_friday_2", {}],
    "TEMPERATURE_FRIDAY_3": ["temperature_friday_3", {}],
    "TEMPERATURE_FRIDAY_4": ["temperature_friday_4", {}],
    "TEMPERATURE_FRIDAY_5": ["temperature_friday_5", {}],
    "TEMPERATURE_FRIDAY_6": ["temperature_friday_6", {}],
    "TEMPERATURE_FRIDAY_7": ["temperature_friday_7", {}],
    "TEMPERATURE_FRIDAY_8": ["temperature_friday_8", {}],
    "TEMPERATURE_FRIDAY_9": ["temperature_friday_9", {}],
    "TEMPERATURE_FRIDAY_10": ["temperature_friday_10", {}],
    "TEMPERATURE_FRIDAY_11": ["temperature_friday_11", {}],
    "TEMPERATURE_FRIDAY_12": ["temperature_friday_12", {}],
    "TEMPERATURE_FRIDAY_13": ["temperature_friday_13", {}],
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
