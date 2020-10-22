from domain.logic import calcula_dedutor

def test_calculo_dedutor():
  # Arrange
  quantidade_dependentes = 5
  expectation = 189.59 * quantidade_dependentes

  # Act
  resultado = calcula_dedutor(quantidade_dependentes)

  # Assert
  assert resultado == expectation