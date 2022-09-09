@namespace
class SpriteKind:
    h = SpriteKind.create()
    Point = SpriteKind.create()

def on_overlap_tile(sprite, location):
    tiles.set_tile_at(location, sprites.builtin.forest_tiles10)
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        d
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    tiles.set_tile_at(location2, sprites.builtin.forest_tiles10)
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        e
    """),
    on_overlap_tile2)

def on_overlap_tile3(sprite3, location3):
    tiles.set_tile_at(location3, sprites.builtin.forest_tiles10)
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        s
    """),
    on_overlap_tile3)

def Splash_Screen():
    global play_game
    scene.set_background_image(assets.image("""
        homepage_background
    """))
    game.splash("PLAY GAME (Press SPACEBAR)")
    game.show_long_text("Aren't houses super expensive?\\n \\n I can't even understand half of these contracts!\\n \\n So many RESTRICTIONS. If only I was more familiar....",
        DialogLayout.FULL)
    game.splash("Instructions : You must catch all the letters to discover the secret word , before the timer runs out . You only have 3 lives and must complete the game before the timer runs out OTHERWISE you will loose a point")
    play_game = True

def on_a_pressed():
    human.vy = -300
    music.set_volume(14)
    music.jump_up.play()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile4(sprite4, location4):
    tiles.set_tile_at(location4, sprites.builtin.forest_tiles10)
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        a
    """),
    on_overlap_tile4)

def on_countdown_end():
    info.change_life_by(-1)
    for index in range(2):
        info.start_countdown(20)
info.on_countdown_end(on_countdown_end)

def on_overlap_tile5(sprite5, location5):
    tiles.set_tile_at(location5, sprites.builtin.forest_tiles10)
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        n
    """),
    on_overlap_tile5)

def on_overlap_tile6(sprite6, location6):
    global level
    if info.score() == 9:
        game.set_dialog_frame(img("""
            ..................................................................
                        ............fff........fff.............fff..............ffff......
                        ...........fddbf......fbdbf...........fbdbf............fbddf......
                        ...........fddbbf.....fdddffff........fdddffff...fff..ffddbff.....
                        ...........fddddffffffbdddbddbffffffffbdddbddbffffddffddddddf.....
                        ...fff....fdddddfddddddddbbddddddddddddddbbddddddfdddddbccddf.....
                        .fffddf..fddffffddddddddddbbddddddddddddddbbdddddffbddbbddff......
                        .fdbddfffddfffdddfffffbdddbddbffffffffbdddbddbfffefddccbddf.......
                        .fdddcddddffeffffeeeeefbdbfddfeeeeeeeefbdbfddfeeeefffcddddf.......
                        .fbddcddddfeeeeeeeeeeeefffffffeeeeeeeeefffffffeeeeeeefdddddf......
                        ..ffdbbbddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffddf.....
                        ...fddbcddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffddfff..
                        ....fddccffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffddddf.
                        ....fdddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffddddf.
                        ...fddbdfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdfddbbf.
                        ...fddfffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdfddbf..
                        ...ffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddfff...
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ...fbddbffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ...fdddddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ...fddbddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbddbff..
                        ..ffbbbbffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbdddddbf.
                        .fbddbddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdddddddf.
                        .fdddddddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbddbddbf.
                        .fbdddddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffbbbbff..
                        ..ffbddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddbddf...
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdddddf...
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffbddbf...
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ...fbddbffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ...fdddddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ...fddbddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbddbff..
                        ..ffbbbbffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbdddddbf.
                        .fbddbddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdddddddf.
                        .fdddddddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbddbddbf.
                        .fbdddddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffbbbbff..
                        ..ffbddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddbddf...
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdddddf...
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffbddbf...
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ...fffddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffff...
                        ..fbddfdfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffddf...
                        .fbbddfdfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdbddf...
                        .fddddfffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdddf....
                        .fddddffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffccddf....
                        ..fffddffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddcbddf...
                        .....fddfffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddbbbdff..
                        ......fdddddfeeeeeeefffffffeeeeeeeeefffffffeeeeeeeeeeeefddddcddbf.
                        .......fddddcfffeeeefddfbdbfeeeeeeeefddfbdbfeeeeeffffeffddddcdddf.
                        .......fddbccddfefffbddbdddbffffffffbddbdddbfffffdddfffddfffddbdf.
                        ......ffddbbddbffdddddbbddddddddddddddbbddddddddddffffddf..fddfff.
                        .....fddccbdddddfddddddbbddddddddddddddbbddddddddfdddddf....fff...
                        .....fddddddffddffffbddbdddbffffffffbddbdddbffffffddddf...........
                        .....ffbddff..fff...ffffdddf........ffffdddf.....fbbddf...........
                        ......fddbf............fbdbf...........fbdbf......fbddf...........
                        ......ffff..............fff.............fff........fff............
                        ..................................................................
        """))
        game.show_long_text("Level 1: COMPLETE\\n \\n You gained knowledge on STAMP DUTY.\\n \\n Definition:\\n \\n A tax applied on legal documents to record monetary exchange.",
            DialogLayout.FULL)
        game.show_long_text("Continue to next level?\\n \\n Press SPACEBAR on your keyboard\\n \\n or\\n \\n 'A' on screen",
            DialogLayout.FULL)
        level = False
        Level_2()
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_closed,
    on_overlap_tile6)

