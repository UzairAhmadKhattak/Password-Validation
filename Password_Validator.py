
import string


def validating_password(password):
    alpha_list = string.ascii_uppercase.replace('',' ').strip().split(' ')
    symbols = string.punctuation.replace('',' ').strip().split(' ')
    numb_list = string.digits.replace('',' ').strip().split(' ')
    sys=[]
    num=[]
    alph=[]
    for item in password:
        if item in symbols:
            sys.append(True)
        if item in numb_list:
            num.append(True)
        if item in alpha_list:
            alph.append(True)

    if True in sys and True in num and True in alph:
        print('All condition saticefied')
    else:
        print('password invalid')


validating_password('!aa1Ajnbv')




