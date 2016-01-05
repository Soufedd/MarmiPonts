c="mynuit"
a="abcdefghijklmnopqrstuvwxyz"

l1="si la vie n'est qu'un passage, sur ce passage au moins, semons des fleurs"
l2=" i la vie n'est qu'un passage, sur ce passage au moins, semons des fleurs"


def code(l,c):
    s=""
    j=0
    for i in range(len(l)):
        if (l[i] in a)==True:
            u=a.index(c[j%len(c)])
            v=a.index(l[i])
            h=(u+v)%26
            s=s+a[h]
            j+=1
        else:
            s=s+l[i]
    return s

print(code(l1,c))
print(code(l2,c))          