import logging

LOG = logging.getLogger(__name__)

# Parameter operations. Just needed if we would get the paramset-descriptions to do some auto-configuration magic.
PARAM_OPERATION_READ = 1
PARAM_OPERATION_WRITE = 2
PARAM_OPERATION_EVENT = 4

PARAM_UNREACH = 'UNREACH'
PARAMSET_VALUES = 'VALUES'
PARAMSET_MASTER = 'MASTER'


class HGGeneric():
    # pylint: disable=unused-argument
    def __init__(self, device_description, proxy, resolveparamsets):
        # These properties are available for every device and its channels
        self._ADDRESS = device_description.get('ADDRESS')
        LOG.debug("HGGeneric.__init__: device_description: " + str(self._ADDRESS) + " : " + str(device_description))
        self._FAMILY = device_description.get('FAMILY')
        self._FLAGS = device_description.get('FLAGS')
        self._ID = device_description.get('ID')
        self._PARAMSETS = device_description.get('PARAMSETS')
        self._PARAMSET_DESCRIPTIONS = {}
        self._TYPE = device_description.get('TYPE')
        self._VERSION = device_description.get('VERSION')
        self._proxy = proxy
        self._paramsets = {}
        self._eventcallbacks = []
        self._name = None
        self._VALUES = {}   # Dictionary to cache values. They are updated in the event() function.
        self._MASTER = {}
        self._VALUES[PARAM_UNREACH] = None

    @property
    def ADDRESS(self):
        return self._ADDRESS

    @property
    def TYPE(self):
        return self._TYPE

    @property
    def PARAMSETS(self):
        return self._paramsets

    @property
    def NAME(self):
        return self._name

    @NAME.setter
    def NAME(self, name):
        self._name = name

    def event(self, interface_id, key, value):
        """
        Handle the event received by server.
        """
        LOG.info(
            "HGGeneric.event: address=%s, interface_id=%s, key=%s, value=%s"
            % (self._ADDRESS, interface_id, key, value))

        self._VALUES[key] = value   # Cache the value

        for callback in self._eventcallbacks:
            LOG.debug("HGGeneric.event: Using callback %s", str(callback))
            callback(self._ADDRESS, interface_id, key, value)

    def getParamsetDescription(self, paramset):
        """
        Descriptions for paramsets are available to determine what can be done with the device.
        """
        try:
            self._PARAMSET_DESCRIPTIONS[paramset] = self._proxy.getParamsetDescription(self._ADDRESS, paramset)
        except Exception as err:
            LOG.error("HGGeneric.getParamsetDescription: Exception: %s", err)
            return False

    def updateParamset(self, paramset):
        """
        Devices should not update their own paramsets. They rely on the state of the server.
        Hence we pull the specified paramset.
        """
        try:
            if paramset:
                if self._proxy:
                    returnset = self._proxy.getParamset(self._ADDRESS, paramset)
                    if returnset:
                        self._paramsets[paramset] = returnset
                        if self.PARAMSETS:
                            if self.PARAMSETS.get(PARAMSET_VALUES):
                                self._VALUES[PARAM_UNREACH] = self.PARAMSETS.get(PARAMSET_VALUES).get(PARAM_UNREACH)
                        return True
            return False
        except Exception as err:
            LOG.debug("HGGeneric.updateParamset: Exception: %s, %s, %s" % (str(err), str(self._ADDRESS), str(paramset)))
            return False

    def updateParamsets(self):
        """
        Devices should update their own paramsets. They rely on the state of the server. Hence we pull all paramsets.
        """
        try:
            for ps in self._PARAMSETS:
                self.updateParamset(ps)
            return True
        except Exception as err:
            LOG.error("HGGeneric.updateParamsets: Exception: %s", err)
            return False

    def putParamset(self, paramset, data={}, rx_mode=None):
        """
        Some devices act upon changes to paramsets.
        A "putted" paramset must not contain all keys available in the specified paramset,
        just the ones which are writable and should be changed.
        """
        try:
            if paramset in self._PARAMSETS and data:
                if rx_mode is None:
                    self._proxy.putParamset(self._ADDRESS, paramset, data)
                else:
                    self._proxy.putParamset(self._ADDRESS, paramset, data, rx_mode)
                # We update all paramsets to at least have a temporarily accurate state for the device.
                # This might not be true for tasks that take long to complete (lifting a rollershutter completely etc.).
                # For this the server-process has to call the updateParamsets-method when it receives events for the device.
                self.updateParamsets()
                return True
            else:
                return False
        except Exception as err:
            LOG.error("HGGeneric.putParamset: Exception: %s", err)
            return False


