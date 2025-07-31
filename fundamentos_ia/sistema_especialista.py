# Sistema Especialista Simples em Python
# Este código implementa um sistema especialista simples que utiliza uma base de conhecimento
# para inferir novos fatos com base em regras definidas.

# cria a base de conhecimento e o sistema especialista
class BasedeConhecimento:
    def __init__(self):
        self.fatos = []
        self.regras = []

    def adicionar_fato(self, fato):
        self.fatos.append(fato)

    def adicionar_regra(self, regra):
        self.regras.append(regra)

class SistemaEspecialista:
    def __init__(self, base_conhecimento):
        self.base_conhecimento = base_conhecimento

# método para inferir novos fatos com base nas regras
    def inferir(self):
        novos_fatos = True
        while novos_fatos:
            novos_fatos = False
            for condicao, conclusao in self.base_conhecimento.regras:
                if all(fato in self.base_conhecimento.fatos for fato in condicao):
                    if conclusao not in self.base_conhecimento.fatos:
                        self.base_conhecimento.adicionar_fato(conclusao)
                        novos_fatos = True


# exemplo de uso do sistema especialista

base = BasedeConhecimento()

base.adicionar_fato("dor de cabeça")
base.adicionar_fato("dor no corpo")
base.adicionar_fato("náusea")
base.adicionar_fato("alergia")

base.adicionar_regra((["dor de cabeça", "dor no olho"], "dengue"))
base.adicionar_regra((["náusea", "alergia"], "reação alérgica"))

sistema = SistemaEspecialista(base)

sistema.inferir()

print("Fatos inferidos na base de conhecimento:")
print(base.fatos)

print("Regras na base de conhecimento:")
for regra in base.regras:
    print(f"Se {' e '.join(regra[0])}, então {regra[1]}")