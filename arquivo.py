import os

class arquivo:

    def capturarUltimoArquivo(self):
        caminho = "C:\\Users\lukin\Downloads"
        listaArquivos = os.listdir(caminho)

        listaDatas = []
        for arquivo in listaArquivos:
            data = os.path.getmtime(f"{caminho}/{arquivo}")
            listaDatas.append((data, arquivo))

        listaDatas.sort(reverse=True)
        ultimoArquivo = listaDatas[0]
        return f"{caminho}/{ultimoArquivo[1]}"