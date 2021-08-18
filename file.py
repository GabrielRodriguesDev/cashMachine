from main_test import functionTest
print('file', __name__)
import os
from back_account_variables import money_splips, account_list
BASE_PATH = os.path.dirname(os.path.abspath(__file__))

print(BASE_PATH)

'''
file = open(BASE_PATH + '/file_test.dat','a')
file.write('Tu vai conseguir entender')
file.write('\n')
file.write('Gabriel tu vai conseguir chegar lá')
file.close()


file = open(BASE_PATH + '/file_test.dat','r')

#print(file.read(10) + ' ' + file.read(115))
#print(file.readline(7))
#print(file.readline())
lines = file.readlines()
file.close()

for line in lines:
    print(line)
'''

def openFileBank(mode):
    return open(BASE_PATH + '/bank_file.dat', mode)



def writeMoneySlips(file): 
    for money_bill, value in money_splips.items():
        file.write(money_bill + '=' + str(value) + ';')
        
def writeBankAccounts(file):
    for account, account_data in account_list.items():
        file.writelines((
                        account, ';',
                        account_data['name'], ';',
                        account_data['password'], ';',
                        str(account_data['value']), ';',
                        str(account_data['admin']), ';',
                        '\n'
                        ))
        
def readMoneySlips(file):
    line = file.readline()  #Ele lê a linha
    while line.find(';') != -1: #Varre a linha enquanto encontrar o ponto e virgula (Caso não encontre ele retorna o -1 por isso tem que ser diferente de -1)
        semicolon_pos = line.find(';')  #Procura novamente o ; e aloca o indice na variavel
        money_bill_value = line[0:semicolon_pos] #Atribui na variavel toda a informação do inicio até o ponto e virgula encontrado
        setMoneyBillValue(money_bill_value) 
        if semicolon_pos + 1 == len(line): #Se o indice do ponto e virgula encontrado anteriormente + 1 for igual ao total da linha
            break #Para o while, para não entrar em loop
        else:
            line = line[semicolon_pos+1:len(line)] #Caso não seja a linha recebe o resto da linha não lida (depois do indice do ultimo ponto e virgula encontrado até o fim da linha)
        
def setMoneyBillValue(money_bill_value):
    equal_pos = money_bill_value.find('=')
    money_bill = money_bill_value[0:equal_pos]
    count_money_bill_value = len(money_bill_value)
    value = money_bill_value[equal_pos + 1:count_money_bill_value]
    money_splips[money_bill] = int(value)
    
def readBankAccounts(file):
    lines = file.readlines() #Lendo as linhas do arquivo
    lines = lines[1 : len(lines)] #Pulando a primeira linha que é referente as cédulas
    for account_line in lines:
        extractBankAccount(account_line)
    
        

def extractBankAccount(account_line):
    account_data = []
    while account_line.find(';') != -1:
        semicolon_pos = account_line.find(';') 
        data = account_line[0:semicolon_pos]
        account_data.append(data)
        if semicolon_pos + 1 == len(account_line):
            break 
        else:
            account_line = account_line[semicolon_pos+1:len(account_line)]
    addBankAccount(account_data)

def addBankAccount(account_data):
    account_list[account_data[0]] = {
        'name': account_data[1],
        'password': account_data[2],
        'value': float(account_data[3]),
        'admin': bool(account_data[4])
    }
    

def loadBankData():
    file = openFileBank('r')
    readMoneySlips(file)
    file.close()
    file = openFileBank('r')
    readBankAccounts(file)
    file.close()


def saveMoneySlips():
    file = openFileBank('r')
    lines = file.readlines()
    file.close()
    ##
    file = openFileBank('w')
    lines[0] = ""
    for money_bill, value in money_splips.items():
        lines[0] += money_bill + '=' + str(value) + ';'
    lines[0] += '\n'
    file.writelines(lines)
    file.close()
    
    
def deleteFile():
    file = open(BASE_PATH + '/_file_to_delete.dat', 'w')
    file.close()
    os.unlink(BASE_PATH + '/_file_to_delete.dat')
    