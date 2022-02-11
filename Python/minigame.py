import random

prot = {'hp': 1200, 'nome': 'protagonista'}
ini1 = {'hp': 500, 'nome': 'monstro das neves'}
ini2 = {'hp': 700, 'nome': 'varredor'}
golpes = ['atkv', 'atkn']


def dano1():
    escolha = input("Dano em quem? varredor ou neves")
    if escolha.lower() == 'varredor':
        if ini2['hp'] <= 0:
            print("\nVarredor já morreu")
        else:
            ini2['hp'] -= 300
            print("\nAgora o varredor tem " + str(ini2['hp']) + " de vida")
    if escolha.lower() == 'neves':
        if ini1['hp'] <= 0:
            print("\nMonstro das Neves já morreu")
        else:
            ini1['hp'] -= 300
            print("\nAgora o monstro das neves tem " + str(ini1['hp']) + " de vida")


def dano2():
    escolha = input("Dano em quem? varredor ou neves")
    if escolha.lower() == 'varredor':
        if ini2['hp'] <= 0:
            print("\nVarredor já morreu")
        ini2['hp'] -= 400
        print("\nAgora o varredor tem " + str(ini2['hp']) + " de vida")

    if escolha.lower() == 'neves':
        if ini1['hp'] <= 0:
            print("\nMonstro das Neves já morreu")
        ini1['hp'] -= 400
        print("\nAgora o monstro das neves tem " + str(ini1['hp']) + " de vida")


def dano3():
    escolha = input("Dano em quem? varredor ou neves")
    if escolha.lower() == 'varredor':
        if ini2['hp'] <= 0:
            print("\nVarredor já morreu")
        ini2['hp'] -= 500
        print("\nAgora o varredor tem " + str(ini2['hp']) + " de vida")

    if escolha.lower() == 'neves':
        if ini1['hp'] <= 0:
            print("\nMonstro das Neves já morreu")
        ini1['hp'] -= 500
        print("\nAgora o monstro das neves tem " + str(ini1['hp']) + " de vida")


def dano(atk):
    if atk.lower() == 'atk1':
        dano1()
    elif atk.lower() == 'atk2':
        dano2()
    elif atk.lower() == 'atk3':
        dano3()
    else:
        print("\nAtaque Inválido")


def golpe(atk_ini):
    if atk_ini.lower() == 'atkv' and ini2['hp'] > 0:
        print("\nVarredor te atacou")
        prot['hp'] -= 400
    elif atk_ini.lower() == 'atkn' and ini1['hp'] > 0:
        prot['hp'] -= 300
        print("\nMonstro das Neves te atacou")


v1 = True
v2 = True
while True:
    print('Você tem ' + str(prot['hp']) + " de vida")

    if ini1['hp'] <= 0 and v1:
        print("\nMonstro das Neves morreu")
        v1 = False
        golpes.remove('atkn')

    if ini2['hp'] <= 0 and v2:
        print("\nVarredor morreu")
        v2 = False
        golpes.remove('atkv')

    if ini1['hp'] <= 0 and ini2['hp'] <= 0:
        print("\nVocê matou os inimigos")
        break

    atk_inimigo = random.choice(golpes)
    golpe(atk_inimigo)

    if prot['hp'] <= 0:
        print("\nVocê Morreu")
        break

    ataque = input('\nEscolha um ataque: atk1 atk2 atk3')
    dano(ataque)
