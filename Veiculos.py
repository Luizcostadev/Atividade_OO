# classe pai

class Veiculo:
    def __init__(self, modelo, placa, valor):
        self.modelo = modelo
        self.placa = placa
        self.valor = valor
        self._disponivel = True

    def alugar(self):
        if self._disponivel:
            self._disponivel = False
            return True
        return False

    def devolver(self):
        if not self._disponivel:
            self._disponivel = True
            return True
        return False

    def exibir_informacoes(self):
        print(f"Modelo: {self.modelo}")
        print(f"Placa: {self.placa}")
        print(f"Diária: R$ {self.valor:.2f}")
        print(f"Disponível: {'Sim' if self._disponivel else 'Não'}")


# classes filhas

class Carro(Veiculo):
    def __init__(self, modelo, placa, valor, portas):
        super().__init__(modelo, placa, valor)
        self.portas = portas

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Portas: {self.portas}")

    def calcular_aluguel(self, dias):
        return self.valor * dias


class Moto(Veiculo):
    def __init__(self, modelo, placa, valor, cilindradas):
        super().__init__(modelo, placa, valor)
        self.cilindradas = cilindradas

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Cilindradas: {self.cilindradas}")

    def calcular_aluguel(self, dias):
        return self.valor * dias * 0.9


# objetos

carro_1 = Carro("Ford Scort", "MOZ700", 200, 4)
carro_2 = Carro("Fiat Marea", "NGR500", 140, 4)
moto_1 = Moto("Honda Pop", "DEZ670", 120, 100)
moto_2 = Moto("Yamaha Sahara", "GLS693", 140, 350)


# lista de veículos

veiculos = []


def cadastrar_veiculo():
    tipo = input("1 - Carro / 2 - Moto: ")
    modelo = input("Modelo: ")
    placa = input("Placa: ")
    valor = float(input("Valor da diária: "))

    if tipo == "1":
        portas = int(input("Quantidade de portas: "))
        veiculo = Carro(modelo, placa, valor, portas)

    elif tipo == "2":
        cilindradas = int(input("Cilindradas: "))
        veiculo = Moto(modelo, placa, valor, cilindradas)

    else:
        print("Tipo inválido.")
        return

    veiculos.append(veiculo)
    print("Veículo cadastrado com sucesso!")

def buscar_veiculo(placa):
    for v in veiculos:
        if v.placa == placa:
            return v

    return None


def listar_veiculos():
    if not veiculos:
        print("Nenhum veículo cadastrado.")
        return

    for veiculo in veiculos:
        veiculo.exibir_informacoes()
        print("-" * 30)


def alugar_veiculo():
    placa = input("Placa: ")

    veiculo = buscar_veiculo(placa)

    if veiculo is None:
        print("Veículo não encontrado.")
        return

    dias = int(input("Dias alugados: "))

    if veiculo.alugar():
        valor = veiculo.calcular_aluguel(dias)
        print("Veículo alugado com sucesso!")
        print(f"Valor do aluguel: R$ {valor:.2f}")

    else:
        print("Veículo indisponível.")

def devolver_veiculo():
    placa = input("Placa: ")

    veiculo = buscar_veiculo(placa)

    if veiculo is None:
        print("Veículo não encontrado.")
        return

    if veiculo.devolver():
        print("Veículo devolvido!")

    else:
        print("Esse veículo já está disponível.")
# menu

while True:
    print("\n===== LOCADORA DE VEÍCULOS =====")
    print("1 - Cadastrar veículo")
    print("2 - Listar veículos")
    print("3 - Alugar veículo")
    print("4 - Devolver veículo")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_veiculo()

    elif opcao == "2":
        listar_veiculos()

    elif opcao == "3":
        alugar_veiculo()

    elif opcao == "4":
        devolver_veiculo()

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")

        