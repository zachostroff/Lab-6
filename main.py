# lab 6
# encoder/ decoder
# GitHub with partner
# started by zachary ostroff
# collaborated on by Jaxon Russell

def encode(code_in):
    code_out = ''
    for i in code_in:
        new = int(i)+3
        if new >= 10:
            new -= 10
        code_out += str(new)
    print('Your password has been encoded and stored!\n')
    return code_out

def decode(encString):
    decString = ''

    for i in encString:
        num = int(i) - 3
        if num < 0:
            num += 10
        decString += str(num)
    return decString


def main():
    go = True
    code_out = ''
    while go:
        print('Menu\n'
              '-------------\n'
              '1. Encode\n'
              '2. Decode\n'
              '3. Quit\n')

        option = input('Please enter an option: ')
        if option == '3':
            go = False
            break
        elif option == '1':
            code_in = input('Please enter your password to encode: ')
            code_out = encode(code_in)
        elif option == '2':
             if code_out != '':
                 decString = decode(code_out)
                 print(f'The encoded password is {code_out}, and the original password is {decString}.\n')
        else:
            print('Invalid input')


if __name__ == "__main__":
    main()
