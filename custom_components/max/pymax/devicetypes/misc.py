import logging
from ..devicetypes.generic import HGDevice
from ..devicetypes.helper import HelperActionPress, HelperEventRemote, HelperEventPress, HelperRssiPeer, HelperLowBat

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
        if "RC-2" in self.TYPE or "PB-2" in self.TYPE or "WRC2" in self.TYPE or "BRC2" in self.TYPE or "WRCC2" in self.TYPE:
            return [1, 2]
        return [1]


class RemotePress(HGEvent, HelperEventPress, HelperActionPress):
    """Remote handle buttons."""

    @property
    def ELEMENT(self):
        return [1, 2, 3]


class RemotePressBattery(HGEvent, HelperEventPress, HelperActionPress, HelperLowBat):
    """Remote handle buttons."""

    @property
    def ELEMENT(self):
        return [1, 2, 3]


DEVICETYPES = {
    "BC-PB-2-WM": RemotePressBattery,
}
