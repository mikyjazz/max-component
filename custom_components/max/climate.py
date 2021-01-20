"""Support for Max! thermostats."""
from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import (
    HVAC_MODE_AUTO,
    HVAC_MODE_HEAT,
    HVAC_MODE_OFF,
    PRESET_BOOST,
    PRESET_COMFORT,
    PRESET_ECO,
    SUPPORT_PRESET_MODE,
    SUPPORT_TARGET_TEMPERATURE,
)
from homeassistant.const import ATTR_TEMPERATURE, TEMP_CELSIUS

from .const import ATTR_DISCOVER_DEVICES, HG_ATTRIBUTE_SUPPORT
from .entity import HGDevice

HG_TEMP_MAP = ["ACTUAL_TEMPERATURE", "TEMPERATURE"]

HG_HUMI_MAP = ["ACTUAL_HUMIDITY", "HUMIDITY"]

HG_PRESET_MAP = {
    "BOOST_MODE": PRESET_BOOST,
    "COMFORT_MODE": PRESET_COMFORT,
    "LOWERING_MODE": PRESET_ECO,
}

HG_CONTROL_MODE = "CONTROL_MODE"
HGIP_CONTROL_MODE = "SET_POINT_MODE"

SUPPORT_FLAGS = SUPPORT_TARGET_TEMPERATURE | SUPPORT_PRESET_MODE


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Max! thermostat platform."""
    if discovery_info is None:
        return

    devices = []
    for conf in discovery_info[ATTR_DISCOVER_DEVICES]:
        new_device = HGThermostat(conf)
        devices.append(new_device)

    add_entities(devices, True)


class HGThermostat(HGDevice, ClimateEntity):
    """Representation of a Max! thermostat."""

    @property
    def supported_features(self):
        """Return the list of supported features."""
        return SUPPORT_FLAGS

    @property
    def temperature_unit(self):
        """Return the unit of measurement that is used."""
        return TEMP_CELSIUS

    @property
    def hvac_mode(self):
        """Return hvac operation ie. heat, cool mode.

        Need to be one of HVAC_MODE_*.
        """
        if self.target_temperature <= self._maxdevice.OFF_VALUE + 0.5:
            return HVAC_MODE_OFF
        if "MANU_MODE" in self._maxdevice.ACTIONNODE:
            if self._hg_control_mode == self._maxdevice.MANU_MODE:
                return HVAC_MODE_HEAT
            return HVAC_MODE_AUTO

        # Simple devices
        if self._data.get("BOOST_MODE"):
            return HVAC_MODE_AUTO
        return HVAC_MODE_HEAT

    @property
    def hvac_modes(self):
        """Return the list of available hvac operation modes.

        Need to be a subset of HVAC_MODES.
        """
        if "AUTO_MODE" in self._maxdevice.ACTIONNODE:
            return [HVAC_MODE_AUTO, HVAC_MODE_HEAT, HVAC_MODE_OFF]
        return [HVAC_MODE_HEAT, HVAC_MODE_OFF]

    @property
    def preset_mode(self):
        """Return the current preset mode, e.g., home, away, temp."""
        if self._data.get("BOOST_MODE", False):
            return "boost"

        if not self._hg_control_mode:
            return None

        mode = HG_ATTRIBUTE_SUPPORT[HG_CONTROL_MODE][1][self._hg_control_mode]
        mode = mode.lower()

        # Filter HVAC states
        if mode not in (HVAC_MODE_AUTO, HVAC_MODE_HEAT):
            return None
        return mode

    @property
    def preset_modes(self):
        """Return a list of available preset modes."""
        preset_modes = []
        for mode in self._maxdevice.ACTIONNODE:
            if mode in HG_PRESET_MAP:
                preset_modes.append(HG_PRESET_MAP[mode])
        return preset_modes

    @property
    def current_humidity(self):
        """Return the current humidity."""
        for node in HG_HUMI_MAP:
            if node in self._data:
                return self._data[node]

    @property
    def current_temperature(self):
        """Return the current temperature."""
        for node in HG_TEMP_MAP:
            if node in self._data:
                return self._data[node]

    @property
    def target_temperature(self):
        """Return the target temperature."""
        return self._data.get(self._state)

    def set_temperature(self, **kwargs):
        """Set new target temperature."""
        temperature = kwargs.get(ATTR_TEMPERATURE)
        if temperature is None:
            return None

        self._maxdevice.writeNodeData(self._state, float(temperature))

    def set_hvac_mode(self, hvac_mode):
        """Set new target hvac mode."""
        if hvac_mode == HVAC_MODE_AUTO:
            self._maxdevice.MODE = self._maxdevice.AUTO_MODE
        elif hvac_mode == HVAC_MODE_HEAT:
            self._maxdevice.MODE = self._maxdevice.MANU_MODE
        elif hvac_mode == HVAC_MODE_OFF:
            self._maxdevice.turnoff()

    def set_preset_mode(self, preset_mode: str) -> None:
        """Set new preset mode."""
        if preset_mode == PRESET_BOOST:
            self._maxdevice.MODE = self._maxdevice.BOOST_MODE
        elif preset_mode == PRESET_COMFORT:
            self._maxdevice.MODE = self._maxdevice.COMFORT_MODE
        elif preset_mode == PRESET_ECO:
            self._maxdevice.MODE = self._maxdevice.LOWERING_MODE

    @property
    def min_temp(self):
        """Return the minimum temperature."""
        return 4.5

    @property
    def max_temp(self):
        """Return the maximum temperature."""
        return 30.5

    @property
    def target_temperature_step(self):
        """Return the supported step of target temperature."""
        return 0.5

    @property
    def _hg_control_mode(self):
        """Return Control mode."""
        if HGIP_CONTROL_MODE in self._data:
            return self._data[HGIP_CONTROL_MODE]

        # Max!
        return self._data.get("CONTROL_MODE")

    def _init_data_struct(self):
        """Generate a data dict (self._data) from the Max! metadata."""
        self._state = next(iter(self._maxdevice.WRITENODE.keys()))
        self._data[self._state] = None

        if (
            HG_CONTROL_MODE in self._maxdevice.ATTRIBUTENODE
            or HGIP_CONTROL_MODE in self._maxdevice.ATTRIBUTENODE
        ):
            self._data[HG_CONTROL_MODE] = None

        for node in self._maxdevice.SENSORNODE.keys():
            self._data[node] = None
