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

from helpers import alunos, calcular_media_total, atribuir_letra_nota, nota_media_classe

if __name__ == '__main__':
    # forlooping no dicionario de alunos e calcular as respectivas notas
    for aluno, detalhes in alunos.items():
        print(f"\n {alunos[aluno]['nome']} ")
        print('_______________')
        media_total_aluno = round(calcular_media_total(alunos[aluno]), 1)
        print(f"Média de notas do(a) {alunos[aluno]['nome']} é: {round(calcular_media_total(alunos[aluno]), 1)}")
        print(f"Nota final do aluno(a) {alunos[aluno]['nome']} é: {atribuir_letra_nota(media_total_aluno)}")

    # Calcula a média da classe
    media_classe = nota_media_classe()

    print(f"\nMédia da classe é: {round(media_classe, 1)}")
    print(f"Nota final da classe é: {atribuir_letra_nota(media_classe)}")