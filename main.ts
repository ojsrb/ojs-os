namespace SpriteKind {
    export const icon = SpriteKind.create()
}

console.log("Starting")
controller.up.onEvent(ControllerButtonEvent.Pressed, function on_up_pressed() {
    
    if (selectorY > 20) {
        selectorY += 0 - 20
        selectorApp += 0 - 7
    }
    
    clickSound()
})
function clickSound() {
    music.setVolume(volume_level)
    music.play(music.createSoundEffect(WaveShape.Sine, 500, 500, 154, 154, 25, SoundExpressionEffect.None, InterpolationCurve.Curve), music.PlaybackMode.InBackground)
}

controller.A.onEvent(ControllerButtonEvent.Pressed, function on_a_pressed() {
    if (selectorApp == 0) {
        colorsApp()
    } else if (selectorApp == 1) {
        startApp()
        volumeApp()
        closeApp()
    } else if (selectorApp == 34) {
        startApp()
        credits()
        closeApp()
    } else {
        
    }
    
    closeApp()
    clickSound()
})
function credits() {
    game.splash("Credits", "Created by Owen J Schmidt")
}

controller.left.onEvent(ControllerButtonEvent.Pressed, function on_left_pressed() {
    
    if (selectorY == 20 && selectorX == 20) {
        
    } else {
        selectorX += 0 - 20
        selectorApp += 0 - 1
    }
    
    if (selectorX == 0 && selectorY != 20) {
        selectorX = 140
        selectorY += 0 - 20
    }
    
    clickSound()
})
function closeApp() {
    
    color.setFlag(SpriteFlag.Invisible, false)
    selector.setFlag(SpriteFlag.Invisible, false)
    logo.setFlag(SpriteFlag.Invisible, false)
    selectorX = 20
    selectorY = 20
    selectorApp = 0
    volume.setFlag(SpriteFlag.Invisible, false)
}

controller.right.onEvent(ControllerButtonEvent.Pressed, function on_right_pressed() {
    
    selectorX += 20
    if (selectorX == 160) {
        selectorX = 20
        selectorY += 20
    }
    
    selectorApp += 1
    if (selectorY > 100) {
        selectorY = 100
        selectorX = 140
        selectorApp = 34
    }
    
    clickSound()
})
function colorsApp() {
    scene.setBackgroundColor(scene.backgroundColor() + 1)
}

controller.down.onEvent(ControllerButtonEvent.Pressed, function on_down_pressed() {
    
    if (selectorY < 100) {
        selectorY += 20
        selectorApp += 7
    }
    
    if (selectorY > 100) {
        selectorY = 100
        selectorX = 140
        selectorApp = 34
    }
    
    clickSound()
})
function setIconLocations() {
    
    selectorX = 20
    selectorY = 20
    selectorApp = 0
}

function volumeApp() {
    
    volume_level = game.askForNumber("Volume Level (0-255)", 3)
    music.setVolume(volume_level)
    music.play(music.stringPlayable("C D F E C D G F ", 315), music.PlaybackMode.InBackground)
    blockSettings.writeNumber("volume", volume_level)
}

function startApp() {
    color.setFlag(SpriteFlag.Invisible, true)
    selector.setFlag(SpriteFlag.Invisible, true)
    logo.setFlag(SpriteFlag.Invisible, true)
    volume.setFlag(SpriteFlag.Invisible, true)
}

let selectorApp = 0
let volume : Sprite = null
let color : Sprite = null
let selector : Sprite = null
let logo : Sprite = null
let volume_level = 0
let selectorX = 0
let selectorY = 0
selectorY = 20
selectorX = 20
music.setVolume(blockSettings.readNumber("volume"))
scene.setBackgroundColor(15)
logo = sprites.create(assets.image`
    OJS-TECH-LOGO
`, SpriteKind.icon)
effects.blizzard.startScreenEffect(2740)
music.play(music.stringPlayable("C D F E C D G F ", 175), music.PlaybackMode.UntilDone)
sprites.destroy(logo)
logo = sprites.create(assets.image`
    OJS-LOGO
`, SpriteKind.Player)
logo.setPosition(140, 100)
logo.z = 1
selector = sprites.create(assets.image`
    SELECTOR
`, SpriteKind.icon)
selector.setPosition(20, 20)
selector.z = 0
selector.scale = 1.25
selector.setStayInScreen(true)
scene.setBackgroundColor(15)
color = sprites.create(assets.image`
    COLORS-APP-ICON
`, SpriteKind.icon)
color.setPosition(20, 20)
color.z = 1
volume = sprites.create(assets.image`
    VOLUME-APP-ICON
`, SpriteKind.icon)
volume.setPosition(40, 20)
volume.z = 1
setIconLocations()
forever(function on_forever() {
    selector.setPosition(selectorX, selectorY)
})
