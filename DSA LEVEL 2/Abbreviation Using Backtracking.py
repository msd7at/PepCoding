strs = input()
def abr(strs, ab, c, pos):
    if pos == len(strs):
      if c == 0:
        print(ab)
      else:
        print(ab + str(c))
      return
    if c<= 0:
        abr(strs, ab + strs[pos], 0, pos + 1)
    else:
        abr(strs, ab + str(c) + strs[pos], 0, pos + 1)
    abr(strs, ab, c + 1, pos + 1)
abr(strs, "", 0, 0)
