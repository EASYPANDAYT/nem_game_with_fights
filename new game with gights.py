from random import randint
player_name = 'Вася Питонов'
player_level = 10
player_xp = 0
player_hp = 100 * player_level
player_money = 5

while True:
    print ('1 - Начать сражение')
    print ('2 - Сыграть в кости')
    print ('3 - Отправиться в трактир')
    print ('4 - Уехать')
    retry = input ('Введите номер ответа и нажмите Enter ')
    if retry == '1' :
        enemy_name = 'Жран Кривой'
        enemy_level = 10
        enemy_xp = 0
        enemy_hp = 100 * enemy_level
        print (player_name, 'вышел на бой с ', enemy_name)
        while True :
            input ('Нажмите ENTER, чтобы продолжать бой ')
            player_attack = randint (0, 10) * player_level
            enemy_hp -= player_attack
            print (player_name, 'ударил', enemy_name, 'на', player_attack, 'жизней')
            print ('У', enemy_name, 'стало', enemy_hp, 'жизней')
            if enemy_hp <= 0 :
                print( enemy_name, 'погиб')
                player_xp += enemy_level
                print (player_name, 'получил', player_xp, 'опыта')
                if player_xp % 10 == 0:
                    player_level += player_xp // 10
                    player_xp += enemy_level % 10
                    print (player_name, 'получил', player_level, 'уровень')
                    player_hp = player_hp
                #hp+= 100 * lvl lvlup+1
                    #todo добавить здоровья по штуке за каждый лвлап х 100
                    
                break
            enemy_attack = randint (0, 10) * enemy_level
            player_hp -= enemy_attack
            print (enemy_name, 'ударил', player_name, 'на', enemy_attack, 'жизней')
            print ('У', player_name, 'стало', player_hp, 'жизней')
            if player_hp <= 0 :
                print( player_name, 'погиб')
                break
    elif retry == '2':
        while True:
            print ('---------------------------')
            print ('1 - Сделать ставку')
            print ('2 - Уехать')
            casino = input ('Введите номер ответа и нажмите Enter: ')
            print ('---------------------------')
            if casino == '2' :
                print (player_name, 'уехал')
                break
            if player_money <= 0 :
                print ('У', player_name, 'недостаточно денег')
                break
            print ('У', player_name, player_money ,'денег')
            bet =int ( input ('Сколько поставить?: '))
            if bet > player_money :
                print ('У', player_name, 'нет столько денег')
                continue
            if bet <= 0 :
                print ('Ставка должна быть больше 0')
                continue
            player_score = randint (2, 12)
            enemy_score = randint (2, 12)
            print (player_name, 'выбросил', player_score)
            print ('Соперник выбросил', enemy_score)
            if player_score > enemy_score :
                player_money += bet
                print (player_name, 'выиграл', bet)
                print ('У', player_name, player_money ,'денег')
            if player_score < enemy_score :
                player_money -= bet
                print (player_name, 'проиграл', bet)
                print ('У', player_name, player_money ,'денег')
            if player_score == enemy_score :
                print ('Ничья')
#магазин
    elif retry == '3':
        while True :
            print ('---------------------------')
            print ('1 - Купить зелье восстановления (10 монет)')
            print ('2 - Поговорить с торговцем')
            print ('3 - Уехать')
            tavern = input ('Введите номер ответа и нажмите Enter: ')
            print ('---------------------------')
            if tavern == '1' :
                
                





         if casino == '3' :
                        print (player_name, 'ушел из трактира')
                        break
    elif retry == '4' :
        print (player_name, 'уехал')
        break
print ('Игра окончена')


