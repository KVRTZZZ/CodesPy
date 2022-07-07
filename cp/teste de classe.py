class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
    def p_nome(self, nome):
        self.nome = nome
    def p_idade(self, idade):
        self.idade = idade
    def devol_nome(self):
        return self.nome
        
    def devol_idade(self):
        return self.idade
        
        
