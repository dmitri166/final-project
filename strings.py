"""With this string:
'monty pythons flying circus'
Create a function that returns a sorted string with no duplicate characters
(keep any whitespace):
Example: ' cfghilmnoprstuy'
Create a function that returns the words in reverse order:
Example: ['circus', 'flying', 'pythons', 'monty']
Create a function that returns a list of 4 character strings:
Example: ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']

"""
import pytest

def no_duplicates():
    x = ('monty pythons flying circus')
    a = ''.join(sorted(set(x)))
    print(a)
no_duplicates()

    #pass


def reversed_words():
    x = ['circus', 'flying', 'pythons', 'monty']
    a = x[4::-1]
    print(a)
reversed_words()
    #pass


def four_char_strings(s):
    return [s[i: i + 4] for i in range(0, len(s), 4)]
x = four_char_strings('monty pythons flying circus')
print(x)






    #pass


#def test_no_duplicates():
    #s = 'monty pythons flying circus'
    #assert no_duplicates(s) == ' cfghilmnoprstuy'


#def test_reversed_words():
    #s = 'monty pythons flying circus'
    #assert reversed_words(s) == ['circus', 'flying', 'pythons', 'monty']


#def test_four_char_strings():
    #s = 'monty pythons flying circus'
    #assert four_char_strings(s) == ['mont', 'y py', 'thon', 's fl', 'ying', ' cir', 'cus']


#def main():
    #return pytest.main(__file__)


#if __name__ == '__main__':
    #main()