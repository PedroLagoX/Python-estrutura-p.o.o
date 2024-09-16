from atividade.models.endereco import Endereco
from atividade.models.enums.sexo import Sexo

class Pessoa:
    def __init__(self, id:str, nome:str, dataNascimento:str, telefone:str, email:str, sexo:Sexo, endereco:Endereco) -> None:
        self.id = id
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.telefone = telefone
        self.email = email
        self.sexo = sexo
        self.endereco = endereco

    def __str__(self) -> str:
        return (
            f"\nID: {self.id}"
            f"\nNome: {self.nome}"
            f"\nData de Nascimento: {self.dataNascimento}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nSexo: {self.sexo.texto}"
            f"\nSexo: {self.sexo.caracter}"
            f"\nEndereço {self.endereco}"
        )