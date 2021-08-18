from file import saveMoneySlips
import getpass
from back_account_variables import account_list, money_splips, money_splips_user #Important only what I need

def doOperation(option_typed, account_auth):
    if option_typed == '1':
        showBalance(account_auth)
    elif option_typed == '10' and account_list[account_auth]['admin']:
        insertMoneySplips()
    elif option_typed == '2':
        withdraw()
        
def showBalance(account_auth):
    print("Seu saldo é %s" % account_list[account_auth]['value'])

def insertMoneySplips():
    amount_typed = input("Digite a quantidade de cédulas: ")
    money_bill_typed = input("Digite a cédula a ser incluída: ")
    money_splips[money_bill_typed] += int(amount_typed)
    print(money_splips)

def withdraw():
    value_typed = input("Digite o valor a ser sacado: ")
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
        saveMoneySlips()
        print("Pegue as notas: ")
        print(money_splips_user)
        
def getMenuOptionsTyped(account_auth):
    print("1 - Saldo")
    print("2 - Sacar")        
    if account_list[account_auth]['admin']:
        print("10 - Incluir cédulas")
    return input("Escolha uma das opções acima: ")
        
def authAccount():    
    account_typed = input('Digite sua conta: ')
    password_typed = getpass.getpass('Digite sua senha: ')
    if account_typed in account_list and password_typed == account_list[account_typed]['password']: #Válidado se a conta existe na lista, caso exista eu acesso ela e verifico a senha
        return account_typed
    else:
        return False

