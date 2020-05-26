import play, math


player = play.new_image(image = "car.png", size = 10)
player.start_physics(stable = 0, obeys_gravity = 0, bounciness = 1, friction = 1)
speedometer = play.new_text(words = str( int( abs(player.physics.x_speed) + abs(player.physics.x_speed) ) ),
                            x = -350, y = 250, font_size = 40)
player.ang = 0
player.speed = 0
player.max_speed = 30
player.vector = [0, 0]

box1 = play.new_box(x = -200)
box1.start_physics(stable = 1, obeys_gravity = 0)



@play.when_program_starts
def start():
    pass


@play.repeat_forever
async def do():
    player.angle = player.ang
    player.vector[0] = math.cos(math.radians(-player.angle))
    player.vector[1] = math.sin(math.radians(-player.angle))

    if play.key_is_pressed('w', 'ц') and player.speed < player.max_speed:  # acceleration and back
        player.speed += 1
    if play.key_is_pressed('s', 'ы') and player.speed > -player.max_speed:
        player.speed -= 1

    if play.key_is_pressed('a', 'ф'):                                      # turns
        player.turn(0.1 * abs(player.speed))
    if play.key_is_pressed('d', 'в'):
        player.turn(-0.1 * abs(player.speed))
    player.ang = player.angle

    brake = 0                                                              # handbrake 1/2
    if play.key_is_pressed("space"):
        brake = 1.5

    if player.speed > 0:                                                   # slow down
        player.speed -= 0.2 + brake
    elif player.speed < 0:
        player.speed += 0.2 + brake

    if play.key_is_pressed("space"):                                       # handbrake 2/2
        player.speed *= 0.99
        if abs(player.speed) < 0.2:
            player.speed = 0

    player.physics.x_speed = player.speed * player.vector[1]              # final movement
    player.physics.y_speed = player.speed * player.vector[0]
    speedometer.words = str(int( abs(player.physics.x_speed) + abs(player.physics.y_speed) ))

    #await play.timer(seconds = 1/60)

play.start_program()
