import logging
from ..devicetypes.generic import HGDevice
from ..devicetypes.helper import HelperActionPress, HelperEventRemote, HelperEventPress, HelperRssiDevice, HelperRssiPeer, HelperLowBat

LOG = logging.getLogger(__name__)


class HGEvent(HGDevice):
    pass


class HGCCU(HGDevice):
    pass


class RemoteVirtual(HGCCU, HelperEventRemote, HelperActionPress):
    """For virtual remote from ccu/homegear or simple devices with just PRESS_SHORT and PRESS_LONG."""

    @property
    def ELEMENT(self):
        return list(range(1, 51))


class Remote(HGEvent, HelperEventRemote, HelperActionPress, HelperRssiPeer):
    """Remote handle buttons."""

    @property
    def ELEMENT(self):
        if "PB-2" in self.TYPE:
            return [1, 2]
        return [1]


class RemotePress(HGEvent, HelperEventPress, HelperActionPress):
    """Remote handle buttons."""

    @property
    def ELEMENT(self):
        return [1, 2, 3]


class RemotePressBattery(HGEvent, HelperEventPress, HelperActionPress, HelperLowBat, HelperRssiDevice, HelperRssiPeer):
    """Remote handle buttons."""

    @property
    def ELEMENT(self):
        return [1, 2, 3]


DEVICETYPES = {
    "BC-PB-2-WM": RemotePressBattery,
}
