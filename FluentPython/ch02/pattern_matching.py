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
>>> metro_areas = [
...     ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
...     ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
...     ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
...     ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
...     ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
... ]
...
>>> def main():
...     print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
...     for record in metro_areas:
...         match record:
...             case [name, _, _, (lat, lon)] if lon <= 0:
...                 print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
...
>>> main()
                |  latitude | longitude
Mexico City     |   19.4333 |  -99.1333
New York-Newark |   40.8086 |  -74.0204
São Paulo       |  -23.5478 |  -46.6358

>>> def lisp_evaluate_trial(exp):
...     match exp:
...         case ['lambda', [*parms], *body] if body:
...              print(parms, body)
...         case _:
...              print('Unknow case!')
>>> exp = ['lambda', [1, 2, 3], 'haha', 'lala']
>>> lisp_evaluate_trial(exp)
[1, 2, 3] ['haha', 'lala']
>>> exp = ['lambda', 1, 'haha', 'lala']
>>> lisp_evaluate_trial(exp)
Unknow case!
>>> exp = ['lambda', (1,), 'haha', 'lala']
>>> lisp_evaluate_trial(exp)
[1] ['haha', 'lala']
>>> exp = ['lambda', [], 'haha', 'lala']
>>> lisp_evaluate_trial(exp)
[] ['haha', 'lala']

>>> def simple_lambda_trial(exp):
...     match exp:
...         case ['lambda', parms, *body] if body:
...              print(parms, body)
...         case _:
...              print('Unknow case!')
>>> exp = ['lambda', 'x', ['*', 'x', 2]]
>>> simple_lambda_trial(exp)
x [['*', 'x', 2]]
"""


if __name__ == '__main__':
    import doctest
    doctest.testmod()
