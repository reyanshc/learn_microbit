radio.onReceivedNumber(function (receivedNumber) {
    basic.showNumber(receivedNumber)
})
input.onButtonPressed(Button.A, function () {
    radio.sendString(INCREASE)
})
input.onButtonPressed(Button.AB, function () {
    radio.sendString(START_MUSIC)
})
input.onButtonPressed(Button.B, function () {
    radio.sendString(DECREASE)
})
input.onGesture(Gesture.LogoDown, function () {
    radio.sendString(RESET)
    control.reset()
})
let START_MUSIC = ""
let RESET = ""
let DECREASE = ""
let INCREASE = ""
radio.setGroup(1000)
INCREASE = "increase"
DECREASE = "decrease"
RESET = "reset"
START_MUSIC = "start"
