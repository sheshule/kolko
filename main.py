# główny kod gry

PlanszaDoGry = {'7':' ','8':' ','9':' ',
                '4':' ','5':' ','6':' ',
                '1':' ','2':' ','3':' '}

KlawiszeDoGry = []

for key in PlanszaDoGry:
    KlawiszeDoGry.append(key)
#print(KlawiszeDoGry)

def drukujPlansze(pole):
    print(f"{pole['7']}|{pole['8']}|{pole['9']}")
    print('-+-+-')
    print(f"{pole['4']}|{pole['5']}|{pole['6']}")
    print('-+-+-')
    print(f"{pole['1']}|{pole['2']}|{pole['3']}")
#drukujPlansze(PlanszaDoGry)

def gra():
    licznik = 0
    gracz = 'x'

    for i in range(9):
        drukujPlansze(PlanszaDoGry)
        ruch = input(f'Rozpoczyna {gracz}. Wybierz, gdzie postawić znak.')

        if PlanszaDoGry[ruch] == ' ':
            PlanszaDoGry[ruch] = gracz
            licznik += 1
        else:
            print('Miejsce zajęte!\nWybierz inne miejsce!')
            continue
        
        if licznik >= 5:
            # poziome
            if PlanszaDoGry['7'] == PlanszaDoGry['8'] == PlanszaDoGry['9']  != ' ':
                drukujPlansze(PlanszaDoGry)
                print('\nKONIEC GRY!')
                print(f'Wygrał gracz: {gracz}\n')
                break
            if PlanszaDoGry['4'] == PlanszaDoGry['5'] == PlanszaDoGry['6']  != ' ':
                drukujPlansze(PlanszaDoGry)
                print('\nKONIEC GRY!')
                print(f'Wygrał gracz: {gracz}\n')
                break
            if PlanszaDoGry['1'] == PlanszaDoGry['2'] == PlanszaDoGry['3']  != ' ':
                drukujPlansze(PlanszaDoGry)
                print('\nKONIEC GRY!')
                print(f'Wygrał gracz: {gracz}\n')
                break
            # pionowe
            if PlanszaDoGry['7'] == PlanszaDoGry['4'] == PlanszaDoGry['1']  != ' ':
                drukujPlansze(PlanszaDoGry)
                print('\nKONIEC GRY!')
                print(f'Wygrał gracz: {gracz}\n')
                break
            if PlanszaDoGry['8'] == PlanszaDoGry['5'] == PlanszaDoGry['2']  != ' ':
                drukujPlansze(PlanszaDoGry)
                print('\nKONIEC GRY!')
                print(f'Wygrał gracz: {gracz}\n')
                break
            if PlanszaDoGry['9'] == PlanszaDoGry['6'] == PlanszaDoGry['3']  != ' ':
                drukujPlansze(PlanszaDoGry)
                print('\nKONIEC GRY!')
                print(f'Wygrał gracz: {gracz}\n')
                break
            # ukośne
            if PlanszaDoGry['1'] == PlanszaDoGry['5'] == PlanszaDoGry['9']  != ' ':
                drukujPlansze(PlanszaDoGry)
                print('\nKONIEC GRY!')
                print(f'Wygrał gracz: {gracz}\n')
                break
            if PlanszaDoGry['7'] == PlanszaDoGry['5'] == PlanszaDoGry['3']  != ' ':
                drukujPlansze(PlanszaDoGry)
                print('\nKONIEC GRY!')
                print(f'Wygrał gracz: {gracz}\n')
                break

            if licznik == 9:
                drukujPlansze(PlanszaDoGry)
                print('\nKONIEC GRY!')
                print('\nREMIS\n')
            
        if gracz == 'x':
            gracz = 'o'
        else:
            gracz = 'x'

    restart = input('Czy chcesz zagrać ponownie? odp: t/n')
    if restart == 't' or restart == 'T':
        for key in KlawiszeDoGry:
            PlanszaDoGry[key] = ' '
        
        gra()

if __name__ == '__main__':
    gra()
            