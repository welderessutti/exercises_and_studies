from validate_docbr import CPF, CNPJ


class Documento:
    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Quantidade de dígitos está incorreta!!")


class DocCpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador_cpf = CPF()
        return validador_cpf.validate(documento)

    def format(self):
        mascara_cpf = CPF()
        return mascara_cpf.mask(self.cpf)


class DocCnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("CNPJ inválido!!")

    def __str__(self):
        return self.format()

    def valida(self, documento):
        validador_cnpj = CNPJ()
        return validador_cnpj.validate(documento)

    def format(self):
        mascara_cnpj = CNPJ()
        return mascara_cnpj.mask(self.cnpj)
