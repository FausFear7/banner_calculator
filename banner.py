import time

COAST = [[300, 270, 250], [350, 320, 300], [400, 380, 360]]
SIZING = 60
GROMMET = 30
calc = True
discount = 0
number_s = 0

print("""                                             
                  ______                             
                  | ___ \                            
                  | |_/ / __ _ _ __  _ __   ___ _ __ 
                  | ___ \/ _` | '_ \| '_ \ / _ \ '__|
                  | |_/ / (_| | | | | | | |  __/ |   
                  \____/ \__,_|_| |_|_| |_|\___|_|   

             _____       _            _       _             
            /  __ \     | |          | |     | |            
            | /  \/ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
            | |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
            | \__/\ (_| | | (__| |_| | | (_| | || (_) | |   
             \____/\__,_|_|\___|\__,_|_|\__,_|\__\___/|_| 
                                                                           """)
while calc:

    print("------------------------------------------------------------")
    print("-------------->ПРИМЕР ВВОДА: 3000 1500 3 40<----------------")
    print("------------>ВСЕ ДАННЫЕ ОБЯЗАТЕЛЬНЫ ДЛЯ ВВОДА!<-------------")
    print("------------------------------------------------------------")
    print("------------------------------------------------------------")
    size = list(input("Введите ширину, высоту в ММ, плотность "
                              "(3, 4, 5), расстояние между люверсами в СМ ЧЕРЕЗ ПРОБЕЛ: \n").split())

    if size == ["exit"]:
        print("Выход из программы через 'exit'")
        calc = False
        continue

    if len(size) != 4:
        print("------------Ошибка! Введите правильные данные!--------------".upper())
        number_s += 1
        if number_s == 3:
            print("Слишком много раз введено неверное значение! Выход из цикла")
            calc = False
        continue

    if size[3] == "0":
        print("------------Ошибка! Введите правильные данные!--------------".upper())
        number_s += 1
        if number_s == 3:
            print("Слишком много раз введено неверное значение! Выход из цикла")
            calc = False
        continue



    density_banner = int(size[2]) - 3
    square_banner = (int(size[0]) * int(size[1])) / 1000000

    if 18 > square_banner > 15:
        discount = 1
    elif square_banner > 18:
        discount = 2
    else:
        discount = 0

    coast_banner = round(square_banner * COAST[density_banner][discount] + 49, -2)
    perimeter_banner = (int(size[0]) + int(size[1])) * 2 / 1000
    number_of_grommets = round(perimeter_banner * 100 / int(size[3]))

    if number_of_grommets % 2 != 0:
        number_of_grommets -= 1

    coast_sizing = round(perimeter_banner * SIZING + 49, -2)
    coast_sizing_banner = coast_sizing + coast_banner
    coast_grommet = number_of_grommets * GROMMET
    coast_grommet_banner = coast_sizing + coast_banner + coast_grommet


    print("**********************************************************")
    print("Стоимость дизайна не входит в итоговые цены".upper())
    print("----------------------------------------------------------")
    print(f"Стоимость распечатки баннера {size[0]}х{size[1]}мм: {coast_banner} руб.")
    print(f"Стоимость баннера с проклейкой: {coast_sizing_banner} руб.")
    print(f"Стоимость баннера с проклейкой, люверсами: {coast_grommet_banner} руб.")
    print("----------------------------------------------------------")
    print(f"Стоимость проклейки: {coast_sizing} руб.")
    print(f"Стоимость люверсов: {coast_grommet} руб.")
    print(f"Стоимость квадратного метра: {COAST[density_banner][discount]} руб.")
    print("----------------------------------------------------------")
    print(f"Площадь баннера м2: {square_banner}")
    print(f"Периметр баннера м: {perimeter_banner}")
    print(f"Количество люверсов: {number_of_grommets}")
    print("----------------------------------------------------------")
    print("**********************************************************")
    yes_no = input("Хотите посчитать ещё баннер? Введите 'Да', либо любую кнопу для выхода из программы: ").lower()
    if yes_no == "да" or yes_no == "lf":
        calc = True
        print("\n" * 30)
    else:
        calc = False

print("Программа завершила свою работу")
time.sleep(4)
