n = int(input("Number: ") )
j = 0
while j <= n:
  x=j%3
  z=j%5
  if x + z == 0:
    l= str(j)
    print(l +" Fizzbuzz")
  elif x == 0:
    b= str(j)
    print(b + " Fizz")
  elif z == 0:
    v= str(j)
    print(v + " Buzz")
  else:
    print(j)
  j=j+1



 
