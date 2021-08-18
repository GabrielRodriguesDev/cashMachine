from os import close
from file import writeBankAccounts, writeMoneySlips, openFileBank
from utils import header

def main():
    header()
    MakeMoneySlips('w')
    file = openFileBank('a')
    file.write('\n')
    file.close()
    MakeBankAccounts('a')
        
def MakeMoneySlips(mode):
    file = openFileBank(mode)
    writeMoneySlips(file)
    file.close()
    print('Cédulas gravadas com sucesso')
    
def MakeBankAccounts(mode):
    file = openFileBank(mode)
    writeBankAccounts(file)
    file.close()
    print('Contas bancárias gravadas com sucesso')    
    
    

main()