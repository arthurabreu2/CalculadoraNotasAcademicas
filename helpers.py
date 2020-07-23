from main import alunos


# Função 1 » Obter a media das notas

def obter_media(notas):
    """
    Função para obter a média das notas do aluno (lista)
    :param notas: lista com notas de cada tipo de teste avaliado (provas, trabalhos, laboratorio)
    :return: média das notas dentro da lista informada
    """
    total_somas = sum(notas)
    total_somas = float(total_somas)
    return total_somas / len(notas)


# Função 2 » Média com base nos pesos

def calcular_media_total(aluno):
    """
    Função que calcula a média total por pesos
    :param aluno: dicionario com dados do aluno
    :return: media final com base nos pesos
    """
    trabalhos = obter_media(aluno['trabalhos'])      # 25% das notas obtidas na submissão do trabalho
    provas = obter_media(aluno['provas'])           # 55% das notas obtidas nas  provas
    laboratorio = obter_media(['laboratorio'])    # 20% das notas obtidas no laboratorio
    return (o.25 * trabalhos + 0.55 * provas + 0.20 * laboratorio)


# Função 3 » Atribuir a letra a nota

def atribuir_letra_nota(nota_final_aluno):
    """
    Função para atribuir a letra correta de acordo com a nota final do aluno
    :param nota_final_aluno: nota final do aluno com base nos pesos
    :return: nota em letra
    """
    if nota_final_aluno >= 90:
        return "A"
    elif nota_final_aluno >= 80:
        return "B"
    elif nota_final_aluno >= 70:
        return "C"
    elif nota_final_aluno >= 60:
        return "D
    else:
        return "F"


# Função 4 » Média da calsse

def nota_media_classe():
    """
    Função para calcular a media final da classe dos alunos
    :return: media final dos alunos
    """
    resultado_lista = []

    for aluno, detalhes in alunos.items():
        media_aluno = calcular_media_total(alunos[aluno])
        resultado_lista.append(media_aluno)

    return obter_media(resultado_lista)