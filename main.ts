let strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
basic.forever(function on_forever() {
    if (input.lightLevel() <= 50) {
        strip.showColor(NeoPixelColors.Purple)
    }
    
})
