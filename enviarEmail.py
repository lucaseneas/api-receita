
class enviarEmail:
    def __init__(self, cnpj, data, email):
        self.cnpj = cnpj
        self.data = data
        self.email = email

    def enviar(self):
        from arquivo import arquivo
        import win32com.client as win32
        outlook = win32.Dispatch('outlook.application')

        email = outlook.CreateItem(0)

        email.To = self.email
        email.Subject = "DAS CNPJ: "+self.cnpj
        email.HTMLBody = """
        <p>Olá, Conforme solicitado segue anexo com arquivo do DAS referente a """+self.data+"""</p>
        Cnpj: """+self.cnpj+"""
        <p>Atenciosamente </p>
        
        <p>Palm Labs</p>
        
        <p>Email automático, favor não responder</p>
        """
        anexo = arquivo()
        email.Attachments.Add(anexo.capturarUltimoArquivo())
        email.send
        return "email enviado com sucesso"

