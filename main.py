from typing import List

def show_menu() :
    print('Alege optiunea: ')
    print('1.Cea mai lunga secventa de numere prime.')
    print('2.Cea mai lunga secventa de numere formate din numere prime ')

def read_list() -> List[int] :
    '''
    Citim lista
    :return: lista citita
    '''
    lst = []
    lst_str=input('Dati numerele din  lista: ')
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split :
        lst.append(int(num_str))
    return lst


def is_prime(nr) ->int :
    """
    Testam daca numarul nr este prim
    Input
    -nr, numar de tip int, dat de utilizator
    Output
    -True, daca nr prim, False daca nr compus
    """
    if nr<2 :
        return False
    if nr == 2 :
        return True
    for i in range (2, int(nr)) :
        if nr % i == 0 :
            return False
    return True

def prime_digit ( nr ) -> int :
    '''
    Testeaza pentru un numar dat daca este format doar din cifre prime
    :param nr: numarul pentru care testam proprietatea
    :return: True, daca numarul satisface proprietatea, False altfel
    '''
    if nr == 0 :
        return False
    while nr !=0 :
        if not is_prime(nr%10) :
            return False
        nr //= 10
    return True

def get_longest_all_primes(lst: list[int]) -> list[int] :
    """
    Gaseste si returneaza cea mai lunga secventa de numere prime din lista data.
    :param lst: lista in care se cauta secventa cu proprietatea ceruta
    :return: secventa maxima care indeplineste proprietatea ceruta
    """
    secventa_maxima = []
    n = len(lst)
    all_primes = True
    for st in range(n):
        for dr in range(st, n):
            for num in range(st, dr+1):
                all_primes = True
                if not is_prime(lst[num]):
                    all_primes = False
                    break
            if all_primes:
                if dr - st + 1 > len(secventa_maxima):
                    secventa_maxima = lst[st: dr + 1]
    return secventa_maxima

def get_longest_prime_digits(lst: list[int]) -> list[int] :
    """
    Gaseste si returneaza cea mai lunga secventa de numere formate doar din cifre prime din lista data.
    :param lst: lista in care se cauta secventa cu proprietatea ceruta
    :return: secventa maxima care indeplineste proprietatea ceruta
    """
    secventa_maxima = []
    n = len(lst)
    all_digits_primes = True
    for st in range(n):
        for dr in range(st, n):
            for num in range(st, dr+1):
                all_digits_primes = True
                if not prime_digit(lst[int(num)]):
                    all_digits_primes = False
                    break
            if all_digits_primes:
                if dr - st + 1 > len(secventa_maxima):
                    secventa_maxima = lst[st: dr + 1]
    return secventa_maxima

def test_get_longest_all_primes() :
    assert get_longest_all_primes([2, 3, 5, 10, 13, 11]) == [2, 3, 5]
    assert get_longest_all_primes([2, 3, 5, 10, 13, 11, 13 ,41, 29, 100]) == [13, 11, 13, 41, 29]
    assert get_longest_all_primes([10, 20, 15, 18]) == []
    assert get_longest_all_primes([2, 3, 5, 13, 11]) == [2, 3, 5, 13, 11]

def test_get_longest_prime_digits():
    assert get_longest_prime_digits([23, 34, 53, 35, 37, 39]) == [53, 35, 37]
    assert get_longest_prime_digits([14, 15, 16, 17, 18, 19]) == []
    assert get_longest_prime_digits([2, 3, 5, 7, 23 ]) == [2, 3, 5, 7, 23]
    assert get_longest_prime_digits([0, 0, 1, 1, 0, 1]) == []


def main() :
    lst=[]
    while True :
        show_menu()
        optiune = input('Optiunea: ')
        if optiune == '1' :
            lst = read_list()
            print('Cea mai lunga secventa de numere prime este :', get_longest_all_primes(lst))
        elif optiune == '2' :
            lst = read_list()
            print('Cea mai lunga secventa de numere formate doar din cifre prime este :', get_longest_prime_digits(lst))
        elif optiune == 'x' :
            break
        else :
            print('Optiune nevalida.')

if __name__ == '__main__' :
    test_get_longest_all_primes()
    test_get_longest_prime_digits()
    main()
