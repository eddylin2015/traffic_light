function TESTING () {
    Tinybit.CarCtrlSpeed2(Tinybit.CarState.Car_Run, 2, 2)
    basic.showString("1")
    basic.pause(60000)
    Tinybit.CarCtrlSpeed2(Tinybit.CarState.Car_Back, 2, 2)
    basic.showString("2")
    basic.pause(60000)
    Tinybit.CarCtrlSpeed2(Tinybit.CarState.Car_SpinLeft, 2, 2)
    basic.showString("3")
    basic.pause(60000)
    Tinybit.CarCtrlSpeed2(Tinybit.CarState.Car_SpinRight, 2, 2)
    basic.showString("4")
    basic.pause(60000)
    Tinybit.CarCtrlSpeed2(Tinybit.CarState.Car_Left, 2, 2)
    basic.showString("5")
    basic.pause(60000)
    Tinybit.CarCtrlSpeed2(Tinybit.CarState.Car_Right, 2, 2)
    basic.showString("6")
    basic.pause(60000)
}
function LightControl (cL: number, wL: number, yL: number) {
    pins.digitalWritePin(DigitalPin.P1, yL)
    if (cL == 1 && wL == 1) {
        Tinybit.CarCtrlSpeed2(Tinybit.CarState.Car_Run, 2, 2)
    } else if (cL == 2 && wL == 2) {
        Tinybit.CarCtrlSpeed2(Tinybit.CarState.Car_Back, 2, 2)
    } else if (cL == 1 && wL == 2) {
        Tinybit.CarCtrlSpeed2(Tinybit.CarState.Car_SpinLeft, 2, 2)
    } else if (cL == 2 && wL == 1) {
        Tinybit.CarCtrlSpeed2(Tinybit.CarState.Car_SpinRight, 2, 2)
    } else if (cL == 1 && wL == 0) {
        Tinybit.CarCtrlSpeed2(Tinybit.CarState.Car_Left, 2, 2)
    } else if (cL == 0 && wL == 1) {
        Tinybit.CarCtrlSpeed2(Tinybit.CarState.Car_Right, 2, 2)
    }
}
basic.forever(function () {
    basic.showLeds(`
        # . . . #
        . # . # .
        . . # . .
        . # . # .
        # . . . #
        `)
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
    basic.showLeds(`
        . . # . .
        . # . # .
        # . . . #
        . # . # .
        . . # . .
        `)
    basic.pause(5000)
})
