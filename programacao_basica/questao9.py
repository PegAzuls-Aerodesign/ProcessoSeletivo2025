aeromodelos = [
    {"nome": "JuninhoAviao", "envergadura": 1.2, "peso": 2.5, "empuxo": 120000},
    {"nome": "PaulinhoAeronave", "envergadura": 1.5, "peso": 3.0, "empuxo": 45},
    {"nome": "Pegazul", "envergadura": 1.0, "peso": 1.8, "empuxo": 90},
    {"nome": "Bismark", "envergadura": 1.8, "peso": 4.2, "empuxo": 29},
    {"nome": "UFERSA", "envergadura": 1.3, "peso": 2.7, "empuxo": 30}
]

X = 30

print(f"Modelos com empuxo maior que {X}:")
print("-" * 32)
print()

for modelo in aeromodelos:
    if modelo["empuxo"] > X:
        print(f"Nome: {modelo['nome']} | Envergadura: {modelo['envergadura']}m | "
              f"Peso: {modelo['peso']}kg | Empuxo: {modelo['empuxo']}N")