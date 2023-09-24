if __name__ == '__main__':
    while(True):
        print('Welcome to Edyoda:\n1 : Log in\n2 : Sign\n3 : Exit')
        try :
            c = int(input("enter any option"))
            print(c)
            if c == 1:
                print('LogedIn')
            elif c == 2:
                print('Sign Up')
            elif c == 3:
                print('Thank you , Please visit again')
                break
            else:
                print('Please select correct option')
            break
        except:
            print('please select correct option')


            

