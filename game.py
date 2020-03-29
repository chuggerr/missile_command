import random
import turtle
import math


window = turtle.Screen()
window.bgpic('images/background.png')
window.setup(1205, 805)
window.screensize(1200, 800)


BASE_X, BASE_Y = 0, -300


def calc_heading(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    length = (dx ** 2 + dy ** 2) ** 0.5
    cos_alpha = dx / length
    alpha = math.acos(cos_alpha)
    alpha = math.degrees(alpha)
    if dy < 0:
        alpha = -alpha
    return alpha


def fire_missile(x, y):
    missile = turtle.Turtle(visible=False)
    missile.speed(0)
    missile.color('white')
    missile.penup()
    missile.setpos(x=BASE_X, y=BASE_Y)
    missile.pendown()
    heading = calc_heading(x1=BASE_X, y1=BASE_Y, x2=x, y2=y)
    missile.setheading(heading)
    missile.showturtle()
    info = {'missile': missile, 'target': [x, y],
            'state': 'launched', 'radius': 0}
    our_missiles.append(info)


def enemy_missile():
    enemy = turtle.Turtle(visible=False)
    enemy.speed(1)
    enemy.color('red')
    enemy.penup()
    resp_x = random.randint(-600, 600)
    enemy.setpos(x=resp_x, y=400)
    enemy.pendown()
    heading = calc_heading(x1=resp_x, y1=800, x2=BASE_X, y2=BASE_Y)
    enemy.setheading(heading)
    enemy.showturtle()
    enemy.setpos(x=BASE_X, y=BASE_Y)
    enemy.shape('circle')
    enemy_info = {'enemy': enemy, 'target': [BASE_X, BASE_Y],
                  'state': 'launched', 'radius': 0}
    enemy_missiles.append(enemy_info)


window.onclick(fire_missile)

our_missiles = []
enemy_missiles = []

while True:
    window.update()
    enemy_missile()
    # for enemy_info in enemy_missiles:
    #     state = enemy_info['state']
    #     enemy = enemy_info['enemy']
    #     if enemy_info['state'] == 'launched':
    #         enemy.forward(4)
    #         target = enemy_info['target']
    #         if enemy.distance(x=target[0], y=target[1]) < 20:
    #             enemy_info['state'] = 'explode'
    #             enemy.shape('circle')
    #     elif state == 'explode':
    #         enemy_info['radius'] += 1
    #         if enemy_info['radius'] > 5:
    #             enemy.clear()
    #             enemy.hideturtle()
    #             enemy['state'] = 'dead'
    #         else:
    #             enemy.shapesize(enemy_info['radius'])

    for info in our_missiles:
        state = info['state']
        missile = info['missile']
        if info['state'] == 'launched':
            missile.forward(4)
            target = info['target']
            if missile.distance(x=target[0], y=target[1]) < 20:
                info['state'] = 'explode'
                missile.shape('circle')
        elif state == 'explode':
            info['radius'] += 1
            if info['radius'] > 5:
                missile.clear()
                missile.hideturtle()
                info['state'] = 'dead'
            else:
                missile.shapesize(info['radius'])




    dead_missiles = [info for info in our_missiles if info['state'] == 'dead']
    for dead in dead_missiles:
        our_missiles.remove(dead)
