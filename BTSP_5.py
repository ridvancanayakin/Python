"""
Bu dosya pyhton dersi 5. hafta alistirmalarini kapsamaktadir.

"""
def bir():
    """
    Bir liste olusturup bu listeye eleman ekleyip cikarilarak ekrana bastirilan bir fonksiyon
    """
    list=[]
    x=10
    y="abcdefghijklmnopqrstuvwxyz"
    while x <21:
        list.append(x)
        x=x+1
    for i in range (len(y)):
        list.append(y[i])

    print(list)
    print(len(list))
    list.remove('k')
    print(list)
    list.append('a')
    list.append(3)
    list.append('a')
    list.append(58)
    print(list.count('a'))
    del list[17:27]
    print(list)

def iki(liste):
    """
    Girdi olarak verilen listenin elemanlarini toplayan program fonksiyon
    """
    toplam=0
    for i in range(len(liste)):
        toplam=toplam+liste[i]
    print(toplam)
def karsilastira(list1,list2):
    """
    iki listeyi karsilastirip kac adet farkli elemanlari oldugunu bulan bir kod
    """
    fark=0
    for i in range (len(list2)):
        if list1[i]!=list2[i]:
            fark=fark+1
    print(fark)
def insert(liste,a):
    """
    Kucukten buyuge sirali listeye yeni verilen bir elemani ekleyen fonksiyon

    """
    for i in range (len(liste)):
        if a<= liste[i]:
            liste.insert(i,a)
            break
        elif i== (len(liste)-1):
            liste.append(a)
    print(liste)
def lenListElements(liste):
    """
    Verilen listedeki elemanlarin kac karakterden olustugunu ekrana bastiran fonksiyon

    """
    for i in range (len(liste)):
        print(len(liste[i]))
def karsilastir(list1,list2):
    """
    Verilen 2 listenin elemanlarini karsilastiri ve ilk listenin kac elemaninin buyuk oldugunu ekrana yazdirir
    """
    sonuc=0
    for i in range (len(list1)):
        if list1[i]>list2[i]:
            sonuc=sonuc+1
        elif list2[i]>list1[i]:
            sonuc=sonuc-1
    print(sonuc)
def carpma(liste,sozluk):
    """
    Verilen listedeki elemanlardan sozlukte olanlarin degerlerinin carpimini ekrana yazdirir.
    """
    sonuc=1
    for i in range (len(liste)):
        x=sozluk.get(liste[i],1)
        sonuc=sonuc*x
    print(sonuc)




liste = [1,3,5,7]

sozluk = {1 : 5, 5 : 15 }
carpma(liste,sozluk)