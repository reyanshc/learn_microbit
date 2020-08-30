def on_received_number(receivedNumber):
    basic.show_number(receivedNumber)
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_string("" + (INCREASE))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    radio.send_string("" + (RESET))
    control.reset()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    radio.send_string("" + (DECREASE))
input.on_button_pressed(Button.B, on_button_pressed_b)

RESET = ""
DECREASE = ""
INCREASE = ""
radio.set_group(1000)
INCREASE = "increase"
DECREASE = "decrease"
RESET = "reset"
START_MUSIC = "start"