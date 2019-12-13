import _thread

from distance_sensor import DistanceSensor
from toilet_occupation import ToiletOccupation

_thread.start_new_thread(DistanceSensor, ())
_thread.start_new_thread(ToiletOccupation, ())