import numpy as np

#recomendada quando há algum aluno com até 88% de nota
def adicao_pontos(dados):
  ponto_extra = 100 - dados.max()   
  nota = dados + ponto_extra

  return nota

#Esse ajuste beneficia muito os alunos com notais mais baixas
def raiz_quadrada(dados):
  raiz = 10 * np.sqrt(dados)

  return raiz
#normalização dos dados
def equacao_normal(dados):
  media = np.mean(dados)
  desvio_padrao = np.std(dados)
  normalizando = 1/(desvio_padrao * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((dados - media) ** 2) / (desvio_padrao ** 2))

  return normalizando
#substituição de notas por conceitos
def modifica_conceitos(dados):
  if dados <= 59:
    return 'F'
  elif dados <= 69:
    return 'D'
  elif dados <= 79:
    return 'C'
  elif dados <= 89:
    return 'B'
  else:
    return 'A'
