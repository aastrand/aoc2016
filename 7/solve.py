#!/usr/bin/env python3

import sys


def parse(f):
    ls = []
    for l in open(f, 'r'):
        l = l.strip()
        ip = []
        hnet = []

        idx = l.find('[')
        while idx > -1:
            ip.append(l[:l.find('[')])
            hnet.append(l[l.find('[')+1:l.find(']')])
            l = l[l.find(']')+1:]
            idx = l.find('[')

        ip.append(l[l.find(']')+1:])
        ls.append((ip, hnet))

    return ls


def has_abba(str):
    for i in range(len(str)-3):
        if str[i] != str[i+1] and str[i] == str[i+3] and str[i+1] == str[i+2]:
            return True
    return False


def get_abas(ls):
    abas = set()
    for str in ls:
        for i in range(len(str)-2):
            if str[i] == str[i+2] and str[i] != str[i+1]:
                abas.add(str[i]+str[i+1]+str[i+2])
    return abas


def to_babs(abas):
    babs = set()
    for aba in abas:
        babs.add(aba[1]+aba[0]+aba[1])
    return babs


def supports_tls(tpl):
    found_valid_abba = False
    for hnet in tpl[1]:
        found_valid_abba |= has_abba(hnet)

    if not found_valid_abba:
        for ip in tpl[0]:
            found_valid_abba |= has_abba(ip)
    else:
        return False

    return found_valid_abba


def supports_ssl(tpl):
    abas = get_abas(tpl[0])
    babs = to_babs(get_abas(tpl[1]))

    return len(abas & babs) > 0


def test():
    assert True == has_abba('abba')
    assert True == has_abba('aaabba')
    assert False == has_abba('aaaa')
    assert False == has_abba('hejhejhej')

    assert True == supports_tls((['abba', 'hejhejhej'], ['aaaa']))

    # abba[mnop]qrst supports TLS (abba outside square brackets).
    assert True == supports_tls((['abba', 'qrst'], ['mnop']))

    # abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
    assert False == supports_tls((['abcd', 'xyyx'], ['bddb']))

    # aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
    assert False == supports_tls((['aaaa', 'tyui'], ['qwer']))

    # ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
    assert True == supports_tls((['ioxxoj', 'zxcvbn'], ['asdfgh']))

    assert set(['xax']) == get_abas(['xax', 'apor'])
    assert set(['axa']) == to_babs(set(['xax']))

    # aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
    assert True == supports_ssl((['aba', 'xyz'], ['bab']))

    # xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
    assert False == supports_ssl((['xyx', 'xyx'], ['xyx']))

    # aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
    assert True == supports_ssl((['aaa', 'eke'], ['kek']))

    # zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
    assert True == supports_ssl((['zazbz', 'cdb'], ['bzb']))


def main(f):
    test()

    ls = parse(f)
    tls_count = 0
    ssl_count = 0

    for ip in ls:
        if supports_tls(ip):
            tls_count += 1
        if supports_ssl(ip):
            ssl_count += 1

    print(tls_count)
    print(ssl_count)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))
