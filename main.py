from file import loadBankData
from back_account_variables import money_splips, account_list
import utils
import operations



def main():
    loadBankData()
    print(money_splips)
    print(account_list)
    utils.header()
    account_auth = operations.authAccount()
    
    if account_auth:
        utils.clearScren()
        
        utils.header()
        
        option_typed = operations.getMenuOptionsTyped(account_auth)
        operations.doOperation(option_typed, account_auth)
    else:
        print("Conta inválida")

if __name__ == '__main__':
    while True:
        
        main()
        input('Pressione <ENTER> para continuar...')# Pause no Programa     
        utils.clearScren()