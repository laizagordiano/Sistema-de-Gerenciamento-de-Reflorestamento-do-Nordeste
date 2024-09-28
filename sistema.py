"Essas são as variáveis acumuladoras, que vão armazenar os dados"
#armazenar quantas árvores foram utilizadas em cada tipo.
somaCajueiro = 0
somaMangueira = 0
somaDende = 0
somaCoqueiro = 0
somaBambu = 0
somaIpe = 0

#Armazenar qual a planta mais e menos utilizada.
planta_menos_usada = ""
planta_mais_usada = ""
planta_mais_usada_sem_repetir = ""
planta_menos_usada_sem_repetir = ""
#Armazenar a área toral por tipo de árvore.
areaCajueiro = 0
areaMangueira = 0
areaDende = 0
areaCoqueiro = 0
areaBambu = 0
areaIpe = 0

#Armazenar o total de áreas de cada estado.
areaBA = 0
areaMA = 0
areaPI = 0
areaPE = 0
areaSE = 0
areaCE = 0
areaRN = 0
areaPB = 0
areaAL = 0

#Armazenar a quantidade de áreas que foram colocadas em cada estado.
somaBA = 0
somaMA = 0
somaPI = 0
somaPE = 0
somaSE = 0
somaCE = 0
somaRN = 0
somaPB = 0
somaAL = 0

#Armazenar o valor da maior área.
maior_area = 0

