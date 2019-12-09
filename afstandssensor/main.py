import _thread

from distance_sensor import DistanceSensor
from toilet_occupation import ToiletOccupation

if __name__ == "__main__":
    _thread.start_new_thread(DistanceSensor, ())
    _thread.start_new_thread(ToiletOccupation, ())
