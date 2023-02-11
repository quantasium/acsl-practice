# Converting to Decimal

# 1101@2 = 1 * 2^3 + 1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 8 + 4 + 0 + 1 + 13@10

# Number to convert
# Base number is in


def toDecimal(n, b):
  ans = 0
  i = 1

  for c in str(n):
    ans += int(int(c) * (b**(len(str(n)) - i)))
    i += 1
  return ans


print("\n\nAnswer: " + str(toDecimal(1101, 2)))