def on_overlap_tile7(sprite7, location7):
    tiles.set_tile_at(location7, sprites.builtin.forest_tiles10)
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        c
    """),
    on_overlap_tile7)

def on_overlap_tile8(sprite8, location8):
    tiles.set_tile_at(location8, sprites.builtin.forest_tiles10)
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        u
    """),
    on_overlap_tile8)

def on_overlap_tile9(sprite9, location9):
    tiles.set_tile_at(location9, sprites.builtin.forest_tiles10)
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        o
    """),
    on_overlap_tile9)

def on_overlap_tile10(sprite10, location10):
    tiles.set_tile_at(location10, sprites.builtin.forest_tiles10)
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        m
    """),
    on_overlap_tile10)

def on_overlap_tile11(sprite11, location11):
    tiles.set_tile_at(location11, sprites.builtin.forest_tiles10)
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        p_letter
    """),
    on_overlap_tile11)

def on_overlap_tile12(sprite12, location12):
    tiles.set_tile_at(location12, sprites.builtin.forest_tiles10)
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        t
    """),
    on_overlap_tile12)

def on_overlap_tile13(sprite13, location13):
    tiles.set_tile_at(location13, sprites.builtin.forest_tiles10)
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        v
    """),
    on_overlap_tile13)

def on_overlap_tile14(sprite14, location14):
    tiles.set_tile_at(location14, sprites.builtin.forest_tiles10)
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        t_letter2
    """),
    on_overlap_tile14)

