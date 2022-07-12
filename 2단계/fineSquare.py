def findGcd(a,b):
    if b>a :
        a,b = b,a
    while(b!=0):
        n = a % b
        a = b 
        b = n
    return a 

def solution(w,h):
    gcd = findGcd(w,h)
    area = w*h
    return area - (w+h-gcd)
        
            