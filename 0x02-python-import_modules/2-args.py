#!/usr/bin/python3
if _name_ == "__main__":
    arglen = len(argv) - 1
    if arglen == 0:
        print('0 arguments.')
    elif arglen == 1:
        print('1 argument:')
        print('1: {}'. format(argv[1]))
    else:
        print('{} arguments:'.format(arglen))
        for i in range(1, len(argv)):
            print('{}: {}'.format(i, argv[i]))
