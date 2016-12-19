name = 'zhangxt'
pw = 'passwd'
counter = 0
while counter < 3:
    username = input('Enter your username: ')
    password = input('Enter your password: ')
    if username == name and password == pw:
        print('Welcome %s!' % name)
        break
    else:
        counter += 1
        if counter < 3:
            print('wrong username or password,please try it again')
        else:
            print('you have try three times,lock user!')