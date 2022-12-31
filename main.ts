radio.setGroup(1)

radio.onReceivedNumber(function (tmp) {
    basic.showNumber(tmp)
})

input.onLogoEvent(TouchButtonEvent.Touched,function(){
    radio.sendString("gt")
})
