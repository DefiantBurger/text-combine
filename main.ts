input.onButtonPressed(Button.A, function () {
    if (letter >= 2) {
        letter += 0 - 1
    }
})
input.onButtonPressed(Button.AB, function () {
    letter = 0
})
input.onButtonPressed(Button.B, function () {
    if (letter <= 25) {
        letter += 1
    }
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    final = "" + final + String.fromCharCode(letter + 64)
})
let final = ""
let letter = 0
letter = 1
let strlttr = "0"
final = ""
basic.forever(function () {
    basic.clearScreen()
    if (letter != 0) {
        basic.showString(String.fromCharCode(letter + 64))
    } else {
        basic.showString(final)
        letter = 1
        final = ""
    }
})
