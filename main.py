밝기 = 0

def on_forever():
    global 밝기
    밝기 = pins.analog_read_pin(AnalogPin.P1)
    if True:
        pass
    else:
        pass
basic.forever(on_forever)
