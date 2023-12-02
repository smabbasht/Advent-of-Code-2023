import re


def read_file(filename):
    with open(filename, 'r') as f:
        data = f.readlines()
    return data


def main():
    data = read_file('input-01')
    word_to_digit = {'one': 'on1ne', 'two': 'tw2wo', 'three': 'thre3hree',
                     'four': 'fou4our', 'five': 'fiv5ive', 'six': 'si6ix', 'seven': 'seve7even',
                     'eight': 'eigh8ight', 'nine': 'nin9ine'}
    getword = '|'.join(word_to_digit.keys())

    for ind in range(len(data)):
        pattern = re.compile(rf'(?:{getword})', re.IGNORECASE)
        data[ind] = pattern.sub(
            lambda match: word_to_digit[match.group(0)], data[ind])
        data[ind] = pattern.sub(
            lambda match: word_to_digit[match.group(0)], data[ind])
        data[ind] = re.sub(r'[^\d]+', '', data[ind])
        if data[ind] == '':
            data[ind] = '0'
        data[ind] = data[ind][0] + data[ind][-1]
        data[ind] = int(data[ind])

    return sum(data)


print(main())
