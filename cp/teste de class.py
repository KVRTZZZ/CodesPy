class computador():
    def __init__(self, marca, memoriaRam, placaMae):
        self.marca = marca
        self.memoriaRam = memoriaRam
        self.placaMae = placaMae
        
        
    def ligar(self):
        print('estou ligando')
        
        
    def desligar(self):
        print('estou desligando')
        
        
    def ExibirInformaçoes(self):
        print(self.marca, self.memoriaRam, self.placaMae)
        
        
computador1 = computador('asus', '16gb', 'geforce')
computador1.ligar()
computador1.desligar()
computador1.ExibirInformaçoes()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
'''computador1 = computador('asus', 'ddr5', 'NVidia')
computador2 = computador('multilaser', ' ddr4', 'nvidia')
computador3 = computador('polishop', 'ddr3', 'nvidia')
print(computador1.marca, computador1.memoriaRam,computador1.placaMae)
print(computador2.marca, computador2.memoriaRam, computador2.placaMae)
print(computador3.marca, computador3.memoriaRam, computador3.placaMae)
print(computador1 .desligar)'''