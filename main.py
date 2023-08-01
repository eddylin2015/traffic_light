def TESTING():
    Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_RUN, 2, 2)
    basic.show_string("1")
    basic.pause(60000)
    Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_BACK, 2, 2)
    basic.show_string("2")
    basic.pause(60000)
    Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_SPINLEFT, 2, 2)
    basic.show_string("3")
    basic.pause(60000)
    Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_SPINRIGHT, 2, 2)
    basic.show_string("4")
    basic.pause(60000)
    Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_LEFT, 2, 2)
    basic.show_string("5")
    basic.pause(60000)
    Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_RIGHT, 2, 2)
    basic.show_string("6")
    basic.pause(60000)
def LightControl(cL: number, wL: number, yL: number):
    pins.digital_write_pin(DigitalPin.P1, yL)
    if cL == 1 and wL == 1:
        Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_RUN, 2, 2)
    elif cL == 2 and wL == 2:
        Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_BACK, 2, 2)
    elif cL == 1 and wL == 2:
        Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_SPINLEFT, 2, 2)
    elif cL == 2 and wL == 1:
        Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_SPINRIGHT, 2, 2)
    elif cL == 1 and wL == 0:
        Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_LEFT, 2, 2)
    elif cL == 0 and wL == 1:
        Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_RIGHT, 2, 2)

def on_forever():
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        """)
    LightControl(1, 1, 0)
    basic.pause(2000)
    LightControl(1, 1, 1)
    basic.pause(2000)
    LightControl(2, 1, 0)
    basic.pause(5000)
    LightControl(0, 1, 1)
    basic.pause(2000)
    LightControl(1, 1, 0)
    basic.pause(2000)
    LightControl(1, 2, 0)
    basic.show_leds("""
        . . # . .
        . # . # .
        # . . . #
        . # . # .
        . . # . .
        """)
    basic.pause(5000)
basic.forever(on_forever)
