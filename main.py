import argparse
import sys

from Lab3.Factory.factory import Factory


def func_pars(file_from, file_to, format_from, format_to):
    ser_from = Factory.parser(format_from)
    ser_to = Factory.parser(format_to)

    res = ser_from.load(f'/home/asus/Labs/PythonLabs/{file_from}')
    print(res)

    ser_to.dump(res, file_to)


def main():
    parser = argparse.ArgumentParser(prog='my_prog', description='Serializer')
    parser.add_argument('file_from', type=str, help='from file')
    parser.add_argument('file_to', type=str, help='to file')
    parser.add_argument('format_from', type=str, help='from format type')
    parser.add_argument('format_to', type=str, help='to format type')

    args = parser.parse_args()

    file_from = args.file_from
    file_to = args.file_to
    format_from = args.format_from
    format_to = args.format_to

    if file_from == '' or file_to == '' or format_from == '' or format_to == '':
        print('Error, args is missing!')
        sys.exit()
    else:
        func_pars(file_from, file_to, format_from, format_to)


if __name__ == '__main__':
    main()
