import pytest
from atividade.models.pessoa import Pessoa 
from atividade.models.endereco import Endereco #Caminha absoluto.
from atividade.models.enums.sexo import Sexo
from atividade.models.enums.unidadefederativa import Unidadefederativa
 
#Modelo
@pytest.fixture
def criar_pessoa():
    pessoa_1 = Pessoa("11", "Pedro", "03/07", "7198523998", "pedro375@gmail.com", Sexo.MASCULINO,
                 Endereco("Rodão", "5", "Travessa", "40350", "Salvador", Unidadefederativa.BAHIA))
    return pessoa_1

def test_pessoa_atributo_nome(criar_pessoa):
    assert criar_pessoa.id == "11"

def test_pessoa_atributo_idade(criar_pessoa):    
    assert criar_pessoa.nome == "Pedro"
    