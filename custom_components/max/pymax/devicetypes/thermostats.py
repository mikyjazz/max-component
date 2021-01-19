import logging
from ..devicetypes.generic import HGDevice
from ..devicetypes.helper import HelperValveState, HelperLowBat, HelperRssiPeer, HelperRssiDevice

LOG = logging.getLogger(__name__)


class HGThermostat(HGDevice):
    """
    HM-CC-RT-DN, HM-CC-RT-DN-BoM
    ClimateControl-RadiatorThermostat that measures temperature and allows to set a target temperature or use some automatic mode.
    """
    def __init__(self, device_description, proxy, resolveparamsets=False):
        super().__init__(device_description, proxy, resolveparamsets)

        # constante
        self.AUTO_MODE = 0
        self.MANU_MODE = 1
        self.PARTY_MODE = 2
        self.BOOST_MODE = 3
        self.COMFORT_MODE = 4
        self.LOWERING_MODE = 5
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
        elif setmode == self.COMFORT_MODE:
            mode = 'COMFORT_MODE'
        elif setmode == self.LOWERING_MODE:
            mode = 'LOWERING_MODE'
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
    def PARTYMODE(self):
        """ Return party mode state. """
        return self.mode == self.PARTY_MODE

    @property
    def BOOSTMODE(self):
        """ Return boost state. """
        return self.mode == self.BOOST_MODE

    @property
    def COMFORTMODE(self):
        """ Return comfort state. """
        return self.mode == self.COMFORT_MODE

    @property
    def LOWERINGMODE(self):
        """ Return lowering state. """
        return self.mode == self.LOWERING_MODE



class MAXThermostat(HGThermostat, HelperLowBat, HelperValveState):
    """
    BC-RT-TRX-CyG, BC-RT-TRX-CyG-2, BC-RT-TRX-CyG-3, BC-RT-TRX-CyG-4
    ClimateControl-Radiator Thermostat that measures temperature and allows to set a target temperature or use some automatic mode.
    """
    def __init__(self, device_description, proxy, resolveparamsets=False):
        super().__init__(device_description, proxy, resolveparamsets)

        # init metadata
        self.SENSORNODE.update({"ACTUAL_TEMPERATURE": [1]})
        self.WRITENODE.update({"SET_TEMPERATURE": [1]})
        self.ACTIONNODE.update({"AUTO_MODE": [1],
                                "MANU_MODE": [1],
                                "BOOST_MODE": [1]})
        self.ATTRIBUTENODE.update({"CONTROL_MODE": [1],
                                   "VALVE_STATE": [1]})

class MAXWallThermostat(HGThermostat, HelperLowBat):
    """
    BC-TC-C-WM-4
    ClimateControl-Wall Thermostat that measures temperature and allows to set a target temperature or use some automatic mode.
    """
    def __init__(self, device_description, proxy, resolveparamsets=False):
        super().__init__(device_description, proxy, resolveparamsets)

        # init metadata
        self.SENSORNODE.update({"ACTUAL_TEMPERATURE": [1]})
        self.WRITENODE.update({"SET_TEMPERATURE": [1]})
        self.ACTIONNODE.update({"AUTO_MODE": [1],
                                "MANU_MODE": [1],
                                "BOOST_MODE": [1]})
        self.ATTRIBUTENODE.update({"CONTROL_MODE": [1]})



DEVICETYPES = {
    "BC-RT-TRX-CyG": MAXThermostat,
    "BC-RT-TRX-CyG-2": MAXThermostat,
    "BC-RT-TRX-CyG-3": MAXThermostat,
    "BC-RT-TRX-CyG-4": MAXThermostat,
    "BC-RT-TRX-CyN": MAXThermostat,
    "BC-TC-C-WM-2": MAXWallThermostat,
    "BC-TC-C-WM-4": MAXWallThermostat
}