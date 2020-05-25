import play
import math


player = play.new_image(image = "car.png", size = 10)
player.start_physics(stable = 1, obeys_gravity = 0, bounciness = 0.2)
speedometer = play.new_text(words = str( int( abs(player.physics.x_speed) + abs(player.physics.x_speed) ) ),
                            x = -350, y = 250, font_size = 40)
vector = [0, 0, player.angle]
speed = 0


@play.when_program_starts
def start():
    pass


@play.repeat_forever
async def do():
    global vector, speed
    vector[0] = math.cos(math.radians(0 - player.angle))
    vector[1] = math.sin(math.radians(0 - player.angle))
    vector[2] = player.angle

    if play.key_is_pressed('w', 'ц') and speed < 30:         # acceleration and back
        speed += 1
    if play.key_is_pressed('s', 'ы') and speed > -30:
        speed -= 1

    if play.key_is_pressed('a', 'ф'):                        # turns
        player.angle = player.angle + abs(speed) * 0.1
    if play.key_is_pressed('d', 'в'):
        player.angle = player.angle - abs(speed) * 0.1

    brake = 0                                           # handbrake
    if play.key_is_pressed("space"):
        brake = 1.5

    if speed > 0:                                       # slow down
        speed -= 0.2 + brake
    elif speed < 0:
        speed += 0.2 + brake

    player.physics.x_speed = speed * vector[1]          # final movement
    player.physics.y_speed = speed * vector[0]
    speedometer.words = str(int( abs(player.physics.x_speed) + abs(player.physics.y_speed) ))


play.start_program()
