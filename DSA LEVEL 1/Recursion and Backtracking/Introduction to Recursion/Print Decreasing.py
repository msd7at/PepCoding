def main():
    n=int(input())
    def dec(n):
        if n==0:
            return
        print(n)
        dec(n-1)
    dec(n)

if __name__ == "__main__":
    main()
