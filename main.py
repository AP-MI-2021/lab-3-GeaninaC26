from typing import List

def show_menu() :
    print('Alege optiunea: ')
    print('1.Cea mai lunga secventa de numere prime.')
    print('2.Cea mai lunga secventa de numere formate din numere prime ')

def read_list() -> List[int] :
    lst = []
    lst_str=input('Dati numerele din  lista: ')
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split :
        lst.append(int(num_str))
    return lst


def is_prime(nr):
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
    for i in range (2, nr) :
        if nr % i == 0 :
            return False
    return True

def prime_digit ( nr ) :
    while nr !=0 :
        if not is_prime(nr%10) :
            return False
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



def test_get_longest_all_primes() :
    assert get_longest_all_primes([2, 3, 5, 10, 13, 11]) == [2, 3, 5]
    assert get_longest_all_primes([2, 3, 5, 10, 13, 11, 13 ,41, 29, 100]) == [13, 11, 13, 41, 29]
    assert get_longest_all_primes([10, 20, 15, 18]) == []
    assert get_longest_all_primes([2, 3, 5, 13, 11]) == [2, 3, 5, 13, 11]

def main() :
    lst=[]
    while True :
        show_menu()
        optiune = input('Optiunea: ')
        if optiune == '1' :
            lst = read_list()
            print('Cea mai lunga secventa de numere prime este :', get_longest_all_primes(lst))
        elif optiune == '2' :
            pass
        elif optiune == 'x' :
            break
        else :
            print('Optiune nevalida.')

if __name__ == '__main__' :
    main()
