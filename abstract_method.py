from abc import ABC, abstractmethod
class Pessoa(ABC):
    ct = 0
    @classmethod
    def get_ct(cls):
        return cls.ct

    def __init__(self,senha,matricula):
        Pessoa.ct += 1
        self.senha = senha
        self.matricula = matricula
        pass
    @abstractmethod
    def get_matricula(self):
        pass
    def senha(self):
        prompt = int(input("senha numérica:"))
        if prompt == self.senha:
            print("Acesso liberado")
        else:
            print("Senha incorreta")
            return self.senha
    def alterar_senha(self,nova_senha):
        if type(nova_senha) != int:
            print("inserção inválida")
        else:
            self.senha = nova_senha
            return self.senha

class Professor(Pessoa):
    def __init__(self,ctps,pg_hora,carga_horaria,matricula):
        super().__init__(ctps,matricula)
        self.ctps = ctps
        self.pg_hora = pg_hora
        self.carga_horaria = carga_horaria
    def get_ctps(self):
        return self.ctps
    def set_ctps(self,novo_ctps):
        if type(novo_ctps) != int:
            print("Inserção inválida")
        elif len(str(novo_ctps)) != 5:
            print("Inserção inválida")
        else:
            self.ctps = novo_ctps
            return self.ctps
    def get_pg_hora(self):
        return self.pg_hora
    def set_pg_hora(self,novo_pg_hora):
        if novo_pg_hora < 0:
            print("Inserção inválida")
        else:
            self.pg_hora = novo_pg_hora
            return self.pg_hora
    def get_carga_horaria(self):
        return self.carga_horaria
    def set_carga_horaria(self,nova_carga_horaria):
        self.carga_horaria = nova_carga_horaria
        return self.carga_horaria
    def get_matricula(self):
        return self.matricula
    def salario(self):
        salario = (self.pg_hora * self.carga_horaria) * 30
        return salario
    def salario_anual(self):
        salario = (self.pg_hora * self.carga_horaria) * 360
        return salario
class Aluno(Pessoa):
    def __init__(self,cpf,matricula):
        super().__init__(cpf,matricula)
        self.cpf = cpf
    def get_cpf(self):
        return self.cpf
    def set_cpf(self,novo_cpf):
        if type(novo_cpf) != int:
            print("Formato inválido")
        else:
            self.cpf = novo_cpf
            return self.cpf
    def get_matricula(self):
        return self.matricula

if __name__ == '__main__':
    professor1 = Professor(17480,10,8,22610090)
    aluno1 = Aluno(700,4291)

    print(professor1.get_ctps())
    professor1.set_ctps(67549)
    print(professor1.get_pg_hora())
    professor1.set_pg_hora(15)
    print(professor1.get_carga_horaria())
    professor1.set_carga_horaria(6)
    print(professor1.get_matricula())
    print(professor1.salario())
    print(professor1.salario_anual())
    print(aluno1.get_cpf())
    print(aluno1.get_ct())
    print(aluno1.senha)
    aluno1.alterar_senha(777)
    print(aluno1.senha)












