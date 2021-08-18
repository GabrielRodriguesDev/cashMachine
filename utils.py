import os

def clearScren():
    os.system('cls' if os.name == 'nt' else 'clear')

def header():
        print("************************************")
        print("**** Gabriel - Caixa Eletrônico ****")
        print("************************************")