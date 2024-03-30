def on_forever():
    basic.show_number(pins.analog_read_pin(AnalogPin.P1))
basic.forever(on_forever)
