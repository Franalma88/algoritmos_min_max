a=int(input("pon un numero para elevar"))
n=int(input("pon un numero al que se va a elevar"))
    
def pow_fast (a,n):
    if n== 0:
        return 1
    
    half= pow_fast(a, n//2)
    
    if n%2 == 0:
        return half* half
    else:
        return half * half * a
    
print(pow_fast(a,n))


