# Criado por https://github.com/rodriaum

# Inicia o sistema junto com as variáveis.
strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)

# Loop Interval.
def on_forever():
    if input.light_level() <= 50:
        strip.show_color(NeoPixelColors.PURPLE)
    else
        strip.clear()

# Call the loop function.
basic.forever(on_forever)