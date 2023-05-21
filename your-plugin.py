class YourPluginHelper:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.printer.register_event_handler("klippy:connect", self.handle_connect)

        # Use this to get values from config file
        # config.getlist returns the list defined in the cfg file
        # config.getint returns the integer value instead
        # and so on...
        self.start_pos = config.getlist("start_pos")
        self.end_pos = config.getlist("end_pos")
        self.move_speed = config.getint("move_speed")
        # example config file section in printer.cfg:
        # [your_plugin]
        #   start_pos: 10, 10, 20, 0
        #   end_pos: 50, 50, 40, 0
        #   move_speed: 120

    def handle_connect(self):
       k = self.printer.lookup_object('toolhead').get_kinematics()

    # write main part of the functionality below

    # E.g. move the toolhead from point A to point B
    def do_move(self):
        toolhead = self.printer.lookup_object("toolhead")
        gcode = self.printer.lookup_object('gcode')
        curpos = toolhead.get_position()

        # this line outputs text in the terminal
        gcode.respond_info("Curpos is " + str(curpos))



        # convert to integers
        start_pos = [int(axis) for axis in self.start_pos]
        end_pos = [int(axis) for axis in self.end_pos]
        move_speed = int(self.move_speed)

        # positions are formatted in a list: [x pos, y pos, z pos, extruder pos]

        toolhead.move(start_pos, move_speed)
        toolhead.move(end_pos, move_speed)


class YourPlugin:
    def __init__(self, config):
        self.printer = config.get_printer()
        self.your_plugin_helper = YourPluginHelper(config)
        gcode = self.printer.lookup_object('gcode')

        # make your gcode recognisable
        gcode.register_command("YOUR_GCODE_MACRO", self.cmd_YOUR_GCODE_MACRO, self.cmd_YOUR_GCODE_MACRO_help)


    cmd_YOUR_GCODE_MACRO_help = "Help hint at what this gcode macro does"
    def cmd_YOUR_GCODE_MACRO(self, gcmd):
        self.your_plugin_helper.do_move()
    
def load_config(config):
    return YourPlugin(config)
