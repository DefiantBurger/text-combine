def on_button_pressed_a():
    global letter
    if letter >= 2:
        letter += 0 - 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def numtext(num: number):
    global strlttr
    if num == 1:
        strlttr = "A"
    elif num == 2:
        strlttr = "B"
    elif num == 3:
        strlttr = "C"
    elif num == 4:
        strlttr = "D"
    elif num == 5:
        strlttr = "E"
    elif num == 6:
        strlttr = "F"
    elif num == 7:
        strlttr = "G"
    elif num == 8:
        strlttr = "H"
    elif num == 9:
        strlttr = "I"
    elif num == 10:
        strlttr = "J"
    elif num == 11:
        strlttr = "K"
    elif num == 12:
        strlttr = "L"
    elif num == 13:
        strlttr = "M"
    elif num == 14:
        strlttr = "N"
    elif num == 15:
        strlttr = "O"
    elif num == 16:
        strlttr = "P"
    elif num == 17:
        strlttr = "Q"
    elif num == 18:
        strlttr = "R"
    elif num == 19:
        strlttr = "S"
    elif num == 20:
        strlttr = "T"
    elif num == 21:
        strlttr = "U"
    elif num == 22:
        strlttr = "V"
    elif num == 23:
        strlttr = "W"
    elif num == 24:
        strlttr = "X"
    elif num == 25:
        strlttr = "Y"
    elif num == 26:
        strlttr = "Z"

def on_button_pressed_ab():
    global dispfinal
    dispfinal = 1
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global letter
    if letter <= 25:
        letter += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    global final
    final = "" + final + strlttr
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

letter = 1
strlttr = "0"
final = ""
dispfinal = 0

def on_forever():
    basic.clear_screen()
    numtext(letter)
    if letter != 0:
        basic.show_string(strlttr)
    else:
        basic.show_string(final)
basic.forever(on_forever)
