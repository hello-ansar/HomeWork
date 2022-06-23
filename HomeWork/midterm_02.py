def task_00():
    '''greeting
    input : -
    output: greeting string
    task  : fix change function behavious so that it will return your name
    Pay attention to punctuation, spelling, grammar, and capitals
    '''
    firstname = 'Diego'
    lastname = 'de la vega'
    greeting = 'Hello! ' + 'My name is ' + firstname + '.'
    return greeting

def task_01(t=1, v = 100, g = 9.8):
    '''fix formula
    input : t time, v initial velocity, g standard gravity value
    output: y height at time t
    task  : fix y component formula of equation of Ballistic Flight 
    '''

    y = v * t - 1 / (2) * g * t **2
    return y

def task_02(m1=2000000, m2=3000000, d=10):
    '''fix formula
    input : m1 mass, m2 mass, d distance
    output: F attractive force
    task  : fix formula of equation for universal gravitation
    '''
    G = 6.6743*10**(-11)
    F = G * m1 * m2 / d**2
    return F

def task_03(n=1000):
    '''fix for loop
    input : n integer
    output: sum of odd number cubes
    task  : now the function counts the sum of integers, 
    change the behaviour of the function so that it will count sum of odd numbers cubes
    '''
    result = 1              
    for i in range(n+1): 
        if i % 2 == 1:
            result += pow(i, 3)
    return result           

def task_04(n = 99):
    '''fix while loop
    input : n integer
    output: a integer
    task  : find such a square value a that its square is bigger than n
    '''
    a = 10
    while a < n:
        z = a
        a = a ** a
        if(a > n):
            break
        a = z + 1
    return a

def task_05(s='123qweads,.?'): 
    """count constants
    input : s string
    output: c number of constants
    task  : now it counts vowels, change code so that it will count constants instead
    """
    vowels = 'aeiouy'        
    c = 0                    
    for i in vowels:
        if i in s:
            c += 1           
    return c                 

def task_06(s='example of the camel string'):
    '''camel string
    input : s string 
    output: t string 
    task  : modify s string so that it will look like camel string 
    ExAmPlE Of tHe cAmEl sTrInG'''
    t = ''
    q = 0
    for i in s:
        if q % 2 == 0:
            t += i.upper()
        else:
            t += i.lower()
        q += 1

    return t

def task_07(s = 'Radar'):
    '''palindrome 
    input : s string 
    output: b bool
    task  : return True if s is palindrome and false if s is not palindrome
    palindrome is a word that reads the same backwards as forwards, e.g. madam.
    '''
    s.lower()

    q = len(s) - 1
    b = True
    for i in range(int(len(s) / 2)):
        if(s[i] != s[q]):
            b = False
        q -= 1

    return b

def task_08(s='pinguin'):
    '''animal sound (dict problem)
    input : s string animal type
    output: t sound that animal says
    task  : return sound for requested animal
    i.e. task_08('cat') should return 'meow' 
    taks_08('pinguin') should return None
    '''

    animals_sound = {"bee": "buzz",
                     "bear": "grrr",
                     "cat": "meow",
                     "chicken": "cluck",
                     "cow": "moo",
                     "dog": "woof",
                     "donkey": "hee - haw",
                     "frog": "ribbit",
                     "horse": "neigh",
                     "sheep": "baa",
                     "pig": "oink",
                     "mouse": "squeak",
                     "owl": "whoo - whoo",
                     "rooster": "cock - a - doodle - doo",
                     "snake": "hiss"
                     }
    if s in animals_sound:
        t = animals_sound[s]
    else:
        t = None
    return t

def task_09(a = [1, 1, 1], b = 1):
    """frequency
    input : a list of numbers, b number
    output: f frequency of b number in a list 
    task  : fix code so that it will return frequence for an asked number in the list
    """
    c = 0
    for i in a:
        if i == b: 
            c += 1
    f = c
    return f

def task_10(n = 100):
    """signum number
    input : n number
    output: s signum of a number
    task  : fix code so that it will return signum value
    signum of a number is a sign of a number 
    """

    if n > 0:
        s = 1
    elif n < 0:
        s = -1
    else:
        s = 0
    return s

def task_11(a=1, b=2):
    '''doctest
    input : a integer, b integer
    output: smallest value 
    task  : write 3-5 doctest cases

    # write test here
    
    '''
    import math
    smallest = a if a < b else b
    try:
        smallest = a//b
    except ZeroDivisionError:
        smallest = "Denominator can't be zero"

    if not a >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(a) != a:
        raise ValueError("n must be exact integer")
    if a+1 == a:
        raise OverflowError("n too large")
    smallest = math.factorial(a)
    return smallest

def task_12(file = 'my_text.txt'):
    ''' file
    input : file filename
    output: number of vowels in file
    task  : count number of vowels for any given file
    '''
    vowels = 'aeiouy'
    with open(file) as f:
        c = 0
        s = f.read()
        for i in s:
            if i in vowels:
                c += 1
    return c



def task_13(a=[2, 3, 4, 5, 7, 9, 11]):
    ''' module
    input : a list
    output: b value of double median of a list
    task  : import function median from my_module.py file
            and return double value for given list of numbers
    '''
    from my_module import median

    b = median(a)
    return b


def task_14(n=5):
    """
    input : n number
    output: f factorial of n number
    task  : write a function that will return factorial 
    """
    import math

    return math.factorial(n)

    # write your code here

def task_15(a=[5,4,3,2,1]):
    '''bubble_sort
    input : a list of numbers
    output: b sorted list of numbers using bubble sort
    task  : write a code that will return list sorted using bubble sort algorithm
    '''
    from random import randint


    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

    return a

if __name__ == '__main__':
    ''' please do not change this block'''
    print(0, task_00())
    print(1, task_01())
    print(2, task_02())
    print(3, task_03())
    print(4, task_04())
    print(5, task_05())
    print(6, task_06())
    print(7, task_07())
    print(8, task_08())
    print(9, task_09())
    print(10, task_10())
    print(11, task_11())
    print(12, task_12())
    print(13, task_13())
    print(14, task_14())
    print(15, task_15())
    
    import doctest
    doctest.testmod(verbose=True)