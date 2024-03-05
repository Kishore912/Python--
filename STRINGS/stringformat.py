age=32
txt="iam kishore and iam {}"
print(txt.format(age))


h="iam kishore and iam {height} years old and i love {cars}"
print(h.format(height="21" , cars="supra"))

quantity=3
ino=567
price=45
a="i want {} pieces of item {} for {} dollars"
print(a.format(quantity,ino,price))


num=3
price=23
b= "i want {1} pieces for {0} dollars"
print(b.format(num,price))