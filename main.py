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
def car_green():
    Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_RUN, 2, 2)
    basic.show_leds("""
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(60000)
    Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_BACK, 2, 2)
    basic.show_leds("""
        # # . . .
        # . . . .
        . # . . .
        . . . . .
        . . . . .
        """)
    basic.pause(60000)
    Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_SPINLEFT, 2, 2)
    basic.show_leds("""
        # # # . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(60000)
    Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_SPINRIGHT, 2, 2)
    basic.show_leds("""
        # # # # .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(60000)
    Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_LEFT, 2, 2)
    basic.show_leds("""
        # # # # #
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(60000)
    Tinybit.car_ctrl_speed2(Tinybit.CarState.CAR_RIGHT, 2, 2)
    basic.show_leds("""
        # # # # #
        # . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(60000)

def on_forever():
    LightControl(1, 1, 0)
    basic.show_leds("""
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        """)
    basic.pause(2000)
    LightControl(2, 1, 1)
    basic.pause(2000)
    LightControl(2, 1, 0)
    basic.pause(2000)
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
    basic.pause(2000)
basic.forever(on_forever)
