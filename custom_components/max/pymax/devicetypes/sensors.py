import logging
from ..devicetypes.generic import HGDevice
from ..devicetypes.helper import (HelperLowBat, HelperBinaryState)

LOG = logging.getLogger(__name__)


class HGSensor(HGDevice):
    """This class helps to resolve class inheritance order problems."""


class MaxShutterContact(HelperBinaryState, HelperLowBat, HelperRssiDevice, HelperRssiPeer):
    """Door / Window contact that emits its open/closed state.
       This is a binary sensor."""


DEVICETYPES = {
    "BC-SC-Rd-WM-2": MaxShutterContact,
    "BC-SC-Rd-WM": MaxShutterContact,
}
