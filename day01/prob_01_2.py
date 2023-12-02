import re


def read_file(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    return data


def main():
    data = read_file('input-01')

    for ind in range(len(data)):
        data[ind] = re.sub(r'[^\d]+', '', data[ind])
        if data[ind] == '':
            data[ind] = '0'
        data[ind] = data[ind][0] + data[ind][-1]
        data[ind] = int(data[ind])

    return sum(data)


print(main())
