"""Support for Max! binary sensors."""
from homeassistant.components.binary_sensor import (
    DEVICE_CLASS_BATTERY,
    DEVICE_CLASS_OPENING,
    BinarySensorEntity,
)

from .const import ATTR_DISCOVER_DEVICES, ATTR_DISCOVERY_TYPE, DISCOVER_BATTERY
from .entity import HGDevice

SENSOR_TYPES_CLASS = {
    "MaxShutterContact": DEVICE_CLASS_OPENING,
}


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Max! binary sensor platform."""
    if discovery_info is None:
        return

    devices = []
    for conf in discovery_info[ATTR_DISCOVER_DEVICES]:
        if discovery_info[ATTR_DISCOVERY_TYPE] == DISCOVER_BATTERY:
            devices.append(MaxBatterySensor(conf))
        else:
            devices.append(MaxBinarySensor(conf))

    add_entities(devices, True)


class MaxBinarySensor(HGDevice, BinarySensorEntity):
    """Representation of a binary Max! device."""

    @property
    def is_on(self):
        """Return true if switch is on."""
        if not self.available:
            return False
        return bool(self._hm_get_state())

    @property
    def device_class(self):
        """Return the class of this sensor from DEVICE_CLASSES."""
        return SENSOR_TYPES_CLASS.get(self._maxdevice.__class__.__name__)

    def _init_data_struct(self):
        """Generate the data dictionary (self._data) from metadata."""
        # Add state to data struct
        if self._state:
            self._data.update({self._state: None})


class MaxBatterySensor(HGDevice, BinarySensorEntity):
    """Representation of an HomeMatic low battery sensor."""

    @property
    def device_class(self):
        """Return battery as a device class."""
        return DEVICE_CLASS_BATTERY

    @property
    def is_on(self):
        """Return True if battery is low."""
        return bool(self._hm_get_state())

    def _init_data_struct(self):
        """Generate the data dictionary (self._data) from metadata."""
        # Add state to data struct
        if self._state:
            self._data.update({self._state: None})
