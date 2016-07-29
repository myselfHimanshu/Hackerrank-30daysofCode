# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
dic = {}
while(N):
    N-=1
    a,b = map(str, raw_input().strip().split())
    dic[a] = b

while True:
    try:
        q = str(raw_input())
        if q in dic:
            print "%s=%s"%(q,dic[q])
        else:
            print "Not found"

    except EOFError:
        break
