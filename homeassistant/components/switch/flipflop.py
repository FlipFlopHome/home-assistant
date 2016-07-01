"""
homeassistant.components.switch.demo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Demo platform that has two fake switches.

"""
from homeassistant.components.switch import SwitchDevice

#from homeassistant.helpers.entity import ToggleEntity
from homeassistant.const import STATE_ON, STATE_OFF, DEVICE_DEFAULT_NAME
from homeassistant.components import flipflop


TCP_IP = '192.168.1.181'
TCP_PORT = 80

# pylint: disable=unused-argument
def setup_platform(hass, config, add_devices_callback, discovery_info=None):
    """ Find and return demo switches. """
    w = flipflop.WiFly(TCP_IP, TCP_PORT)
    
    w.OpenConnection()
    if w.getSwitchState() == True:
        state = STATE_ON
    else:
        state = STATE_OFF
        
    add_devices_callback([
        FlipFlopSwitch('Pool Pump', state, 'mdi:pool')
    ])


class FlipFlopSwitch(SwitchDevice):
    """ Provides a demo switch. """
    def __init__(self, name, state, icon):
        self._name = name or DEVICE_DEFAULT_NAME
        self._state = state
        self._icon = icon

        self.w = flipflop.WiFly(TCP_IP, TCP_PORT)
        

    @property
    def should_poll(self):
        """ polling needed """
        return True

    @property
    def name(self):
        """ Returns the name of the device if any. """
        return self._name
    
    @property
    def icon(self):
        """Return the icon to use for device if any."""
        return self._icon

    @property
    def state(self):
        """ Returns the state of the device if any. """
        return self._state

    @property
    def is_on(self):
        """ True if device is on. """
        self.w.OpenConnection()
        if self.w.getSwitchState() == True:
            self._state = STATE_ON
        else:
            self._state = STATE_OFF

        return self._state
    
    def turn_on(self, **kwargs):
        """ Turn the device on. """
        self.w.OpenConnection()
        self.w.setOn()
        
        self._state = STATE_ON

    def turn_off(self, **kwargs):
        """ Turn the device off. """
        self.w.OpenConnection()
        self.w.setOff()
        
        self._state = STATE_OFF
