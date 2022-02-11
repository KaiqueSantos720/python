class Computador:
    """modelar um PC"""

    def __init__(self, ram, cpu, gpu, ssd, fonte):
        self.ram = ram
        self.cpu = cpu
        self.gpu = gpu
        self.ssd = ssd
        self.fonte = fonte
        self.gabinete = ''

    def ligar(self):
        print("O PC ligou")

    def desligar(self):
        print("O PC desligou")

    def consultar_gabinete(self):
        print("O gabinete do PC é: " + self.gabinete)

    def alterar_gabinete(self, novo_gabinete):
        self.gabinete = novo_gabinete


pc = Computador("8GB", 'i5', 'integrada', '500GB', '500W')
pc.consultar_gabinete()
print("---------------------------------")
pc.gabinete = 'gabinete padrao'
pc.consultar_gabinete()
print("---------------------------------")
pc.alterar_gabinete('gabinete gamer')
pc.consultar_gabinete()
print("---------------------------------")

pc.ligar()
pc.desligar()
