from random import randint
player_name = 'Вася Питонов'
player_level = 10
player_xp = 0
player_hp = 100 * player_level
player_money = 0

while True:
    print ('1 - начать сражение')
    print ('2 - сыграть в кости')
    print ('3 - уехать')
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
                break
            enemy_attack = randint (0, 10) * enemy_level
            player_hp -= enemy_attack
            print (enemy_name, 'ударил', player_name, 'на', enemy_attack, 'жизней')
            print ('У', player_name, 'стало', player_hp, 'жизней')
            if player_hp <= 0 :
                print( player_name, 'погиб')
                break
    elif retry == '2':
        print ('У', player_name , player_money , 'денег')
        bet = input ('Сколько поставить: ')
        if bet <= 0 and bet > player_money :
            print ('Ставка недействительна')
        else :
            bet = randint (1, 2)
        if bet == 1:
            print ('Вы победили')
            player_money = player_money * 2
            print ('У тебя осталось', player_money, 'денег')
        elif player_2 > player_1:
            print ('Компьютер победил')
            chips = chips - 25
            print ('У тебя осталось', chips, 'фишек')
        else :
            print ('Ничья')
        








    elif retry == '3' :
        print (player_name, 'уехал')
        break
print ('Бой окончен')


