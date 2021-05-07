#nested function
# def f():
#     print("kl rahul")
#     s='i love india'
#     def se():
#         s='my name is ankita'
#         print(s)
#     se()
#     print(s)
    
# print(f())      
# print("kl rahul")



#
# def h(a,b,c):
#     if a>b and a>c:
#         print(a,"first no is max")
#     elif b>a and b>c:
#         print(b,"second is max")
#     else:
#         print(c,"third is max")
# h(1234,34,56)
# l=[2,3,2]
# print(sum(l))

#reversed
def l(q):
    k=""
    i=len(q)
    while i>0:
        k+=q[i-1]
        i-=1
    return k
print(l('123ad'))


# def k(s):
#     d={"UPPER_CASE":0,"LOWER_CASE":0}
#     for c in s:
#         if c.isupper():
#             d["UPPER_CASE"]+=1
#         elif c.islower():
#             d["LOWER_CASE"]+=1
#         else:
#             pass
#     print("origanal",s)
#     print("no.of upper case letters",d["UPPER_CASE"])
#     print("no of lower case letters",d["LOWER_CASE"])
# k('The quick Brown Fox')

# def h(d):
#     p=[]
#     i=0
#     while i<len(d):
#         if d[i] not in p:
#             p.append(d[i])
#         i+=1
#     print(p)
# h(d=[1,2,23,1,1,12,3,3,3,23,32])



#split 
# p="ankita shantaram pisal"
# a=p.split(" ")
# print(a)

#join
# P="ANKITA PISAL"
# a="_".join(P)
# print(a)

#REPLACE:
# a="sunflower"
# b=a.replace("sun","moon")
# print(b)

