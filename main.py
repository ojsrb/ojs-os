print("Hello World")
print("Hello Brian")
@namespace
class SpriteKind:
    icon = SpriteKind.create()
console.log("Starting")
def on_up_pressed():
    global selectorY, selectorApp
    if selectorY > 20:
        selectorY += 0 - 20
        selectorApp += 0 - 7
    clickSound()
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def clickSound():
    music.set_volume(volume_level)
    music.play(music.create_sound_effect(WaveShape.SINE,
            500,
            500,
            154,
            154,
            25,
            SoundExpressionEffect.NONE,
            InterpolationCurve.CURVE),
        music.PlaybackMode.IN_BACKGROUND)

def on_a_pressed():
    if selectorApp == 0:
        colorsApp()
    elif selectorApp == 1:
        startApp()
        volumeApp()
        closeApp()
    elif selectorApp == 34:
        startApp()
        credits()
        closeApp()
    else:
        pass
    closeApp()
    clickSound()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def credits():
    game.splash("Credits", "Created by Owen J Schmidt")

def on_left_pressed():
    global selectorX, selectorApp, selectorY
    if selectorY == 20 and selectorX == 20:
        pass
    else:
        selectorX += 0 - 20
        selectorApp += 0 - 1
    if selectorX == 0 and selectorY != 20:
        selectorX = 140
        selectorY += 0 - 20
    clickSound()
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def closeApp():
    global selectorX, selectorY, selectorApp
    color.set_flag(SpriteFlag.INVISIBLE, False)
    selector.set_flag(SpriteFlag.INVISIBLE, False)
    logo.set_flag(SpriteFlag.INVISIBLE, False)
    selectorX = 20
    selectorY = 20
    selectorApp = 0
    volume.set_flag(SpriteFlag.INVISIBLE, False)

def on_right_pressed():
    global selectorX, selectorY, selectorApp
    selectorX += 20
    if selectorX == 160:
        selectorX = 20
        selectorY += 20
    selectorApp += 1
    if selectorY > 100:
        selectorY = 100
        selectorX = 140
        selectorApp = 34
    clickSound()
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def colorsApp():
    scene.set_background_color(scene.background_color() + 1)

def on_down_pressed():
    global selectorY, selectorApp, selectorX
    if selectorY < 100:
        selectorY += 20
        selectorApp += 7
    if selectorY > 100:
        selectorY = 100
        selectorX = 140
        selectorApp = 34
    clickSound()
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def setIconLocations():
    global selectorX, selectorY, selectorApp
    selectorX = 20
    selectorY = 20
    selectorApp = 0
def volumeApp():
    global volume_level
    volume_level = game.ask_for_number("Volume Level (0-255)", 3)
    music.set_volume(volume_level)
    music.play(music.string_playable("C D F E C D G F ", 315),
        music.PlaybackMode.IN_BACKGROUND)
    blockSettings.write_number("volume", volume_level)
def startApp():
    color.set_flag(SpriteFlag.INVISIBLE, True)
    selector.set_flag(SpriteFlag.INVISIBLE, True)
    logo.set_flag(SpriteFlag.INVISIBLE, True)
    volume.set_flag(SpriteFlag.INVISIBLE, True)
selectorApp = 0
volume: Sprite = None
color: Sprite = None
selector: Sprite = None
logo: Sprite = None
volume_level = 0
selectorX = 0
selectorY = 0
selectorY = 20
selectorX = 20
music.set_volume(blockSettings.read_number("volume"))
scene.set_background_color(15)
logo = sprites.create(assets.image("""
    OJS-TECH-LOGO
"""), SpriteKind.icon)
effects.blizzard.start_screen_effect(2740)
music.play(music.string_playable("C D F E C D G F ", 175),
    music.PlaybackMode.UNTIL_DONE)
sprites.destroy(logo)
logo = sprites.create(assets.image("""
    OJS-LOGO
"""), SpriteKind.player)
logo.set_position(140, 100)
logo.z = 1
selector = sprites.create(assets.image("""
    SELECTOR
"""), SpriteKind.icon)
selector.set_position(20, 20)
selector.z = 0
selector.scale = 1.25
selector.set_stay_in_screen(True)
scene.set_background_color(15)
color = sprites.create(assets.image("""
    COLORS-APP-ICON
"""), SpriteKind.icon)
color.set_position(20, 20)
color.z = 1
volume = sprites.create(assets.image("""
    VOLUME-APP-ICON
"""), SpriteKind.icon)
volume.set_position(40, 20)
volume.z = 1
setIconLocations()

def on_forever():
    selector.set_position(selectorX, selectorY)
forever(on_forever)
