import os

import SollarisConfig

Commands = [':q', ':r', ':s', ':c']

working = True

currentLine = 0

fileName = ''


fileContent = ''

os.system('cmd /c color ' + SollarisConfig.color)

print('SollarisIDE by AndrezinGamepão\n \n \n \n')

text = input(str(currentLine) +'>>FileName: ')
fileName = text
file = open(fileName, 'a')
if open(fileName, 'r').read() != '':
    print(open(fileName, 'r').read())

currentLine += 1
while working:

    text = input(str(currentLine) + '>>')

    if text == Commands[0]:

        if open(fileName).read() != fileContent:
            print('Save File?(y/n)')
            text = input('>>>')

            if text == 'y':
                file.write(fileContent)
                print('Saved')
                file.close()
                working = False

            elif text == 'n':
                file.close()
                
                if open(fileName, 'r').read() == '':
                    os.remove(fileName)
                working = False
            print('closing')
            
        else:
            file.close()
            working = False
            print('closing')

    elif text == Commands[1]:
        fileContent = ''
        print(" \n \n \n")
        currentLine = 1

    elif text == Commands[2]:
        file.write(fileContent)
        fileContent = ''
        file.close()
        file = open(fileName, "a")
        print('saved')

    elif text == Commands[3]:
        text = input('Command>>')
        os.system('cmd /c {}'.format(text))

    else:
        currentLine += 1
        fileContent += text + '\n'

    pass