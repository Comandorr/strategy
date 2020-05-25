import play

player = play.new_box(width = 25, height = 40)
player.start_physics(obeys_gravity = 0, bounciness = 0.2)

@play.when_program_starts
def start():
    pass



@play.repeat_forever
async def do():

    if player.physics.x_speed < 0:
        player.physics.x_speed += 1
    if player.physics.x_speed > 0:
        player.physics.x_speed -= 1
    if player.physics.y_speed < 0:
        player.physics.y_speed += 1
    if player.physics.y_speed > 0:
        player.physics.y_speed -= 1

    if play.key_is_pressed('w') and player.physics.y_speed < 30:
        player.physics.y_speed += 2
    if play.key_is_pressed('s') and player.physics.y_speed > -30:
        player.physics.y_speed -= 2
    if play.key_is_pressed('a') and player.physics.x_speed > -30:
        player.physics.x_speed -= 2
    if play.key_is_pressed('d') and player.physics.x_speed < 30:
        player.physics.x_speed += 2

    print("x_speed : " + str(player.physics.x_speed))
    print("y_speed : " + str(player.physics.y_speed))

play.start_program()
