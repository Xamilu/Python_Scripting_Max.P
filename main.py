# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        year = input("Entrez une année: ")
        year_convert = int(year)
        if year_convert % 4 == 0 and year_convert % 100 != 0 or year_convert % 400 == 0:
            year_convert = str(year)
            print('L\'année ' + year_convert + ' est bisextile')
        else:
            year_convert = str(year)
            print('L\'année ' + year_convert + ' n\'est pas bisextile')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
