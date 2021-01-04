"""
BU dosya Python dersi 7. hafta alistirmalarini kapsamaktadir.
"""

def isSihirli (list):
    """
    Sihirli kare: ic ice listeler halinde verilen, 2 boyutlu girdinizin her sirasinin,
    her kolonunun ve her iki kosegeninin toplamlari birbirine esit ise bu kareye sihirli kare diyoruz.
    Bu kod sihirli verilen girdi sihitli kare olduğu zaman ekrana 0 bastirir
    """
    toplam=[0,0]
    toplamr=[]
    toplamc=[0]*len(list[0])
    for i in range (len(list[0])):
        for j in range (len(list[0])):
            if (i==j):
                toplam[0]=toplam[0] + list[i][i]
    for i in range (len(list[0])):
        for j in range (len(list[0])):
            if (j==len(list[0])-i-1):
                toplam[1]=toplam[1] + list[i][j]
    for i in range (len (list)):
        toplamr.append(sum(list[i]))
    for i in range (len (list[0])):
        for j in range(len(list)):
            toplamc[i]=toplamc[i]+list[j][i]


    toplamx=toplam+toplamc+toplamr
    if min(toplamx)==max(toplamx): print(0)
    else : print(1)
def maksList(list1,list2):
    """
    Bu kod verien iki listenin elemanlarini karsilastirip büyük olani yeni bir listeye atar
    """
    list=[]
    for i in range (len(list1)):
        if list1[i]<list2[i]: list.append(list2[i])
        else: list.append(list1[i])
    print(list)
def isPal(list):
    """
    Stack veri yapisi kullanilarak bir listenin palindrome olup olmadigini kontrol eden kod
    Stack: sadece 1 yerden ekleme ve cikarma yapilabilen Bitişik Listeler (Contiguous Lists).
    Bu ornekte sadece 0. elemandan (listenin basindan) ekleme ve cikarma yapildi.
    """
    list1=[]
    list2=[]
    for i in range (len(list)):
        list1.insert(0,list[i])
    for i in range(len(list1)):
        list2.insert(0, list1[i])
    for i in range (len (list1)):
        if list1[i]!=list2[i]:
            print(1)
            return
    print(0)
def isPer(x):
    """
    Kuyruk veri yapisi kullanilarak bir sayinin mukemmel sayi olup olmadigini kontrol eden kod
    Kuyruk: Sadece sonundan ekleme ve cikarma yapilan bitisik listeler
    Mukemmel Sayi: Kendi haric tum bolenleri kendine esit olan sayi
    """
    a=1
    bolen=[]
    while a<=(x/2):
        if x%a==0:
            bolen.append(a)
        a=a+1
    if sum(bolen)==x: print(0)
    else: print(1)


def listeDil(list,l,r):
    """
    :param list: Verilien Liste
    :param l: Sol indeks
    :param r: Sag indeks
    :return: Verilen liste sol ve sag indeks ile bolunur. Eleman bazli toplama yapilir ve ekrana basilir.
    """
    nlist=list[l:r]
    slist=[]
    for i in range (len(nlist[0])):
        toplam=0
        for j in range (len(nlist)):
            toplam=toplam+nlist[j][i]
        slist.append(toplam)
    print(slist)

def stackOp(liste,op,x):
    """
    Verilen op girdisine göre belirli islemler yapacak kod.
    :param liste: verilen liste
    :param op: op + ise listeye ekleme, - ise listeden cikarma ve ? ise listenin ilk elemanini yazdirma
    :param x: listeye eklenecek eleman
    """
    if (op=="+"):
        liste.insert(0,x)
        print(liste)
    elif (op=="-"):
        liste.pop(0)
        print(liste)
    elif (op=="?"): print(liste[0])
#a=1
#b=3
#c=[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
#listeDil(c,a,b)
#isPer(a)
#isSihirli(a)
#maksList(aa,bb)
#print(isPer.__doc__)
#isPal(cc)
x=[1,2,3,4,5,6,9]
stackOp(x,'?',2)