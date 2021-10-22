def function(x):
   a = lambda x=x: x
   x = 5
   b = lambda: x
   return a,b
aa, bb = function(2)
print(aa())
print(bb())