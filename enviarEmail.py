class enviarEmail:
    def __init__(self, cnpj, ano, email):
        self.cnpj = cnpj
        self.ano = ano
        self.email = email

    def enviar(self):
        import win32com.client as win32
        outlook = win32.Dispatch('outlook.application')

        email = outlook.CreateItem(0)

        email.To = self.email
        email.Subject = "Teste22"
        email.HTMLBody = """
        <p>Olá, Conforme solicitado segue anexo com arquivo do DAS</p>
        """+self.cnpj+self.ano+"""
        <p>Atenciosamente </p>
        
        <p>Palm Labs</p>
        """
        email.send
        return "email enviado com sucesso"