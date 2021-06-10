"""SISTEMA DE RH - CÁLCULO DO SALÁRIO LÍQUIDO"""

def main():
    print(f'\033[1:33m{"="*10} SISTEMA DE RH - CÁLCULO DE SALÁRIO LÍQUIDO {"="*10}\033[m')

    while True:
        try:
            nomeusu = input('Digite o nome do funcionário: ')
            setor = input('Digite o setor do funcionário: ')
            salariobruto = float(input('Digite o sálario Bruto para cáculo do salário líquido: '))
            if salariobruto < 1100:
                print('ERRO! Valor de salário inválido e menor que o permitido tente novamente')
            else:
                salarioliquido = 0
                inss = 0
                irrf = 0
                valortransporte = 0
                valoremprestimo = 0
                valorsaude = 0
                valorsindicato = 0
                aliqinss = 0
                aliqirrf = 0
                parceladeduirrf = 0
                valordeciter = 0
                valorbonus = 0
                valorferias = 0
                aliqinssf = 0
                inssf = 0
                aliqinssff = 0
                inssff = 0
                vendferias = ''
                # ---------------------------------------- INICIO DO CODIGO DE CRIPTOGRAFIA ------------------------------------------------



                phrase = True
                key = [[1, 3], [2, 1]]
                criptografia = True
                letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                           's', 't', 'u',
                           'v', 'w', 'x', 'y', 'z', ' ', ]

                while phrase:
                    try:
                        message = nomeusu.lower().strip()
                        for x in message:
                            if x not in letters:
                                raise
                            else:
                                phrase = False
                    except:
                        print("\nDigite apenas letras\n")

                # Verificando se o tamanho da frase é divisível por 2, para que seja possível o armazenamento em pares de letras
                # Se nao for, o programa irá acrescentar um espaço deixando a frase divisivel por 2

                double = []
                matriz_phrase = []

                if len(message) % 2 != 0:
                    message = message + ' '

                # Armazenando a frase em pares de letras

                for x in message:
                    double.append(letters.index(x))
                    if len(double) == 2:
                        matriz_phrase.append(double.copy())
                        double.clear()
                matriz_cifrada = []
                double = []

                # Realizando o Pmodulo da Matriz

                for x in matriz_phrase:
                    double.append((key[0][0] * x[0] + key[0][1] * x[1]) % 26)
                    double.append((key[1][0] * x[0] + key[1][1] * x[1]) % 26)
                    matriz_cifrada.append(double.copy())
                    double.clear()

                # Seleciona as letras de acordo com o resultado do pmodulo e mostra na tela
                mensagem_cifrada = ''
                for x in matriz_cifrada:
                    mensagem_cifrada += letters[x[0]] + letters[x[1]]

                # ---------------------------------------- FIM DO CODIGO DE CRIPTOGRAFIA ---------------------------------------------------

                # Cálculo do INSS:

                if salariobruto <= 1100.00:
                    aliqinss = 0.075
                    inss = salariobruto * 0.075
                elif 1100.01 <= salariobruto <= 2203.48:
                    aliqinss = 0.09
                    inss = 1100.00 * 0.075 + (salariobruto - 1100.01) * 0.09
                elif 2203.49 <= salariobruto <= 3305.22:
                    aliqinss = 0.12
                    inss = 1100.00 * 0.075 + 1103.47 * 0.09 + (salariobruto - 2203.49) * 0.12
                elif 3305.23 <= salariobruto <= 6433.57:
                    aliqinss = 0.14
                    inss = 1100.00 * 0.075 + 1103.47 * 0.09 + 1101.73 * 0.12 + (salariobruto - 3305.22) * 0.14
                elif salariobruto > 6433.57:
                    aliqinss = 751.99
                    inss = 751.99

                # Cálculo do imposto de renda:
                while True:
                    try:
                        dependente = int(input('Digite quantos dependentes possui: '))
                        if dependente < 0:
                            print('ERRO! Valor de dependentes inválido tente novamente')
                        else:
                            if salariobruto <= 1903.98:
                                print('Isento para contribuição do imposto de renda.')
                            elif 1903.99 <= salariobruto <= 2826.65:
                                aliqirrf = 0.075
                                parceladeduirrf = 142.80
                                irrf = ((salariobruto - 189.59 * dependente) * 0.075) - 142.80
                            elif 2826.66 <= salariobruto <= 3751.05:
                                aliqirrf = 0.15
                                parceladeduirrf = 354.80
                                irrf = ((salariobruto - 189.59 * dependente) * 0.15) - 354.80
                            elif 3751.06 <= salariobruto <= 4664.68:
                                aliqirrf = 0.225
                                parceladeduirrf = 636.13
                                irrf = ((salariobruto - 189.59 * dependente) * 0.225) - 636.13
                            elif salariobruto > 4664.68:
                                aliqirrf = 0.275
                                parceladeduirrf = 869.36
                                irrf = ((salariobruto - 189.59 * dependente) * 0.275) - 869.36
                            break
                    except ValueError:
                        print('ERRO! Tente novamente Digitando apenas valores numéricos inteiros.')

                    # Cálculo plano de saúde:
                while True:
                    try:
                        planosaude = input('Possui plano de saúde vínculado à empresa [S,N]? ')
                        if planosaude == 'S' or planosaude == 's':
                            valorsaude = float(input('Digite o valor do plano de saúde: '))
                            if valorsaude < 0:
                                print('ERRO! Valor de inválido tente novamente')
                            else:
                                salariobruto = salariobruto - valorsaude
                                break
                        elif planosaude == 'N' or planosaude == 'n':
                            break
                        else:
                            print('ERRO! Tente novamente Digitando apenas S ou N')
                    except ValueError:
                        print('ERRO! Tente novamente Digitando apenas S ou N')
                    # Cálculo vale-transporte:
                while True:
                    try:
                        valetransporte = input('Possui vale transporte vínculado à empresa [S,N]? ')
                        if valetransporte == 'S' or valetransporte == 's':
                            valortransporte = float(input('Digite o valor do vale transporte: '))
                            if valortransporte < 0:
                                print('ERRO! Valor de inválido tente novamente')
                            else:
                                salariobruto = salariobruto - valortransporte
                                break
                        elif valetransporte == 'N' or valetransporte == 'n':
                            break
                        else:
                            print('ERRO! Tente novamente Digitando apenas S ou N')
                    except ValueError:
                        print('ERRO! Tente novamente Digitando apenas S ou N')

                    # Cálculo empréstimos
                while True:
                    try:
                        emprestimo = input('Possui empréstimo vínculado à empresa [S,N]? ')
                        if emprestimo == 'S' or emprestimo == 's':
                            valoremprestimo = float(input('Digite o valor do empréstimo: '))
                            if valoremprestimo < 0:
                                print('ERRO! Valor de inválido tente novamente')
                            else:
                                salariobruto = salariobruto - valoremprestimo
                                break
                        elif emprestimo == 'N' or emprestimo == 'n':
                            break
                        else:
                            print('ERRO! Tente novamente Digitando apenas S ou N')
                    except ValueError:
                        print('ERRO! Tente novamente Digitando apenas S ou N')
                    # Cálculo contribuição sindical
                while True:
                    try:
                        sindicato = input('Possui contribuição sindical vínculado à empresa [S,N]? ')
                        if sindicato == 'S' or sindicato == 's':
                            valorsindicato = float(input('Digite o valor da contribuição sindical: '))
                            if valorsindicato < 0:
                                print('ERRO! Valor de inválido tente novamente')
                            else:
                                salariobruto = salariobruto - valorsindicato
                                break
                        elif sindicato == 'N' or sindicato == 'n':
                            break
                        else:
                            print('ERRO! Tente novamente Digitando apenas S ou N')
                    except ValueError:
                        print('ERRO! Tente novamente Digitando apenas S ou N')
                    # Adiantamento salárial (VALE)
                while True:
                    try:
                        vale = input('Possui adiantamento salárial (VALE) [S,N]? ')
                        if vale == 'S' or sindicato == 's':
                            valorvale = salariobruto * 0.4
                            break
                        elif sindicato == 'N' or sindicato == 'n':
                            break
                        else:
                            print('ERRO! Tente novamente Digitando apenas S ou N')
                    except ValueError:
                        print('ERRO! Tente novamente Digitando apenas S ou N')

                    # Cálculo de férias
                while True:
                    try:
                        ferias = input('Completou 12 meses trabalhados [S,N]? ')
                        if ferias == 'S' or ferias == 's':
                            diasferias = int(input('Digite a quantidade de dias de férias: '))
                            if diasferias < 0 or diasferias > 30:
                                print('ERRO! Valor inválido tente novamente')
                            else:
                                meses = 12
                                feriasliq = (salariobruto * 1.3) / 30 * diasferias

                                # INSS das Férias
                                if feriasliq <= 1100.00:
                                    aliqinssff = 0.075
                                    inssff = feriasliq * 0.075
                                elif 1100.01 <= feriasliq <= 2203.48:
                                    aliqinssff = 0.09
                                    inssff = 1100.00 * 0.075 + (feriasliq - 1100.01) * 0.09
                                elif 2203.49 <= feriasliq <= 3305.22:
                                    aliqinssff = 0.12
                                    inssff = 1100.00 * 0.075 + 1103.47 * 0.09 + (feriasliq - 2203.49) * 0.12
                                elif 3305.23 <= feriasliq <= 6433.57:
                                    aliqinssff = 0.14
                                    inssff = 1100.00 * 0.075 + 1103.47 * 0.09 + 1101.73 * 0.12 + (feriasliq - 3305.22) * 0.14
                                elif feriasliq > 6433.57:
                                    aliqinssff = 751.99
                                    inssff = 751.99

                                # IRRF das férias
                                if feriasliq <= 1903.98:
                                    print('Isento para contribuição do imposto de renda no valor das férias.')
                                elif 1903.99 <= feriasliq <= 2826.65:
                                    aliqirrff = 0.075
                                    parceladeduirrf = 142.80
                                    irrff = ((feriasliq - 189.59 * dependente) * 0.075) - 142.80
                                elif 2826.66 <= feriasliq <= 3751.05:
                                    aliqirrff = 0.15
                                    parceladeduirrf = 354.80
                                    irrff = ((feriasliq - 189.59 * dependente) * 0.15) - 354.80
                                elif 3751.06 <= feriasliq <= 4664.68:
                                    aliqirrff = 0.225
                                    parceladeduirrf = 636.13
                                    irrff = ((feriasliq - 189.59 * dependente) * 0.225) - 636.13
                                elif feriasliq > 4664.68:
                                    aliqirrff = 0.275
                                    parceladeduirrf = 869.36
                                    irrff = ((feriasliq - 189.59 * dependente) * 0.275) - 869.36
                                break
                                feriasliq = feriasliq - inssff - irrff
                        elif ferias == 'N' or ferias == 'n':
                            feriasprop = int(input('Digite a quantidade de meses trabalhados: '))
                            if feriasprop < 0 or feriasprop > 30:
                                print('ERRO! Valor inválido tente novamente')
                            else:
                                diasferias = int(input('Digite a quantidade de dias de férias: '))
                                if diasferias < 0:
                                    print('ERRO! Valor inválido tente novamente')
                                else:
                                    meses = feriasprop
                                    feriasliq = (salariobruto * 1.3) / 30 * diasferias
                                    # INSS das Férias
                                    if feriasliq <= 1100.00:
                                        aliqinssff = 0.075
                                        inssff = feriasliq * 0.075
                                    elif 1100.01 <= feriasliq <= 2203.48:
                                        aliqinssff = 0.09
                                        inssff = 1100.00 * 0.075 + (feriasliq - 1100.01) * 0.09
                                    elif 2203.49 <= feriasliq <= 3305.22:
                                        aliqinssff = 0.12
                                        inssff = 1100.00 * 0.075 + 1103.47 * 0.09 + (feriasliq - 2203.49) * 0.12
                                    elif 3305.23 <= feriasliq <= 6433.57:
                                        aliqinssff = 0.14
                                        inssff = 1100.00 * 0.075 + 1103.47 * 0.09 + 1101.73 * 0.12 + (
                                                    feriasliq - 3305.22) * 0.14
                                    elif feriasliq > 6433.57:
                                        aliqinssff = 751.99
                                        inssff = 751.99

                                    # IRRF das férias
                                    if feriasliq <= 1903.98:
                                        print('Isento para contribuição do imposto de renda no valor das férias.')
                                    elif 1903.99 <= feriasliq <= 2826.65:
                                        aliqirrff = 0.075
                                        parceladeduirrf = 142.80
                                        irrff = ((feriasliq - 189.59 * dependente) * 0.075) - 142.80
                                    elif 2826.66 <= feriasliq <= 3751.05:
                                        aliqirrff = 0.15
                                        parceladeduirrf = 354.80
                                        irrff = ((feriasliq - 189.59 * dependente) * 0.15) - 354.80
                                    elif 3751.06 <= feriasliq <= 4664.68:
                                        aliqirrff = 0.225
                                        parceladeduirrf = 636.13
                                        irrff = ((feriasliq - 189.59 * dependente) * 0.225) - 636.13
                                    elif feriasliq > 4664.68:
                                        aliqirrff = 0.275
                                        parceladeduirrf = 869.36
                                        irrff = ((feriasliq - 189.59 * dependente) * 0.275) - 869.36
                                    break
                        else:
                            print('ERRO! Tente novamente Digitando apenas S ou N')
                    except ValueError:
                        print('ERRO! Tente novamente Digitando apenas S ou N')
                    # Vender férias

                while True:
                    try:
                        if diasferias < 30:
                            vendferias = input('Quer vender 1/3 das férias [S,N]? ')
                            if vendferias == 'S' or vendferias == 's':
                                valorferias = feriasliq / 3
                                feriasliq = feriasliq + valorferias
                                break
                            elif vendferias == 'N' or vendferias == 'n':
                                break
                            else:
                                print('ERRO! Tente novamente Digitando apenas S ou N')
                        else:
                            break

                    except ValueError:
                        print('ERRO! Tente novamente Digitando apenas S ou N')
                    # Cálculo do 13º

                    try:
                        # Bruto décimo terceiro
                        brutodecter = (salariobruto/12)*meses
                        # Primeira parcela
                        decterp1 = brutodecter/2
                        # Segunda parcela
                        valorfinalinss = salariobruto * aliqinss
                        valorbaseirrf = salariobruto - valorfinalinss
                        if salariobruto > 6433.57:
                            descontoinss = brutodecter - 751.99
                            descontoirrf = (valorbaseirrf * aliqirrf) - parceladeduirrf
                            decterp2 = decterp1 - (descontoinss + descontoirrf + valortransporte + valorsaude)
                        else:
                            descontoinss = brutodecter * aliqinss
                            descontoirrf = (valorbaseirrf * aliqirrf) - parceladeduirrf
                            decterp2 = decterp1 - (descontoinss + descontoirrf + valortransporte + valorsaude)
                        valordeciter = decterp1 + decterp2

                    except ValueError:
                        print('ERRO! Tente novamente...')
                    # Bônus
                while True:
                    try:
                        bonus = input('Possui bônus salárial [S,N]? ')
                        if bonus == 'S' or bonus == 's':
                            valorbonus = float(input('Digite o valor do bônus: '))
                            if valorbonus < 0:
                                print('ERRO! Valor de inválido tente novamente')
                            else:
                                salariobruto = salariobruto + valorbonus
                                break
                        elif bonus == 'N' or bonus == 'n':
                            break
                        else:
                            print('ERRO! Tente novamente Digitando apenas S ou N')
                    except ValueError:
                        print('ERRO! Tente novamente Digitando apenas S ou N')
                    # Mostrar na tela
                totaldesconto = valoremprestimo + valorsaude + valorsindicato + valortransporte + inss + irrf
                salarioliquido = salariobruto - inss - irrf
                while True:
                    try:
                        aceitacriptografia = input('Deseja imprimir com o nome criptografado [S,N]? ')
                        if aceitacriptografia == 'S' or aceitacriptografia == 's':

                            # Impressão com criptografia

                            print(f'|NOME: \033[0:33m{mensagem_cifrada}\033[m               SETOR: {setor}    |\n')
                            print(f'|    |Descrição              |Valor            |Aliquota/valor       |\n'
                                  f'{"-" * 46}\n'
                                  f'|    |Vale transporte        |\033[0:31mR${valortransporte:^17.2f}\033[m         \n'
                                  f'|    |Contribuição sindical  |\033[0:31mR${valorsindicato:^17.2f}\033[m         \n'
                                  f'|    |Plano de saúde         |\033[0:31mR${valorsaude:^17.2f}\033[m         \n'
                                  f'|    |Empréstimos            |\033[0:31mR${valoremprestimo:^17.2f}\033[m         ')
                            if salariobruto > 6433.57:
                                print(
                                    f'|    |INSS                   |\033[0:31mR${inss:^17.2f}\033[m|{aliqinss:.2f}       ')
                            else:
                                print(
                                    f'|    |INSS                   |\033[0:31mR${inss:^17.2f}\033[m|{aliqinss:.2f}%       ')
                            print(
                                f'|    |IRRF                   |\033[0:31mR${irrf:^17.2f}\033[m|{aliqirrf:.2f}%       \n'
                                f'|    |Total descontos        |\033[0:31mR${totaldesconto:^17.2f}\033[m         \n\n{"-" * 46}\n'
                                f'|    |Férias                 |\033[0:32mR${feriasliq:^17.2f}\033[m     \n'
                                f'|    |Décimo terceiro        |\033[0:32mR${valordeciter:^17.2f}\033[m     \n'
                                f'|    |Bônus salárial         |\033[0:32mR${valorbonus:^17.2f}\033[m     \n'
                                f'|    |Salário líquido        |\033[0:32mR${salarioliquido:^17.2f}\033[m     \n{"-" * 46}')
                            if diasferias < 30:
                                break
                            else:
                                if vendferias == 'S' or vendferias == 's':
                                    print(f'|    |Valor férias vendidas |    R${valorferias:.2f}\n{"-" * 46}')
                                    break
                                else:
                                    break

                            # Impressão sem criptografia

                        elif aceitacriptografia == 'N' or aceitacriptografia == 'n':
                            print(f'|NOME: \033[0:33m{nomeusu}\033[m               SETOR: {setor}    |\n')
                            print(f'|    |Descrição              |Valor            |Aliquota/valor       |\n'
                                  f'{"-" * 46}\n'
                                  f'|    |Vale transporte        |\033[0:31mR${valortransporte:^17.2f}\033[m         \n'
                                  f'|    |Contribuição sindical  |\033[0:31mR${valorsindicato:^17.2f}\033[m         \n'
                                  f'|    |Plano de saúde         |\033[0:31mR${valorsaude:^17.2f}\033[m         \n'
                                  f'|    |Empréstimos            |\033[0:31mR${valoremprestimo:^17.2f}\033[m         ')
                            if salariobruto > 6433.57:
                                print(
                                    f'|    |INSS                   |R$\033[0:31m{inss:^17.2f}\033[m|{aliqinss:.2f}       ')
                            else:
                                print(
                                    f'|    |INSS                   |R$\033[0:31m{inss:^17.2f}\033[m|{aliqinss:.2f}%       ')
                            print(
                                f'|    |IRRF                   |\033[0:31mR${irrf:^17.2f}\033[m|{aliqirrf:.2f}%       \n'
                                f'|    |Total descontos        |\033[0:31mR${totaldesconto:^17.2f}\033[m         \n\n{"-" * 46}\n'
                                f'|    |Férias                 |\033[0:32mR${feriasliq:^17.2f}\033[m     \n'
                                f'|    |Décimo terceiro        |\033[0:32mR${valordeciter:^17.2f}\033[m     \n'
                                f'|    |Bônus salárial         |\033[0:32mR${valorbonus:^17.2f}\033[m     \n'
                                f'|    |Salário líquido        |\033[0:32mR${salarioliquido:^17.2f}\033[m     \n{"-" * 46}')
                            if diasferias < 30:
                                break
                            else:
                                if vendferias == 'S' or vendferias == 's':
                                    print(f'|    |Valor férias vendidas |    R${valorferias:.2f}\n{"-" * 46}')
                                    break
                                else:
                                    break
                        else:
                            print('ERRO! Tente novamente Digitando apenas S ou N')
                    except ValueError:
                        print('ERRO! Tente novamente Digitando apenas S ou N')

            while True:
                try:
                    novofunc = input('Quer calcular o salário de um novo funcionário [S,N]? ')
                    if novofunc == 'S' or novofunc == 's':
                        break
                    elif novofunc == 'N' or novofunc == 'n':
                        quit('OBRIGADO POR USAR ESSE PROGRAMA!')
                    else:
                        print('ERRO! Tente novamente Digitando apenas S ou N')

                except ValueError:
                    print('ERRO! Tente novamente Digitando apenas S ou N')
                break
        except ValueError:
            print('*** ERRO! Tente novamente Digitando apenas valores numéricos.*** ')
main()