## This function will count the number of consonants in arg string
## and return that number.
def countConsonants(string):
## list of consonants
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
                  'r', 's', 't', 'v', 'w', 'x', 'z']
    num = 0
## convert string to all lowercase
    string = string.lower()
## index through string and count consonants
    for letter in string:
        if letter in consonants:
            num = num + 1
## return number of consonants
    return num
    

## This function will count the number of vowels in arg string
## and return that number.
def countVowels(string):
## list of vowels
    vowels = ['a','e','i','o','u','y']
    num = 0
## convert string to all lowercase
    string = string.lower()
## index through string and count vowels
    for letter in string:
        if letter in vowels:
            num = num + 1
## return number of vowels
    return num

def main():
## gather string input
    string = input('Enter any string and I will tell you the number of vowels and consonants in it: ')
## calcuate number of consonants and vowels
    numConsonants = countConsonants(string)
    numVowels = countVowels(string)
## print results
    print (f'The number of vowels in string: {string} is {numVowels}. The number of consonants is {numConsonants}.')

## call main function
if __name__== '__main__':
    main()