class HGChannel(HGGeneric):
    def __init__(self, device_description, proxy, resolveparamsets=False):
        super().__init__(device_description, proxy, resolveparamsets)

        # These properties only exist for device-channels
        self._PARENT = device_description.get('PARENT')
        self._AES_ACTIVE = device_description.get('AES_ACTIVE')
        self._DIRECTION = device_description.get('DIRECTION')
        self._INDEX = device_description.get('INDEX')
        self._LINK_SOURCE_ROLES = device_description.get('LINK_SOURCE_ROLES')
        self._LINK_TARGET_ROLES = device_description.get('LINK_TARGET_ROLES')
        self._PARENT_TYPE = device_description.get('PARENT_TYPE')

        # We set the name to the parents address initially
        self._name = device_description.get('ADDRESS')

        # Optional properties of device-channels
        self._GROUP = device_description.get('GROUP')
        self._TEAM = device_description.get('TEAM')
        self._TEAM_TAG = device_description.get('TEAM_TAG')
        self._TEAM_CHANNELS = device_description.get('TEAM_CHANNELS')

        # Not in specification, but often present
        self._CHANNEL = device_description.get('CHANNEL')

        if resolveparamsets:
            self.updateParamsets()

    def getCachedOrUpdatedValue(self, key):
        """ Gets the device's value with the given key.

        If the key is not found in the cache, the value is queried from the host.
        """
        try:
            return self._VALUES[key]
        except KeyError:
            return self.getValue(key)

    def getCachedOrUpdatedMaster(self, key):
        """ Gets the device's master value with the given key.

        If the key is not found in the cache, the value is queried from the host.
        """
        try:
            return self._MASTER[key]
        except KeyError:
            return self.getMaster(key)

    @property
    def PARENT(self):
        return self._PARENT

    @property
    def UNREACH(self):
        """ Returns true if children is not reachable """
        return bool(self._VALUES.get(PARAM_UNREACH, False))

    def setEventCallback(self, callback):
        """
        Set additional event callbacks for the channel.
        Signature for callback-functions: foo(address, interface_id, key, value).
        """
        if hasattr(callback, '__call__'):
            self._eventcallbacks.append(callback)

    def setValue(self, key, value):
        """
        Some devices allow to directly set values to perform a specific task.
        """
        LOG.debug("HGChannel.setValue: address = '%s', key = '%s' value = '%s'", self._ADDRESS, key, value)
        try:
            self._proxy.setValue(self._ADDRESS, key, value)
            return True
        except Exception as err:
            LOG.error("HGChannel.setValue: %s on %s Exception: %s", key, self._ADDRESS, err)
            return False

    def getValue(self, key):
        """
        Some devices allow to directly get values for specific parameters.
        """
        LOG.debug("HGChannel.getValue: address = '%s', key = '%s'", self._ADDRESS, key)
        try:
            returnvalue = self._proxy.getValue(self._ADDRESS, key)
            self._VALUES[key] = returnvalue
            return returnvalue
        except Exception as err:
            LOG.info("HGChannel.getValue: %s on %s Exception: %s", key, self._ADDRESS, err)
            return False

    def setMaster(self, key, value):
        """
        Some devices allow to directly set values to perform a specific task.
        """
        LOG.debug("HGChannel.setMaster: address = '%s', key = '%s' value = '%s'", self._ADDRESS, key, value)
        try:
            self._proxy.setMaster(self._ADDRESS, key, value)
            return True
        except Exception as err:
            LOG.error("HGChannel.setMaster: %s on %s Exception: %s", key, self._ADDRESS, err)
            return False

    #here
    def getMaster(self, key):
        """
        Some devices allow to directly get values for specific parameters.
        """
        LOG.debug("HGChannel.getMaster: address = '%s', key = '%s'", self._ADDRESS, key)
        try:
            returnvalue = self.PARAMSETS.get(PARAMSET_MASTER)[key]
            #self._proxy.getParamset(Integer peerId, Integer channel, Integer remotePeerId, Integer remoteChannel)            
            #returnvalue = self._proxy.getMaster(self._ADDRESS, key)
            self._MASTER[key] = returnvalue
            return returnvalue
        except Exception as err:
            LOG.info("HGChannel.getMaster: %s on %s Exception: %s", key, self._ADDRESS, err)
            return False

