import getpass
import os

account_list = { #Lista de dicionario
    '0001-02': {
        'password': '123456',
        'name': 'Fulano da Silva',
        'value': 100,
        'admin': False
    },
    '0002-02': {
        'password': '123456',
        'name': 'Cicrano',
        'value': 50,
        'admin': False
    },
    '1111-11': {
        'password': '123456',
        'name': 'Admin da Silva',
        'value': 1000,
        'admin': True
    }   
}
    
money_splips = {
    '20': 5,
    '50': 5,
    '100' : 5
}
    

while True:
    print("************************************")
    print("**** Gabriel - Caixa Eletrônico ****")
    print("************************************")
    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')

    print(account_typed)
    print(password_typed)

    if account_typed in account_list and password_typed == account_list[account_typed]['password']: #Válidado se a conta existe na lista, caso exista eu acesso ela e verifico a senha
        os.system('cls' if os.name == 'nt' else 'clear') #Operação Ternaria
        print("************************************")
        print("**** Gabriel - Caixa Eletrônico ****")
        print("************************************")
        print("1 - Saldo")
        print("2 - Sacar")
        
        if account_list[account_typed]['admin']:
            print("10 - Incluir cédulas")
        option_typed = input("Escolha uma das opções acima: ")
        
        if option_typed == '1':
            print("Seu saldo é %s" % account_list[account_typed]['value'])
        elif option_typed == '10' and account_list[account_typed]['admin']:
            amount_typed = input("Digite a quantidade de cédulas: ")
            money_bill_typed = input("Digite a cédula a ser incluída: ")
            #money_splips[money_bill_typed] = money_splips[money_bill_typed] + int(amount_typed)
            money_splips[money_bill_typed] += int(amount_typed)
            print(money_splips)
        elif option_typed == '2':
            value_typed = input("Digite o valor a ser sacado: ")
            
            
            money_splips_user = {}
            value_int = int(value_typed)
            
            if value_int // 100 > 0 and value_int // 100 <= money_splips['100'] :
                money_splips_user['100'] = value_int // 100
                value_int = value_int - value_int // 100 * 100
                
            if value_int // 50 > 0 and value_int // 50 <= money_splips['50'] :
                money_splips_user['50'] = value_int // 50
                value_int =  value_int -value_int // 50 * 50
                
            if value_int // 20 > 0 and value_int // 20 <= money_splips['20'] :
                money_splips_user['20'] = value_int // 20
                value_int =  value_int - value_int // 20 * 20
                
            if value_int != 0:
                print("O caixa não tem cédulas disponiveis para este valor")
            else:
                for money_bill in money_splips_user:
                    money_splips[money_bill] -= money_splips_user[money_bill]
                    
                print("Pegue as notas: ")
                print(money_splips_user)
            
        else:
            print("Opção inválida")
    else:
        print('Conta inválida')
    input('Pressione <ENTER> para continuar...')# Pause no Programa     
    os.system('cls' if os.name == 'nt' else 'clear')