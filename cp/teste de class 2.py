class carro:
    def __init__(self, rodas, cor, marca):
        self.rodas = rodas
        self.cor = cor
        self.marca = marca
    def ligar(self, chaves):
        self.chaves = chaves

    def desligar(self, chaves_desligar):
        self.chaves_desligar = chaves_desligar
        
        
        
carro1 = carro('michellin', 'amarelo', 'mustang')
carro1.ligar('chaves')
print(carro1.ligar)

print(carro1.cor)