class HGDevice(HGGeneric):
    def __init__(self, device_description, proxy, resolveparamsets=False):
        super().__init__(device_description, proxy, resolveparamsets)

        self._hgchannels = {}

        # Data point information
        # "NODE_NAME": channel
        #  for channel is possible:
        # - c  / getVaule from channel (dynamic)
        # - 0...n / getValue from channel (fix)
        self._SENSORNODE = {}
        self._BINARYNODE = {}
        self._ATTRIBUTENODE = {}
        self._WRITENODE = {}
        self._EVENTNODE = {}
        self._ACTIONNODE = {}
        self._MASTERNODE = {}

        # These properties only exist for interfaces themselves
        self._CHILDREN = device_description.get('CHILDREN')
        self._RF_ADDRESS = device_description.get('RF_ADDRESS')

        # We set the name to the address initially
        self._name = device_description.get('ADDRESS')

        # Optional properties might not always be present
        if 'CHANNELS' in device_description:
            self._CHANNELS = device_description['CHANNELS']
        else:
            self._CHANNELS = []

        self._PHYSICAL_ADDRESS = device_description.get('PHYSICAL_ADDRESS')
        self._INTERFACE = device_description.get('INTERFACE')
        self._ROAMING = device_description.get('ROAMING')
        self._RX_MODE = device_description.get('RX_MODE')
        self._FIRMWARE = device_description.get('FIRMWARE')
        self._AVAILABLE_FIRMWARE = device_description.get('AVAILABLE_FIRMWARE')
        self._UPDATABLE = device_description.get('UPDATABLE')
        self._PARENT_TYPE = None

    def getCachedOrUpdatedValue(self, key, channel=None):
        """ Gets the channel's value with the given key.

        If the key is not found in the cache, the value is queried from the host.
        If 'channel' is given, the respective channel's value is returned.
        """
        if channel:
            return self._hgchannels[channel].getCachedOrUpdatedValue(key)

        try:
            return self._VALUES[key]
        except KeyError:
            value = self._VALUES[key] = self.getValue(key)
            return value

    def getCachedOrUpdatedMaster(self, key, channel=None):
        """ Gets the channel's master value with the given key.

        If the key is not found in the cache, the value is queried from the host.
        If 'channel' is given, the respective channel's value is returned.
        """
        if channel:
            return self._hgchannels[channel].getCachedOrUpdatedMaster(key)

        try:
            return self._MASTER[key]
        except KeyError:
            value = self._MASTER[key] = self.getMaster(key)
            return value

    @property
    def UNREACH(self):
        """ Returns true if the device or any children is not reachable """
        if self._VALUES.get(PARAM_UNREACH, False):
            return True
        else:
            for device in self._hgchannels.values():
                if device.UNREACH:
                    return True
        return False

    @property
    def CHANNELS(self):
        return self._hgchannels

    @property
    def SENSORNODE(self):
        return self._SENSORNODE

    @property
    def BINARYNODE(self):
        return self._BINARYNODE

    @property
    def ATTRIBUTENODE(self):
        return self._ATTRIBUTENODE

    @property
    def WRITENODE(self):
        return self._WRITENODE

    @property
    def EVENTNODE(self):
        return self._EVENTNODE

    @property
    def ACTIONNODE(self):
        return self._ACTIONNODE

    @property
    def MASTERNODE(self):
        return self._MASTERNODE

    def getAttributeData(self, name, channel=None):
        """ Returns a attribute node """
        return self._getNodeData(name, self._ATTRIBUTENODE, channel)

    def getBinaryData(self, name, channel=None):
        """ Returns a binary node """
        return self._getNodeData(name, self._BINARYNODE, channel)

    def getSensorData(self, name, channel=None):
        """ Returns a sensor node """
        return self._getNodeData(name, self._SENSORNODE, channel)

    def getWriteData(self, name, channel=None):
        """ Returns a write node """
        return self._getNodeData(name, self._WRITENODE, channel)

    def getMasterData(self, name, channel=None):
        """ Returns a master node """
        return self._getMasterData(name, self._MASTERNODE, channel)

    def _getNodeData(self, name, metadata, channel=None):
        """ Returns a data point from data"""
        nodeChannel = None
        if name in metadata:
            nodeChannelList = metadata[name]
            if len(nodeChannelList) > 1:
                nodeChannel = channel if channel is not None else nodeChannelList[0]
            elif len(nodeChannelList) == 1:
                nodeChannel = nodeChannelList[0]
            else:
                LOG.warning("HGDevice._getNodeData: %s not found in %s, empty nodeChannelList" % (name, metadata))
                return None
            if nodeChannel is not None and nodeChannel in self.CHANNELS:
                return self._hgchannels[nodeChannel].getValue(name)

        LOG.error("HGDevice._getNodeData: %s not found in %s" % (name, metadata))
        return None

    def _getMasterData(self, name, metadata, channel=None):
        """ Returns a data point from master data"""
        nodeChannel = None
        if name in metadata:
            nodeChannelList = metadata[name]
            if len(nodeChannelList) > 1:
                nodeChannel = channel if channel is not None else nodeChannelList[0]
            elif len(nodeChannelList) == 1:
                nodeChannel = nodeChannelList[0]
            else:
                LOG.warning("HGDevice._geMasterData: %s not found in %s, empty nodeChannelList" % (name, metadata))
                return None
            if nodeChannel is not None and nodeChannel in self.CHANNELS:
                return self._hgchannels[nodeChannel].getMaster(name)

        LOG.error("HGDevice._getNodeData: %s not found in %s" % (name, metadata))
        return None

    def writeNodeData(self, name, data, channel=None):
        return self._setNodeData(name, self.WRITENODE, data, channel)

    def actionNodeData(self, name, data, channel=None):
        return self._setNodeData(name, self.ACTIONNODE, data, channel)

    def masterNodeData(self, name, data, channel=None):
        return self._setMasterData(name, self.MASTERNODE, data, channel)

    def _setNodeData(self, name, metadata, data, channel=None):
        """ Write a data point to data"""
        nodeChannel = None
        if name in metadata:
            nodeChannelList = metadata[name]
            if len(nodeChannelList) > 1:
                nodeChannel = channel if channel is not None else nodeChannelList[0]
            elif len(nodeChannelList) == 1:
                nodeChannel = nodeChannelList[0]
            if nodeChannel is not None and nodeChannel in self.CHANNELS:
                return self._hgchannels[nodeChannel].setValue(name, data)

        LOG.error("HGDevice._setNodeData: %s not found with value %s on %i" %
                  (name, data, nodeChannel))
        return False

    def _setMasterData(self, name, metadata, data, channel=None):
        """ Write a master data point to data"""
        nodeChannel = None
        if name in metadata:
            nodeChannelList = metadata[name]
            if len(nodeChannelList) > 1:
                nodeChannel = channel if channel is not None else nodeChannelList[0]
            elif len(nodeChannelList) == 1:
                nodeChannel = nodeChannelList[0]
            if nodeChannel is not None and nodeChannel in self.CHANNELS:
                return self._hgchannels[nodeChannel].setMaster(name, data)

        LOG.error("HGDevice._setNodeData: %s not found with value %s on %i" %
                  (name, data, nodeChannel))
        return False

    def get_rssi(self, channel=0):
        """
        This is a stub method which is implemented by the helpers
        HelperRssiPeer/HelperRssiDevice in order to provide a suitable
        implementation for the device.
        """
        #pylint: disable=unused-argument
        return 0

    @property
    def ELEMENT(self):
        """
        Returns count of elements for same functionality.
        Overwrite this value only if you have a special device such as Sw2 etc.
        """
        return [1]

    def setEventCallback(self, callback, bequeath=True, channel=0):
        """
        Set additional event callbacks for the device.
        Set the callback for specific channels or use the device itself and let
        it bequeath the callback to all of its children.
        Signature for callback-functions: foo(address, interface_id, key, value)
        """
        if hasattr(callback, '__call__'):
            if channel == 0:
                self._eventcallbacks.append(callback)
            elif not bequeath and channel > 0 and channel in self._hgchannels:
                self._hgchannels[channel]._eventcallbacks.append(callback)
            if bequeath:
                for channel, device in self._hgchannels.items():
                    device._eventcallbacks.append(callback)

    def setValue(self, key, value, channel=1):
        """
        Some devices allow to directly set values to perform a specific task.
        """
        if channel in self.CHANNELS:
            return self.CHANNELS[channel].setValue(key, value)

        LOG.error("HGDevice.setValue: channel not found %i!" % channel)

    def getValue(self, key, channel=1):
        """
        Some devices allow to directly get values for specific parameters.
        """
        if channel in self.CHANNELS:
            return self.CHANNELS[channel].getValue(key)

        LOG.error("HGDevice.getValue: channel not found %i!" % channel)

    def setMaster(self, key, value, channel=1):
        """
        Some devices allow to directly set values to perform a specific task.
        """
        if channel in self.CHANNELS:
            return self.CHANNELS[channel].setMaster(key, value)

        LOG.error("HGDevice.setMaster: channel not found %i!" % channel)

    def getMaster(self, key, channel=1):
        """
        Some devices allow to directly get values for specific parameters.
        """
        if channel in self.CHANNELS:
            return self.CHANNELS[channel].getMaster(key)

        LOG.error("HGDevice.getMaster: channel not found %i!" % channel)
