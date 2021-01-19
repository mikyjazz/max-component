import logging
from ..devicetypes import generic, misc, sensors, thermostats

LOG = logging.getLogger(__name__)

try:
    UNSUPPORTED = generic.HGDevice
    SUPPORTED = {}
    SUPPORTED.update(sensors.DEVICETYPES)
    SUPPORTED.update(thermostats.DEVICETYPES)
    SUPPORTED.update(misc.DEVICETYPES)
except Exception as err:
    LOG.critical("devicetypes Exception: %s" % (err,))
    UNSUPPORTED = False
    SUPPORTED = {}
