"""
Um programa para criar uma Calculadora de Notas Academicas em Python
Dados diferentes pesos e notas aos alunos, precisamos encontrar as notas finais.
A pontuação do provas é uma média das respectivas notas (provas, trabalhos, laboratorio)

A pontuação final da provas é atribuido usando a fórmula abaixo:
25% das notas obtidas na submissão do trabalho
55% das notas obtidas nas  provas
20% das notas obtidas no laboratorio

A nota será calculada de acordo com:
1. pontuação >= 90: "A"
2. pontuação >= 80: "B"
3. pontuação >= 70: "C"
4. pontuaçãO >= 60: "D"
Além disso, calcule a média total da classe e a nota da classe.
"""

alunos = {
    "arthurv":
        {
            'nome': 'Arthur Vinicius'
            'trabalhos': [90, 95, 80, 100],
            'provas': [90, 80]
            'laboratorio': [70, 85.2]
        },
    "refaelas":
        {
            'nome': 'Rafaela Santos '
            'trabalhos': [100, 60, 80, 90],
            'provas': [87, 95]
            'laboratorio': [60, 75]
        },
    "samuelb":
        {
            'nome': 'Samuel Batista'
            'trabalhos': [78, 95, 65, 88],
            'provas': [70, 60]
            'laboratorio': [60, 85.5]
        },
    "josec":
        {
            'nome': 'Jose Carlos'
            'trabalhos': [100, 95, 80, 100],
            'provas': [90, 95]
            'laboratorio': [70, 75.5]
        },
}