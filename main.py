# lab 6
# encoder/ decoder
# GitHub with partner

def encode(code_in):
    code_out = ''
    for i in code_in:
        new = int(i)+3
        if new >= 10:
            new -= 10
        code_out += str(new)
    print('Your password has been encoded and stored!\n')
    return code_out


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
        # elif option == '2':
        #     if code_out != '':
        #         decode(code_out)
        else:
            print('Invalid input')


if __name__ == "__main__":
    main()
