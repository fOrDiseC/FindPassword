import re,os

def findAllPasswords(text):
    #  задаем паттерн
    loginRegexp = re.compile(r'''
        ([Ll]ogin.)?        
        ([Лл]огин.)?
        ([Pp]ass.)?        #Слово pass  , не обязательно 
        ([Pp]assword.)?        #Слово password , не обязательно 
        ([Пп]ароль.)?        #Слово пароль  , не обязательно 
        ([A-Za-z0-9@#$%^&+=]{8,}) #выражение для пароля  


        ''', re.VERBOSE)

    # ищем все совпадения
    loginmatches = []

    for logins in loginRegexp.findall(text):
        mylogin = logins

        loginmatches.append(mylogin)

    return loginmatches



def main():

    path = os.getcwd()
    match=[]
    for root, dirs, files in os.walk(path):
        for file in files:
               if file.endswith('.txt'):
                filepath=os.path.join(root, file)
                match.append(filepath)
    file1 = open('savedPasswords.txt', 'w', encoding='UTF-8')
    for files in match:
        # print(files)

        file = open(files, 'r')
        text = file.read()
        listpasswords =(findAllPasswords(text))
        for i in range(len(listpasswords)):
             temp =listpasswords[i]
             temp1 =' '.join(temp).replace(' ','')

             file1.write(temp1)
             file1.write('\n')
        file.close()
    file1.close()

if __name__ == '__main__':
    main()


