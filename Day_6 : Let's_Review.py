# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(raw_input())
while(t):
    t-=1
    s= str(raw_input())
    even = ''
    odd = ''
    for i in range(len(s)):
        if i%2==0: even+=s[i]
        else: odd+=s[i]

    print even,odd
        
