
def maxx(s,n): 
  c=[0]*256
  for i in range(n): 
    c[ord(s[i])] += 1
  m = 0
  for i in range(256):
    if (c[i] != 0):
      m += 1
  return m 
  
def small_sub(s): 
  
    n = len(s)    
    max1 = maxx(s, n)
    m2 = n
    i=j=0    
    while(i<=n):
        while(j<=n): 
            st = s[i:j] 
            s1 = len(st) 
            sub_dis = maxx(st,s1) 
            if (s1 < m2 and max1 == sub_dis):
              m2 = s1
            j+=1
        i+=1
    return m2
s = input()
l = small_sub(s) 
print(l) 