def on_overlap_tile15(sprite15, location15):
    tiles.set_tile_at(location15, sprites.builtin.forest_tiles10)
    info.change_score_by(1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        y
    """),
    on_overlap_tile15)

def Level_2():
    tiles.set_current_tilemap(tilemap("""
        level2
    """))
    info.set_life(3)
    info.set_score(0)
    human.set_position(130, 640)
    controller.move_sprite(human, 100, 0)
    human.ay = 500
    scene.camera_follow_sprite(human)
    info.start_countdown(60)

def on_overlap_tile16(sprite16, location16):
    if info.score() == 8:
        game.set_dialog_frame(img("""
            ..................................................................
                        ............fff........fff.............fff..............ffff......
                        ...........fddbf......fbdbf...........fbdbf............fbddf......
                        ...........fddbbf.....fdddffff........fdddffff...fff..ffddbff.....
                        ...........fddddffffffbdddbddbffffffffbdddbddbffffddffddddddf.....
                        ...fff....fdddddfddddddddbbddddddddddddddbbddddddfdddddbccddf.....
                        .fffddf..fddffffddddddddddbbddddddddddddddbbdddddffbddbbddff......
                        .fdbddfffddfffdddfffffbdddbddbffffffffbdddbddbfffefddccbddf.......
                        .fdddcddddffeffffeeeeefbdbfddfeeeeeeeefbdbfddfeeeefffcddddf.......
                        .fbddcddddfeeeeeeeeeeeefffffffeeeeeeeeefffffffeeeeeeefdddddf......
                        ..ffdbbbddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffffddf.....
                        ...fddbcddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffddfff..
                        ....fddccffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffddddf.
                        ....fdddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffddddf.
                        ...fddbdfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdfddbbf.
                        ...fddfffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdfddbf..
                        ...ffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddfff...
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ...fbddbffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ...fdddddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ...fddbddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbddbff..
                        ..ffbbbbffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbdddddbf.
                        .fbddbddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdddddddf.
                        .fdddddddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbddbddbf.
                        .fbdddddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffbbbbff..
                        ..ffbddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddbddf...
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdddddf...
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffbddbf...
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ...fbddbffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ...fdddddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ...fddbddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbddbff..
                        ..ffbbbbffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbdddddbf.
                        .fbddbddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdddddddf.
                        .fdddddddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefbddbddbf.
                        .fbdddddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffbbbbff..
                        ..ffbddbfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddbddf...
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdddddf...
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffbddbf...
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ....fddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddf....
                        ...fffddfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffff...
                        ..fbddfdfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefffddf...
                        .fbbddfdfeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdbddf...
                        .fddddfffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefdddf....
                        .fddddffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeffccddf....
                        ..fffddffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddcbddf...
                        .....fddfffffeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeefddbbbdff..
                        ......fdddddfeeeeeeefffffffeeeeeeeeefffffffeeeeeeeeeeeefddddcddbf.
                        .......fddddcfffeeeefddfbdbfeeeeeeeefddfbdbfeeeeeffffeffddddcdddf.
                        .......fddbccddfefffbddbdddbffffffffbddbdddbfffffdddfffddfffddbdf.
                        ......ffddbbddbffdddddbbddddddddddddddbbddddddddddffffddf..fddfff.
                        .....fddccbdddddfddddddbbddddddddddddddbbddddddddfdddddf....fff...
                        .....fddddddffddffffbddbdddbffffffffbddbdddbffffffddddf...........
                        .....ffbddff..fff...ffffdddf........ffffdddf.....fbbddf...........
                        ......fddbf............fbdbf...........fbdbf......fbddf...........
                        ......ffff..............fff.............fff........fff............
                        ..................................................................
        """))
        game.show_long_text("Level 2: COMPLETE\\n \\n You gained knowledge on COVENANT.\\n \\n Definition:\\n \\n A tax applied on legal documents to record monetary exchange.",
            DialogLayout.FULL)
scene.on_overlap_tile(SpriteKind.player,
    sprites.dungeon.chest_open,
    on_overlap_tile16)

human: Sprite = None
level = False
play_game = False
hitting = False
play_game = False
level = True
Splash_Screen()
if play_game:
    if level == True:
        info.set_life(3)
        tiles.set_current_tilemap(tilemap("""
            level1
        """))
        info.set_score(0)
        human = sprites.create(assets.image("""
            human
        """), SpriteKind.player)
        human.set_position(150, 462)
        controller.move_sprite(human, 100, 0)
        human.ay = 500
        scene.camera_follow_sprite(human)
        info.start_countdown(60)

def on_on_update():
    global hitting
    if True:
        if human.is_hitting_tile(CollisionDirection.BOTTOM):
            if not (hitting):
                music.set_volume(25)
                music.pew_pew.play()
            hitting = True
        else:
            hitting = False
game.on_update(on_on_update)
