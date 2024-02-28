matr=[1,2,3]
res=[]
elem=0
comb=0
for i in range(len(matr)):
      res.append(matr[elem])
      while comb<len(matr):
            res.append(matr[comb])
            print(res)
            res.pop()
            comb+=1
      res.clear()
      elem+=1
      comb=0