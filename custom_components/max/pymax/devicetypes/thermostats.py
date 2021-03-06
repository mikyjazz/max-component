import logging
from ..devicetypes.generic import HGDevice
from ..devicetypes.helper import HelperValveState, HelperLowBat, HelperRssiPeer, HelperRssiDevice

MAX_DOW = ["SATURDAY", "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]

LOG = logging.getLogger(__name__)


class HGThermostat(HGDevice):
    """
    ClimateControl-RadiatorThermostat that measures temperature and allows to set a target temperature or use some automatic mode.
    """
    def __init__(self, device_description, proxy, resolveparamsets=False):
        super().__init__(device_description, proxy, resolveparamsets)

        # constante
        self.AUTO_MODE = 0
        self.MANU_MODE = 1
        self.PARTY_MODE = 2
        self.BOOST_MODE = 3
        self.OFF_VALUE = 4.5

        self.mode = None

    def actual_temperature(self):
        """ Returns the current temperature. """
        return self.getSensorData("ACTUAL_TEMPERATURE")

    def get_set_temperature(self):
        """ Returns the current target temperature. """
        return self.getWriteData("SET_TEMPERATURE")

    def set_temperature(self, target_temperature):
        """ Set the target temperature. """
        try:
            target_temperature = float(target_temperature)
        except Exception as err:
            LOG.debug("Thermostat.set_temperature: Exception %s" % (err,))
            return False
        self.writeNodeData("SET_TEMPERATURE", target_temperature)

    def turnoff(self):
        """ Turn off Thermostat. """
        self.writeNodeData("SET_TEMPERATURE", self.OFF_VALUE)

    @property
    def MODE(self):
        """ Return mode. """
        return self.getAttributeData("CONTROL_MODE")

    @MODE.setter
    def MODE(self, setmode):
        """ Set mode. """
        set_data = True
        mode = None
        if setmode == self.AUTO_MODE:
            mode = 'AUTO_MODE'
        elif setmode == self.MANU_MODE:
            mode = 'MANU_MODE'
            set_data = self.get_set_temperature()
        elif setmode == self.BOOST_MODE:
            mode = 'BOOST_MODE'
        elif setmode == self.PARTY_MODE:
            mode = 'PARTY_MODE'
        else:
            LOG.warning("Thermostat.MODE.setter: Invalid mode: %s" % str(setmode))
        if mode:
            self.actionNodeData(mode, set_data)

    @property
    def AUTOMODE(self):
        """ Return auto mode state. """
        return self.mode == self.AUTO_MODE

    @property
    def MANUMODE(self):
        """ Return manual mode state. """
        return self.mode == self.MANU_MODE

    @property
    def BOOSTMODE(self):
        """ Return boost state. """
        return self.mode == self.BOOST_MODE

    @property
    def PARTYMODE(self):
        """ Return party mode state. """
        return self.mode == self.PARTY_MODE

class MAXThermostat(HGThermostat, HelperLowBat, HelperValveState, HelperRssiDevice, HelperRssiPeer):
    """
    BC-RT-TRX-CyG, BC-RT-TRX-CyN, BC-RT-TRX-CyG-2, BC-RT-TRX-CyG-3, BC-RT-TRX-CyG-4
    ClimateControl-Radiator Thermostat that measures temperature and allows to set a target temperature or use some automatic mode.
    """
    def __init__(self, device_description, proxy, resolveparamsets=False):
        super().__init__(device_description, proxy, resolveparamsets)

        # init metadata
        self.SENSORNODE.update({"ACTUAL_TEMPERATURE": [1]})
        self.WRITENODE.update({"SET_TEMPERATURE": [1]})
        self.ACTIONNODE.update({"AUTO_MODE": [1],
                                "MANU_MODE": [1],
                                "PARTY_MODE": [1],
                                "BOOST_MODE": [1]})
        self.ATTRIBUTENODE.update({"CONTROL_MODE": [1],
                                   "PARTY_STOP_DAY": [1],
                                   "PARTY_STOP_MONTH": [1],
                                   "PARTY_STOP_YEAR": [1],
                                   "PARTY_STOP_TIME": [1],
                                   "VALVE_STATE": [1],
                                   "ECO_TEMPERATURE": [1],
                                   "COMFORT_TEMPERATURE": [1],
                                   "WINDOW_OPEN_TEMPERATURE": [1],
                                   "DECALCIFICATION_TIME": [1],
                                   "DECALCIFICATION_WEEKDAY": [1]})
        for dow in MAX_DOW:
            for step in range(1, 14):
                self.MASTERNODE.update({"ENDTIME_"+dow+"_"+str(step): [0],
                                        "TEMPERATURE_"+dow+"_"+str(step): [0]})


class MAXWallThermostat(HGThermostat, HelperLowBat, HelperRssiDevice, HelperRssiPeer):
    """
    BC-TC-C-WM-4, BC-TC-C-WM-2
    ClimateControl-Wall Thermostat that measures temperature and allows to set a target temperature or use some automatic mode.
    """
    def __init__(self, device_description, proxy, resolveparamsets=False):
        super().__init__(device_description, proxy, resolveparamsets)

        # init metadata
        self.SENSORNODE.update({"ACTUAL_TEMPERATURE": [1]})
        self.WRITENODE.update({"SET_TEMPERATURE": [1]})
        self.ACTIONNODE.update({"AUTO_MODE": [1],
                                "MANU_MODE": [1],
                                "PARTY_MODE": [1],
                                "BOOST_MODE": [1]})
        self.ATTRIBUTENODE.update({"CONTROL_MODE": [1],
                                   "PARTY_STOP_DAY": [1],
                                   "PARTY_STOP_MONTH": [1],
                                   "PARTY_STOP_YEAR": [1],
                                   "PARTY_STOP_TIME": [1],
                                   "ECO_TEMPERATURE": [1],
                                   "COMFORT_TEMPERATURE": [1],
                                   "WINDOW_OPEN_TEMPERATURE": [1],
                                   "DECALCIFICATION_TIME": [1],
                                   "DECALCIFICATION_WEEKDAY": [1]})
        for dow in MAX_DOW:
            for step in range(1, 14):
                self.MASTERNODE.update({"ENDTIME_"+dow+"_"+str(step): [0],
                                        "TEMPERATURE_"+dow+"_"+str(step): [0]})

DEVICETYPES = {
    "BC-RT-TRX-CyG": MAXThermostat,
    "BC-RT-TRX-CyG-2": MAXThermostat,
    "BC-RT-TRX-CyG-3": MAXThermostat,
    "BC-RT-TRX-CyG-4": MAXThermostat,
    "BC-RT-TRX-CyN": MAXThermostat,
    "BC-TC-C-WM-2": MAXWallThermostat,
    "BC-TC-C-WM-4": MAXWallThermostat
}
