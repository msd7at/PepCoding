def main():
    n=int(input())
    def dec(n,i):
        if n+1==i:
            return
        print(i)
        dec(n,i+1)
    dec(n,1)

if __name__ == "__main__":
    main()
