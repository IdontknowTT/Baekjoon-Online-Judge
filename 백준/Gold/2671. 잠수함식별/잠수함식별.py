import sys
import re 

word = str(sys.stdin.readline().rstrip("\n"))
pattern = re.compile('(100+1+|01)+') 
res = pattern.fullmatch(word) 

if res:
    print("SUBMARINE")
else:
    print("NOISE")