#Armazenar as informações da maior área.
codigo_da_maior_area = ""
cidade_da_maior_area = ""
estado_da_maior_area = ""
planta_da_maior_area = ""
estado_menos_reflorestado = ""
estados_sem_repetir = ""
sistemaGeral= True
while sistemaGeral:
    
    '------------------ Menu ------------------'
    tratamentoDeErro = 0
    while(tratamentoDeErro == 0):
        
        try:
            #Recebimento da opção do menu.
            menu = int(input("""Menu
            [1] Exibir relatório de reflorestamento da região Nordeste
            [2] Iniciar Cadastramento
            [3] Encerrar sessão\n"""))
            
        except:
            'Se der erro no try ele executa o que  tá aqui'
            print("Isira uma opção válida")
            
        #Verificar se foi inserida uma opção válida no menu.
        if menu == 1 or menu == 2 or menu == 3:  
            tratamentoDeErro = 1
        else:
            print("Isira uma opção válida")

    'Encerrar o programa'
    if menu == 3:
        sistemaGeral = False

    ''' Cadastrar uma nova área reflorestada'''
    if menu == 2:

        cod_p_area = input("informe o Código de números para a área:\n")
        cidade = input("informe a cidade do reflorestamento:\n")
        
        tratamento_de_area = True
        while tratamento_de_area:
            certo = True
            try:
                largura = float(input("Digite a largura da área:"))
                comprimento = float(input("Digite o comprimento da área:"))
            except:
                print("Insira valores válidos")
                certo = False
            if certo:
                tratamento_de_area = False


        nome_da_planta = ""
        while nome_da_planta == "":
            
            try:
                planta = int(input(""" Escolha o tipo de árvore:
                [1] Cajueiro
                [2] Mangueira
                [3] Dendê
                [4] Coqueiro
                [5] Bambu Gigante
                [6] Ipê\n"""))
            except:
                planta = 0

            if planta == 1:
                nome_da_planta = "Cajueiro"
            elif planta == 2:
                nome_da_planta = "Mangueira"
            elif planta == 3:
                nome_da_planta = "Dendê"
            elif planta == 4:
                nome_da_planta = "Coqueiro"
            elif planta == 5:
                nome_da_planta = "Bambu Gigante"
            elif planta == 6:
                nome_da_planta = "Ipê"
            else:
                print("Escolha uma opção válida")

        
        estadoCerto = True 
        'Tratamento de erro para a sigla do estado'
        
        while estadoCerto:
            estado = input("informe a sigla do estado do reflorestamento(Em letras maiúsculas EX: BA):\n")           
            if(estado == "MA" or estado == "PI" or estado == "CE" or estado == "RN" or estado == "PB" or estado == "PE" or estado == "AL" or estado == "SE" or estado == "BA"):
                estadoCerto = False
                
        confirmacao = 0        
    
        confirmacao = input("Confirmar? \n[1] Sim\n[2] Não\n")
        
        if confirmacao == '1':
            
            dimensao = largura*comprimento

            'Somar a planta usada'
            if planta == 1:
                somaCajueiro += 1
                areaCajueiro += dimensao
            elif planta == 2:
                somaMangueira += 1
                areaMangueira += dimensao
            elif planta == 3:
                somaDende += 1
                areaDende += dimensao
            elif planta == 4:
                somaCoqueiro += 1
                areaCoqueiro += dimensao
            elif planta == 5:
                somaBambu += 1
                areaBambu += dimensao
            elif planta == 6:
                somaIpe += 1
                areaIpe += dimensao

            'Essa parte define qual a planta mais ultilizada no cadastro do reflorestamento.'
            planta_mais_usada = ""           
            if somaCajueiro >= somaMangueira and somaCajueiro >= somaDende and somaCajueiro >= somaCoqueiro and somaCajueiro >= somaBambu and somaCajueiro >= somaIpe:
                planta_mais_usada = planta_mais_usada + "Cajueiro "
            if somaMangueira >= somaCajueiro and somaMangueira >= somaDende and somaMangueira >= somaCoqueiro and somaMangueira >= somaBambu and somaMangueira >= somaIpe:
                planta_mais_usada = planta_mais_usada + "Mangueira "
            if somaDende >= somaCajueiro and somaDende >= somaMangueira and somaDende >= somaCoqueiro and somaDende >= somaBambu and somaDende >= somaIpe:
                planta_mais_usada = planta_mais_usada + "Dendê "
            if somaCoqueiro >= somaCajueiro and somaCoqueiro >= somaMangueira and somaCoqueiro >= somaDende and somaCoqueiro >= somaBambu and somaCoqueiro >= somaIpe:
                planta_mais_usada = planta_mais_usada + "Coqueiro "
            if somaBambu >= somaCajueiro and somaBambu >= somaMangueira and somaBambu >= somaDende and somaBambu >= somaCoqueiro and somaBambu >= somaIpe:
                planta_mais_usada = planta_mais_usada + "Bambu gigante "
            if somaIpe >= somaCajueiro and somaIpe >= somaMangueira and somaIpe >= somaDende and somaIpe >= somaCoqueiro and somaIpe >= somaBambu: 
                planta_mais_usada  = planta_mais_usada + "Ipê "         
            
            'Essa parte define qual a planta menos ultilizada no cadastro do reflorestamento.'
            planta_menos_usada = ""
            if somaCajueiro <= somaMangueira and somaCajueiro <= somaDende and somaCajueiro <= somaCoqueiro and somaCajueiro <= somaBambu and somaCajueiro <= somaIpe:
                planta_menos_usada = planta_menos_usada + "Cajueiro "
            if somaMangueira <= somaCajueiro and somaMangueira <= somaDende and somaMangueira <= somaCoqueiro and somaMangueira <= somaBambu and somaMangueira <= somaIpe:
                planta_menos_usada = planta_menos_usada + "Mangueira "
            if somaDende <= somaCajueiro and somaDende <= somaMangueira and somaDende <= somaCoqueiro and somaDende <= somaBambu and somaDende <= somaIpe:
                planta_menos_usada = planta_menos_usada + "Dendê "
            if somaCoqueiro <= somaCajueiro and somaCoqueiro <= somaMangueira and somaCoqueiro <= somaDende and somaCoqueiro <= somaBambu and somaCoqueiro <= somaIpe:
                planta_menos_usada = planta_menos_usada + "Coqueiro "
            if somaBambu <= somaCajueiro and somaBambu <= somaMangueira and somaBambu <= somaDende and somaBambu <= somaCoqueiro and somaBambu <= somaIpe:
                planta_menos_usada = planta_menos_usada + "Bambu gigante "
            if somaIpe <= somaCajueiro and somaIpe <= somaMangueira and somaIpe <= somaDende and somaIpe <= somaCoqueiro and somaIpe <= somaBambu: 
                planta_menos_usada  = planta_menos_usada + "Ipê "  

            'Essa parte soma as áreas dos estados e quantas vezes foi adcionada uma área no mesmo.'
            if estado == "BA":
                areaBA += dimensao
                somaBA += 1
            elif estado == "MA":
                areaMA += dimensao
                somaMA += 1
            elif estado == "PI":
                areaPI += dimensao
                somaPI += 1
            elif estado == "PE":
                areaPE += dimensao
                somaPE += 1
            elif estado == "SE":
                areaSE += dimensao
                somaSE += 1
            elif estado == "CE":
                areaCE += dimensao
                somaCE += 1
            elif estado == "RN":
                areaRN += dimensao
                somaRN += 1
            elif estado == "PB":
                areaPB += dimensao
                somaPB += 1
            elif estado == "AL":
                areaAL += dimensao
                somaAL += 1

            'Definir qual o estado menos reflorestado.' 
            estado_menos_reflorestado = ''
            if areaBA <= areaMA and areaBA <= areaPI and areaBA <= areaPE and areaBA <= areaSE and areaBA <= areaCE and areaBA <= areaRN and areaBA <= areaPB and areaBA <= areaAL:
                estado_menos_reflorestado = estado_menos_reflorestado + "Bahia "
            if areaMA <= areaBA and areaMA <= areaPI and areaMA <= areaPE and areaMA <= areaSE and areaMA <= areaCE and areaMA <= areaRN and areaMA <= areaPB and areaMA <= areaAL:
                estado_menos_reflorestado = estado_menos_reflorestado + "Maranhão "
            if areaPI <= areaMA and areaPI <= areaPE and areaPI <= areaBA and areaPI <= areaSE and areaPI <= areaCE and areaPI <= areaRN and areaPI <= areaPB and areaPI <= areaAL:
                estado_menos_reflorestado = estado_menos_reflorestado + "Piauí "
            if areaPE <= areaMA and areaPE <= areaPI and areaPE <= areaBA and areaPE <= areaSE and areaPE <= areaCE and areaPE <= areaRN and areaPE <= areaPB and areaPE <= areaAL:
                estado_menos_reflorestado = estado_menos_reflorestado + "Pernambuco " 
            if areaSE <= areaMA and areaSE <= areaPI and areaSE <= areaBA and areaSE <= areaPE and areaSE <= areaCE and areaSE <= areaRN and areaSE <= areaPB and areaSE <= areaAL:
                estado_menos_reflorestado = estado_menos_reflorestado + "Sergipe "
            if areaCE <= areaMA and areaCE <= areaPI and areaCE <= areaBA and areaCE <= areaPE and areaCE <= areaSE and areaCE <= areaRN and areaCE <= areaPB and areaCE <= areaAL:
                estado_menos_reflorestado = estado_menos_reflorestado + "Ceará " 
            if areaRN <= areaMA and areaRN <= areaPI and areaRN <= areaBA and areaRN <= areaPE and areaRN <= areaSE and areaRN <= areaCE and areaRN <= areaPB and areaRN <= areaAL:
                estado_menos_reflorestado = estado_menos_reflorestado + "Rio Grande do Norte "
            if areaPB <= areaMA and areaPB <= areaPI and areaPB <= areaBA and areaPB <= areaPE and areaPB <= areaSE and areaPB <= areaCE and areaPB <= areaRN and areaPB <= areaAL:
                estado_menos_reflorestado = estado_menos_reflorestado + "Paraíba "
            if areaAL <= areaMA and areaAL <= areaPI and areaAL <= areaBA and areaAL <= areaPE and areaAL <= areaSE and areaAL <= areaCE and areaAL <= areaRN and areaAL <= areaPB:
                estado_menos_reflorestado = estado_menos_reflorestado + "Alagoas "    

  
            'Definir informações da maior área.'
            if dimensao == maior_area:
                codigo_da_maior_area = codigo_da_maior_area + ', ' + cod_p_area
                cidade_da_maior_area = cidade_da_maior_area + ', ' + cidade
                maior_area = dimensao
                planta_da_maior_area = planta_da_maior_area + ', ' + nome_da_planta 
                estado_da_maior_area = estado_da_maior_area + ', ' + estado

            if dimensao > maior_area:
                codigo_da_maior_area = cod_p_area
                cidade_da_maior_area = cidade
                maior_area = dimensao
                planta_da_maior_area = nome_da_planta
                estado_da_maior_area = estado 

            'Evitar que os estados menos utilizados se repitam quando for solicitado o relatório de reflorestamento mais de uma vez.'
        ler_estado = ''
        estados_sem_repetir = ''
        for i in estado_menos_reflorestado:
            pode_adicionar = True
            if i != ' ':
                ler_estado = ler_estado + i
            if i == ' ':
                ler_estado_sem_repetir = ''
                for j in estados_sem_repetir:
                    if j != ' ':
                        ler_estado_sem_repetir = ler_estado_sem_repetir + j
                    if j == ' ':
                        if ler_estado == ler_estado_sem_repetir:
                            pode_adicionar = False
                            ler_estado = ''
                        ler_estado_sem_repetir = ''

                if pode_adicionar:
                    estados_sem_repetir = estados_sem_repetir + ler_estado + " "
                    ler_estado = ''

            'Evitar que as plantas menos utilizadas se repitam quando for solicitado o relatório de reflorestamento mais de uma vez.'
        ler_planta = ''
        planta_menos_usada_sem_repetir = ''
        for i in planta_menos_usada:
            pode_adicionar = True
            if i != ' ':
                ler_planta = ler_planta + i
            if i == ' ':
                ler_planta_sem_repetir = ''
                for j in planta_menos_usada_sem_repetir:
                    if j != ' ':
                        ler_planta_sem_repetir = ler_planta_sem_repetir + j
                    if j == ' ':
                        if ler_planta == ler_planta_sem_repetir:
                            pode_adicionar = False
                            ler_planta = ''
                        ler_planta_sem_repetir = ''

                if pode_adicionar:
                    planta_menos_usada_sem_repetir = planta_menos_usada_sem_repetir + ler_planta + " "
                    ler_planta = '' 

            'Evitar que as plantas mais utilizadas se repitam quando for solicitado o relatório de reflorestamento mais de uma vez.'
        ler_planta = ''
        planta_mais_usada_sem_repetir = ''
        for i in planta_mais_usada:
            pode_adicionar = True
            if i != ' ':
                ler_planta = ler_planta + i
            if i == ' ':
                ler_planta_mais_usada_sem_repetir = ''
                for j in planta_mais_usada_sem_repetir:
                    if j != ' ':
                        ler_planta_mais_usada_sem_repetir = ler_planta_mais_usada_sem_repetir + j
                    if j == ' ':
                        if ler_planta == ler_planta_mais_usada_sem_repetir:
                            pode_adicionar = False
                            ler_planta = ''
                        ler_planta_mais_usada_sem_repetir = ''

                if pode_adicionar:
                    planta_mais_usada_sem_repetir = planta_mais_usada_sem_repetir + ler_planta + " "
                    ler_planta = ''                      
            
    if menu == 1:  
        print("-------------------RELATÓRIO---------------------")      
        print(f"A área total reflorestada Alagoas: {areaAL}\nA área total reflorestada Bahia:{areaBA}\nA área total reflorestada Ceará: {areaCE}\nA área total reflorestada Maranhão: {areaMA}\nA área total reflorestada Paraíba: {areaPB}\nA área total reflorestada Pernambuco: {areaPE}\nA área total reflorestada Piauí: {areaPI}\nA área total reflorestada Rio Grande do Norte: {areaRN}\nA área total reflorestada Sergipe: {areaSE}")
        print("-"*50)
        print(f"A área total reflorestada no Nordeste:{areaBA + areaMA + areaAL + areaCE + areaPB + areaPE + areaPI + areaRN + areaSE}")
        print("-"*50)
        print(f"Área total de reflorestamento com Cajueiro: {areaCajueiro}\nÁrea total de reflorestamento com Mangueira: {areaMangueira}\nÁrea total de reflorestamento com Dendê: {areaDende}\nÁrea total de reflorestamento com Coqueiro: {areaCoqueiro}\nÁrea total de reflorestamento com Bambu Gigante: {areaBambu}\nÁrea total de reflorestamento com Ipê: {areaIpe}")
        print("-"*50)
        print(f"A planta mais utilizda: {planta_mais_usada_sem_repetir}\nA planta menos utilizada: {planta_menos_usada_sem_repetir}")
        print("-"*50)
        print(f"informação(ôes) da(s) maior(es) área(s):\nCodigo(s) da(s) área(s): {codigo_da_maior_area}\nCidade(s): {cidade_da_maior_area}\nTamanho da(s) área(s): {maior_area}\nÁrvore(s) utilizada(s): {planta_da_maior_area}\nEstado(s): {estado_da_maior_area}")
        print("-"*50)
        print(f"A quantidade de áreas reflorestadas Alagoas: {somaAL}\nA quantidade de áreas reflorestadas Bahia: {somaBA}\nA quantidade de áreas reflorestadas Ceará: {somaCE}\nA quantidade de áreas reflorestadas Pernambuco: {somaPE}\nA quantidade de áreas reflorestadas Piauí: {somaPI}\nA quantidade de áreas reflorestadas Paraíba: {somaPB}\nA quantidade de áreas reflorestadas Rio Grande do Norte: {somaRN}\nA quantidade de áreas reflorestadas Maranhão: {somaMA}\nA quantidade de áreas reflorestadas Sergipe: {somaSE}")
        print("-"*50)
        print(f"O estado menos reflorestado:{estados_sem_repetir}")
