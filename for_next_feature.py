def with_net():
    global continuehod
    global mouse_button_down_fl
    global gochess
    global ipos
    global jpos
    global continuehahka
    if gochess == playerchess:
        for i in range(10):
            for j in range(10):
                if checkchess(mp, polemass, i, j):
                    if continuehod == True and polemass[i][j] == continuehahka:
                        print('in False')
                        mouse_button_down_fl = True
                        continuehod = False
                        ipos = i
                        jpos = j
                    elif continuehod == True and polemass[i][j] != continuehahka:
                        break
                    # блок выбора шашки
                    elif (mouse_button_down_fl == False or polemass[i][j].vid == gochess) and polemass[i][
                        j].vid != 'kletka' and polemass[i][j].vid == gochess:
                        if len(check_chess_with_enemy(polemass, gochess)) != 0:
                            if check_correct_chess(polemass, check_chess_with_enemy(polemass, gochess), polemass[i][j]):

                                print('in False')
                                mouse_button_down_fl = True
                                ipos = i
                                jpos = j
                                break
                            else:
                                break
                        else:
                            print('in False')
                            mouse_button_down_fl = True

                            ipos = i
                            jpos = j
                            break
                    # блок хода
                    elif mouse_button_down_fl == True and gochess != polemass[i][j].vid:
                        mass = check_enemy(polemass, polemass[ipos][jpos], ipos, jpos)
                        if len(mass) != 0:
                            if hod_with_enemy(polemass, mass, ipos, jpos, i, j):

                                mouse_button_down_fl = False
                                set_damka(polemass, i, j)

                                if len(check_enemy(polemass, polemass[i][j], i, j)) == 0:
                                    set_damka(polemass, i, j)
                                    CLT.next_hod()
                                    gochess = None
                                else:
                                    set_damka(polemass, i, j)
                                    continuehod = True
                                    continuehahka = polemass[i][j]
                                    CLT.send_array()
                                break


                        elif (check_hod_without_enemy(polemass[ipos][jpos], polemass[i][j]) or (
                            polemass[ipos][jpos].damka and check_correct_damka_hod(polemass[ipos][jpos],
                                                                                   polemass[i][j]))) and polemass[i][
                            j].vid == 'kletka':
                            print('in True')
                            mouse_button_down_fl = False
                            hod(polemass, ipos, jpos, i, j)
                            set_damka(polemass, i, j)
                            CLT.next_hod()
                            gochess = None
                            break
