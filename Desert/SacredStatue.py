# http://codecombat.com/play/level/sacred-statue?session=56c5ebfded946a44004fb659&observing=true
# Прогуляйтесь вокруг позиций огров, уничтожайте каждого врага, что повстречаете на своем пути.
# Посетите статую, что бы начать бой.
while True:
    # Удерживайте позици и победите атакующих огров.
    enemy = hero.findNearest(hero.findEnemies())
    if enemy and hero.health > hero.maxHealth / 3:
        hero.attack(enemy)
    else:
        hero.moveXY(60, 65)  # Подсказка: в бою держитесь рядом со статуей, она окажет поддержку во время сражения.

    # После того как вы одержите победу над ограми, вам предстоит сразиться с Древним Циклопом!
