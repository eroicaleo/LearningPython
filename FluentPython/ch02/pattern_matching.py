"""
>>> def handle_command(message):
...     match message:
...         case ['BEEPER', frequency, times]:
...             self.beep(times, frequency)
...         case ['NECK', angle]:
...             self.rotate_neck(angle)
...         case ['LED', ident, intensity]:
...             self.leds[ident].set_brightness(ident, intensity)
...         case ['LED', ident, red, green, blue]:
...             self.leds[ident].set_color(ident, red, green, blue)
...         case _:
...             raise InvalidCommand(message)
...

"""


if __name__ == '__main__':
    import doctest
    doctest.testmod()
