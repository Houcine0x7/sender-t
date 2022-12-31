radio.set_group(1)

def on_button_pressed_a():
    radio.send_string("gt")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_number(onReceivedNumber):
    if onReceivedNumber == input.temperature():
        basic.show_number(input.temperature())
radio.on_received_number(on_received_number)
