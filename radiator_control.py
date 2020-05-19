from eq3bt import Thermostat, Mode

class RadiatorControl:
    def __init__(self, rooms):
        self.rooms = rooms
        self.radiators = {}
        
        for room_name, value in self.rooms.items():
            if isinstance(value, dict):
                for k, v in value.items():
                    self.radiators[room_name + '_' + k] = v    
            else:
                self.radiators[room_name] = value

    def get_radiators(self):
        return list(self.radiators.keys())

    def get_rooms(self):
        return list(self.rooms.keys())

    def mode_auto(self, radiator):
        if radiator in self.radiators.keys():
            try:
                t = Thermostat(self.radiators[radiator])
                t.mode = Mode.Auto
                return t.mode_readable
            except:
                return 'timeout'


    def mode_off(self, radiator):
        if radiator in self.radiators.keys():
            try:
                t = Thermostat(self.radiators[radiator])
                t.mode = Mode.Closed
                return t.mode_readable
            except:
                return 'timeout'

    def mode_manual(self, radiator, temp):
        if radiator in self.radiators.keys():
            try:
                t = Thermostat(self.radiators[radiator])
                t.mode = Mode.Manual
                t.target_temperature = temp
                return t.mode_readable.replace('(', '\(').replace(')', '\)').replace('.', '\.')
            except:
                return 'timeout'