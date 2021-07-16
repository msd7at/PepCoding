def prn(s, ans):
    if s == "":
        print(ans)
        return
    ch = s[0]
    roq = s[1:]
    cho = d[ch]
    for i in cho:
        prn(roq, ans + i)


if __name__ == "__main__":
    n = input()
    d = {
        "0": ".;",
        "1": "abc",
        "2": "def",
        "3": "ghi",
        "4": "jkl",
        "5": "mno",
        "6": "pqrs",
        "7": "tu",
        "8": "vwx",
        "9": "yz",
    }

    prn(n, "")
