from impostos_funcao import calcula_ICMS, calcula_ISS
from impostos_classe import ICMS, ISS

class Calculador_imposto(object):

  def realiza_calculo_funcao(self, orcamento, imposto):
    imposto_calculado = imposto(orcamento)
    print(imposto_calculado)

  def realiza_calculo_metodo(self, orcamento, imposto):
    imposto_calculado = imposto(orcamento)
    print(imposto_calculado)

  def realiza_calculo_classe(self, orcamento, imposto):
    imposto_calculado = imposto.calcula(orcamento)
    print(imposto_calculado)

# executando código
if __name__ == '__main__':
  from orcamento import Orcamento

  calculador = Calculador_imposto()

  orcamento = Orcamento(500)

  calculador.realiza_calculo_funcao(orcamento, calcula_ICMS)
  calculador.realiza_calculo_funcao(orcamento, calcula_ISS)

  calculador.realiza_calculo_metodo(orcamento, ISS().calcula)
  calculador.realiza_calculo_metodo(orcamento, ICMS().calcula)

  calculador.realiza_calculo_classe(orcamento, ISS())
  calculador.realiza_calculo_classe(orcamento, ICMS())
