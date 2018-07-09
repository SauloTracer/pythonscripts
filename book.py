'''
Solicita ao usuário um valor inteiro;
Se for passado um valor padrão (default), caso o usuário não insira um inteiro válido, retorna o valor default.
Se não for passado um valor padrão, repete a pergunta até que um valor inteiro seja informado.
'''
def getInt(msg, default = None):
    gotIt = False
    while not gotIt:
        try:
            n = int(input(msg))
            gotIt = True
        except:
            if(default != None):
                print("Entrada inválida. Utilizando valor default ", default)
                n = default
                gotIt = True
            else:
                print("Entrada inválida. Informe um valor numérico inteiro.")
    return n

'''
Solicita um total de itens (ex.: total de páginas de um livro)
O total concluído até o momento (ex.: páginas lidas)
e a quantidade de dias em que se deseja concluir.

Retorna a porcentagem concluída e quantos itens devem ser concluídos por intervalo para alcançar esse prazo.
'''
def main():
    t = getInt("Total: ")
    l = getInt("Concluído: ",0)
    d = getInt("Intervalos: ",10)
    p = (100*l)/t
    r = (t-l)/d

    print("\n\nConcluído: {:.2f}%\nPrazo: {} intervalos\nMeta: {} itens por intervalo ".format(p,d,r))

main()