import logging
from ..devicetypes.generic import HGDevice

LOG = logging.getLogger(__name__)



class HelperLowBat(HGDevice):
    """This Helper adds easy access to read the LOWBAT state"""
    def __init__(self, device_description, proxy, resolveparamsets=False):
        super().__init__(device_description, proxy, resolveparamsets)

        # init metadata
        self.ATTRIBUTENODE.update({"LOWBAT": [0]})

    def low_batt(self, channel=None):
        """ Returns if the battery is low. """
        return self.getAttributeData("LOWBAT", channel)

class HelperValveState(HGDevice):
    """View the valve state of thermostats and valve controllers."""
    def valve_state(self):
        """ Returns the current valve state. """
        return int(self.getAttributeData("VALVE_STATE"))


class HelperBinaryState(HGDevice):
    """Return the state of binary sensors."""
    def __init__(self, device_description, proxy, resolveparamsets=False):
        super().__init__(device_description, proxy, resolveparamsets)

        # init metadata
        self.BINARYNODE.update({"STATE": self.ELEMENT})

    def get_state(self, channel=None):
        """ Returns current state of handle """
        return bool(self.getBinaryData("STATE", channel))


class HelperSensorState(HGDevice):
    """Return the state of binary sensors."""
    def __init__(self, device_description, proxy, resolveparamsets=False):
        super().__init__(device_description, proxy, resolveparamsets)

        # init metadata
        self.SENSORNODE.update({"STATE": self.ELEMENT})

    def get_state(self, channel=None):
        """ Returns current state of handle """
        return self.getSensorData("STATE", channel)


class HelperActionPress(HGDevice):
    """Helper for simulate press button."""

    def __init__(self, device_description, proxy, resolveparamsets=False):
        super().__init__(device_description, proxy, resolveparamsets)

        self.ACTIONNODE.update({"PRESS_SHORT": self.ELEMENT,
                                "PRESS_LONG": self.ELEMENT})

    def press_long(self, channel=None):
        """Simulat a button press long."""
        self.actionNodeData("PRESS_LONG", 1, channel)

    def press_short(self, channel=None):
        """Simulat a button press short."""
        self.actionNodeData("PRESS_SHORT", 1, channel)


class HelperEventPress(HGDevice):
    """Remote handle buttons."""
    def __init__(self, device_description, proxy, resolveparamsets=False):
        super().__init__(device_description, proxy, resolveparamsets)

        self.EVENTNODE.update({"PRESS": self.ELEMENT})


class HelperEventRemote(HGDevice):
    """Remote handle buttons."""
    def __init__(self, device_description, proxy, resolveparamsets=False):
        super().__init__(device_description, proxy, resolveparamsets)

        self.EVENTNODE.update({"PRESS_SHORT": self.ELEMENT,
                               "PRESS_LONG": self.ELEMENT,
                               "PRESS_CONT": self.ELEMENT,
                               "PRESS_LONG_RELEASE": self.ELEMENT})


class HelperRssiDevice(HGDevice):
    """Used for devices which report their RSSI value through RSSI_DEVICE"""
    def __init__(self, device_description, proxy, resolveparamsets=False):
        super().__init__(device_description, proxy, resolveparamsets)
        self.ATTRIBUTENODE["RSSI_DEVICE"] = [0]

    def get_rssi(self, channel=0):
        return self.getAttributeData("RSSI_DEVICE", channel)


class HelperRssiPeer(HGDevice):
    """Used for devices which report their RSSI value through RSSI_PEER"""
    def __init__(self, device_description, proxy, resolveparamsets=False):
        super().__init__(device_description, proxy, resolveparamsets)
        self.ATTRIBUTENODE["RSSI_PEER"] = [0]

    def get_rssi(self, channel=0):
        return self.getAttributeData("RSSI_PEER", channel)


