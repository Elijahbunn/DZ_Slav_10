win_state = False
playing_field = list(range(1,10))
counter = 0
player = ""
status = False
positions = []
all_win_coords = ((1,2,3),(4,5,6),(7,8,9),(1,5,9),(3,6,9),(1,4,7),(2,5,8),(3,6,9))
while status == False:
    if counter == 9:
        print("ничья")
        break
    for current in range(1,10,3):
        print(playing_field[current-1],playing_field[current],playing_field[current+1])
    if counter %2:
        player = "0"
    else:
        player = "X"
    counter += 1
    walid = False
    while walid == False:
        position = int(input(player+"ваш код: "))
        if position in positions:
            
            print("эта позиция уже занята!")
        else:
            positions.append(position)
            walid = True
            playing_field [position-1] = player
    if counter > 4:
        for number_one,number_two,number_three in all_win_coords:
            if playing_field [number_one-1] == playing_field [number_two-1] == playing_field [number_three-1] == player:
                print(f"игрок {player} выйграл ")
                status = True
