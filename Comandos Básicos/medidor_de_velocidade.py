# Medidor de Velocidade

"""
Levando em consideração a velocidade máxima permitida de 80km em uma determinada rua.
Crie um programa que recebe do usuário um valor que representa a velocidade
e com base nessa velocidade diga se ele tomou um multa leve, grave ou gravíssima.
Levando em consideração que se a pessoa estiver abaixo da velocidade máxima
seu programa deve exibir "não houve multa", caso esteja até 10km acima, deve exibir:
"levou multa leve", caso esteja entre 11 a 20km acima da velocidade máxima,
exibir: "levou multa grave", e caso esteja acima de 20km acima da velocidade máxima,
exiba: "levou multa gravíssima".
"""

velocidade = int(input("Digite a velocidade do carro: "))
velocidade_maxima = 80

if velocidade >= 0:
    if velocidade <= velocidade_maxima:
        print("não houve multa")
    elif velocidade_maxima < velocidade <= velocidade_maxima + 10:
        print("levou multa leve")
    elif velocidade_maxima + 11 <= velocidade <= velocidade_maxima + 20:
        print("levou multa grave")
    elif velocidade > velocidade_maxima + 20:
        print("levou multa gravíssima")
else:
    print("Não existe velocidade negativa")