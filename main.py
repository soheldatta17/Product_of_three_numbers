for i in range(int(input())):
    n=int(input())
    a=b=c=1
    i=2
    while i*i<=n:
        if n%i==0:
            a=i
            break
        i+=1
    n=int(n/a)
    j=a+1
    while j*j<=n:
        if n%j==0:
            b=j
            break
        j+=1
    c=int(n/b)
    print(f"YES\n{a} {b} {c}") if (a!=b and b!=c and a!=1 and b!=1 and c!=1) else print("NO")