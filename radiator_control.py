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
                return self.__print_temp(t.mode_readable)
            except:
                return 'timeout'

    def get_status(self, radiator):
        if radiator in self.radiators.keys():
            try:
                t = Thermostat(self.radiators[radiator])
                t.update()
                answer = '\n'
                answer += '  Locked: ' + str(t.locked) + '\n'
                answer += '  Battery low: ' + str(t.low_battery) + '\n'
                answer += '  Window open: ' + str(t.window_open) + '\n'
                answer += '  Window open temp: ' + self.__print_temp(t.window_open_temperature) + '\n'
                answer += '  Window open time: ' + str(t.window_open_time) + '\n'
                answer += '  Boost: ' + str(t.boost) + '\n'
                answer += '  Current target temp: ' + self.__print_temp(t.target_temperature) + '\n'
                answer += '  Current comfort temp: ' + self.__print_temp(t.comfort_temperature) + '\n'
                answer += '  Current eco temp: ' + self.__print_temp(t.eco_temperature) + '\n'
                answer += '  Valve: ' + str(t.valve_state)
                return answer
            except:
                return 'timeout'

    def __print_temp(self, temperature):
        return str(temperature).replace('(', '\(').replace(')', '\)').replace('.', '\.')