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
drukujPlansze(PlanszaDoGry)

