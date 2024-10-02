"""
This is a sample module to show the usage of a Jenkins pipeline.
"""

from enum import Enum

class MeasurementError(Exception):
    """ Custom exception. """

class DeviceError(Exception):
    """ Custom exception. """

class MODE(Enum):
    """ Enumeration to specify the multimeter mode."""
    DCV = 1
    ACV = 2
    DCI = 3
    ACI = 4
    RES = 5

class Multimeter:
    """Simulates a simple multimeter."""
    def __init__(self, device):
        """Set the devive and a mode dictionary"""
        self.device = device
        self.mode_dictionary = {
                MODE.DCV: "dc_v",
                MODE.ACV: "ac_v",
                MODE.DCI: "dc_i",
                MODE.ACI: "ac_i",
                MODE.RES: "res"
            }

    def set_mode(self, mode):
        """Set the multimeter mode."""
        self.device.set_measurement_mode(self.mode_dictionary.get(mode))

    def set_range(self, range_value):
        """"Set the multimeter measurement range."""
        self.device.set_measurement_range(range_value)

    def measure(self)-> float:
        """Returns a measurement value."""
        try:
            return self.device.get_measurement_value()
        except DeviceError as ex:
            raise MeasurementError('Can not perform measurement!') from ex
