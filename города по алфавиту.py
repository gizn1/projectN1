from bs4 import BeautifulSoup
import requests
# url = 'https://www.travel.ru/hotel/russia/ia/'#ссылка для каждой буквы
# response = requests.get(url)
# soul = BeautifulSoup(response.text,'lxml')
# opuis = soul.find('div',class_='b-destinations row').find_all("a")#дастаем название
# with open('ia.html','w',encoding="utf-8") as h:#создаем папку с каждой буквой
#       h.write(str(opuis))


def a ():
    with open('a.html',encoding='utf-8') as a:
        str = a.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global A
    A = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        A.append(item)#список для сохранений даных
        p += 1

def b ():
    with open('b.html',encoding='utf-8') as b:
        str = b.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')
    p = 0
    global B
    B = []
    for item in opuis:
        x = item.text
        print(p,x)
        B.append(item)
        p += 1


def v ():
    with open('v.html',encoding='utf-8') as v:
        str = v.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#<div class="b-destinations row">
    p = 0
    global V
    V = []
    for item in opuis:
        x = item.text
        print(p,x)
        V.append(item)
        p += 1
def g ():
    with open('g.html',encoding='utf-8') as g:
        str = g.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global G
    G = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        G.append(item)#список для сохранений даных
        p += 1


def d ():
    with open('d.html',encoding='utf-8') as d:
        str = d.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global D
    D = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        D.append(item)#список для сохранений даных
        p += 1


def e ():
    with open('e.html',encoding='utf-8') as e:
        str = e.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global E
    E = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        E.append(item)#список для сохранений даных
        p += 1


def zh ():
    with open('zh.html',encoding='utf-8') as zh:
        str = zh.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global ZH
    ZH = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        ZH.append(item)#список для сохранений даных
        p += 1

def z ():
    with open('z.html',encoding='utf-8') as z:
        str = z.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global Z
    Z = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        Z.append(item)#список для сохранений даных
        p += 1

def i ():
    with open('i.html',encoding='utf-8') as i:
        str = i.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global I
    I = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        I.append(item)#список для сохранений даных
        p += 1

def j ():
    with open('j.html',encoding='utf-8') as j:
        str = j.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global J
    J = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        J.append(item)#список для сохранений даных
        p += 1

def k ():
    with open('k.html',encoding='utf-8') as k:
        str = k.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global K
    K = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        K.append(item)#список для сохранений даных
        p += 1



def l ():
    with open('l.html',encoding='utf-8') as l:
        str = l.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global L
    L = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        L.append(item)#список для сохранений даных
        p += 1

def m ():
    with open('m.html',encoding='utf-8') as m:
        str = m.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global M
    M = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        M.append(item)#список для сохранений даных
        p += 1

def n ():
    with open('n.html',encoding='utf-8') as n:
        str = n.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global N
    N = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        N.append(item)#список для сохранений даных
        p += 1

def o ():
    with open('o.html',encoding='utf-8') as o:
        str = o.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global O
    O = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        O.append(item)#список для сохранений даных
        p += 1


def p ():
    with open('p.html',encoding='utf-8') as p:
        str = p.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global P
    P = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        P.append(item)#список для сохранений даных
        p += 1




def r ():
    with open('r.html',encoding='utf-8') as r:
        str = r.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global R
    R = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        R.append(item)#список для сохранений даных
        p += 1


def s ():
    with open('s.html',encoding='utf-8') as s:
        str = s.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global S
    S = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        S.append(item)#список для сохранений даных
        p += 1

def t ():
    with open('t.html',encoding='utf-8') as t:
        str = t.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global T
    T = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        T.append(item)#список для сохранений даных
        p += 1

def u ():
    with open('u.html',encoding='utf-8') as u:
        str = u.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global U
    U = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        U.append(item)#список для сохранений даных
        p += 1


def f ():
    with open('f.html',encoding='utf-8') as f:
        str = f.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global F
    F = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        F.append(item)#список для сохранений даных
        p += 1


def h ():
    with open('h.html',encoding='utf-8') as h:
        str = h.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global H
    H = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        H.append(item)#список для сохранений даных
        p += 1

def c ():
    with open('c.html',encoding='utf-8') as c:
        str = c.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global C
    C = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        C.append(item)#список для сохранений даных
        p += 1

def ch ():
    with open('ch.html',encoding='utf-8') as ch:
        str = ch.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global CH
    CH = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        CH.append(item)#список для сохранений даных
        p += 1

def sh ():
    with open('sh.html',encoding='utf-8') as sh:
        str = sh.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global SH
    SH = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        SH.append(item)#список для сохранений даных
        p += 1


def sc ():
    with open('sc.html',encoding='utf-8') as sc:
        str = sc.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global SC
    SC = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        SC.append(item)#список для сохранений даных
        p += 1


def y ():
    with open('y.html',encoding='utf-8') as y:
        str = y.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global Y
    Y = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        Y.append(item)#список для сохранений даных
        p += 1


def eh ():
    with open('eh.html',encoding='utf-8') as eh:
        str = eh.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global EH
    EH = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        EH.append(item)#список для сохранений даных
        p += 1

def iu ():
    with open('iu.html',encoding='utf-8') as iu:
        str = iu.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global IU
    IU = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        IU.append(item)#список для сохранений даных
        p += 1

def ia ():
    with open('ia.html',encoding='utf-8') as ia:
        str = ia.read()
    soul = BeautifulSoup(str,'lxml')
    global opuis
    opuis = soul.find_all('a')#дастаем текст с сохраненого документа
    p = 0
    global IA
    IA = []
    for item in opuis:#перебор
        x = item.text
        print(p,x)
        IA.append(item)#список для сохранений даных
        p += 1


i = 0#отслеживание певого раза
while True:
    o = input()
    if o == 'а':
        if i != 1:# вызов функции один раз из за того что добавляютиься удаленые элименты
            a()
            i += 1
            rip = int(input('какой город убрать '))
            del A[rip]



        else:
            p = 0
            for item in A:
                x = item.text
                print(p, x)
                p += 1
            rip = int(input('какой город убрать '))
            if rip > len(A):
                rip -= 1

            if rip < len(A):
                  rip += 1
            del A[rip]

    if o == 'б':
        if i != 1:
            b()
            i += 1
            rip = int(input('какой город убрать '))
            del B[rip]



        else:
            p = 0
            for item in B:
                x = item.text
                print(p, x)
                p += 1
            rip = int(input('какой город убрать '))
            if rip > len(B):
                rip -= 1

            if rip < len(B):
                  rip += 1
            del B[rip]

    if o == 'в':
          if i != 1:
                v()
                i += 1
                rip = int(input('какой город убрать '))
                del V[rip]



          else:
                p = 0
                for item in V:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(V):
                      rip -= 1

                if rip < len(V):
                      rip += 1
                del V[rip]

    if o == 'г':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                g()
                i += 1
                rip = int(input('какой город убрать '))
                del G[rip]



          else:
                p = 0
                for item in G:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(G):
                      rip -= 1

                if rip < len(G):
                      rip += 1
                del G[rip]

    if o == 'д':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                d()
                i += 1
                rip = int(input('какой город убрать '))
                del D[rip]



          else:
                p = 0
                for item in D:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(D):
                      rip -= 1

                if rip < len(D):
                      rip += 1
                del D[rip]



    if o == 'е':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                e()
                i += 1
                rip = int(input('какой город убрать '))
                del E[rip]



          else:
                p = 0
                for item in E:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(E):
                      rip -= 1

                if rip < len(E):
                      rip += 1
                del E[rip]



    if o == 'ж':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                zh()
                i += 1
                rip = int(input('какой город убрать '))
                del ZH[rip]



          else:
                p = 0
                for item in ZH:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(ZH):
                      rip -= 1

                if rip < len(ZH):
                      rip += 1
                del ZH[rip]



    if o == 'з':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                z()
                i += 1
                rip = int(input('какой город убрать '))
                del Z[rip]



          else:
                p = 0
                for item in Z:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(Z):
                      rip -= 1

                if rip < len(Z):
                      rip += 1
                del Z[rip]




    if o == 'и':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                i()
                i += 1
                rip = int(input('какой город убрать '))
                del I[rip]



          else:
                p = 0
                for item in I:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(I):
                      rip -= 1

                if rip < len(I):
                      rip += 1
                del I[rip]




    if o == 'й':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                j()
                i += 1
                rip = int(input('какой город убрать '))
                del J[rip]



          else:
                p = 0
                for item in J:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(J):
                      rip -= 1

                if rip < len(J):
                      rip += 1
                del J[rip]


    if o == 'к':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                k()
                i += 1
                rip = int(input('какой город убрать '))
                del K[rip]



          else:
                p = 0
                for item in K:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(K):
                      rip -= 1

                if rip < len(K):
                      rip += 1
                del K[rip]

    if o == 'л':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                  l()
                  i += 1
                  rip = int(input('какой город убрать '))
                  del L[rip]



          else:
                p = 0
                for item in L:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(L):
                      rip -= 1

                if rip < len(L):
                      rip += 1
                del L[rip]

    if o == 'м':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                m()
                i += 1
                rip = int(input('какой город убрать '))
                del N[rip]



          else:
                p = 0
                for item in N:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(N):
                      rip -= 1

                if rip < len(N):
                      rip += 1
                del N[rip]


    if o == 'о':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                o()
                i += 1
                rip = int(input('какой город убрать '))
                del O[rip]



          else:
                p = 0
                for item in O:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(O):
                      rip -= 1

                if rip < len(O):
                      rip += 1
                del O[rip]


    if o == 'с':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                s()
                i += 1
                rip = int(input('какой город убрать '))
                del S[rip]



          else:
                p = 0
                for item in S:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(S):
                      rip -= 1

                if rip < len(S):
                      rip += 1
                del S[rip]


    if o == 'т':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                t()
                i += 1
                rip = int(input('какой город убрать '))
                del T[rip]



          else:
                p = 0
                for item in T:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(T):
                      rip -= 1

                if rip < len(T):
                      rip += 1
                del T[rip]

    if o == 'у':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                u()
                i += 1
                rip = int(input('какой город убрать '))
                del U[rip]



          else:
                p = 0
                for item in U:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(U):
                      rip -= 1

                if rip < len(U):
                      rip += 1
                del U[rip]

    if o == 'ф':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                f()
                i += 1
                rip = int(input('какой город убрать '))
                del F[rip]



          else:
                p = 0
                for item in F:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(F):
                      rip -= 1

                if rip < len(F):
                      rip += 1
                del F[rip]


    if o == 'х':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                h()
                i += 1
                rip = int(input('какой город убрать '))
                del H[rip]



          else:
                p = 0
                for item in H:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(H):
                      rip -= 1

                if rip < len(H):
                      rip += 1
                del H[rip]



    if o == 'ц':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                c()
                i += 1
                rip = int(input('какой город убрать '))
                del C[rip]



          else:
                p = 0
                for item in C:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(C):
                      rip -= 1

                if rip < len(C):
                      rip += 1
                del C[rip]



    if o == 'ч':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                ch()
                i += 1
                rip = int(input('какой город убрать '))
                del CH[rip]



          else:
                p = 0
                for item in CH:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(CH):
                      rip -= 1

                if rip < len(CH):
                      rip += 1
                del CH[rip]


    if o == 'ш':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                sh()
                i += 1
                rip = int(input('какой город убрать '))
                del SH[rip]



          else:
                p = 0
                for item in SH:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(SH):
                      rip -= 1

                if rip < len(SH):
                      rip += 1
                del SH[rip]


    if o == 'щ':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                sc()
                i += 1
                rip = int(input('какой город убрать '))
                del SC[rip]



          else:
                p = 0
                for item in SC:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(SC):
                      rip -= 1

                if rip < len(SC):
                      rip += 1
                del SC[rip]



    if o == 'ы':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                y()
                i += 1
                rip = int(input('какой город убрать '))
                del Y[rip]



          else:
                p = 0
                for item in Y:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(Y):
                      rip -= 1

                if rip < len(Y):
                      rip += 1
                del Y[rip]



    if o == 'э':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                eh()
                i += 1
                rip = int(input('какой город убрать '))
                del EH[rip]



          else:
                p = 0
                for item in EH:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(EH):
                      rip -= 1

                if rip < len(EH):
                      rip += 1
                del EH[rip]



    if o == 'ю':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                iu()
                i += 1
                rip = int(input('какой город убрать '))
                del IU[rip]



          else:
                p = 0
                for item in IU:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(IU):
                      rip -= 1

                if rip < len(IU):
                      rip += 1
                del IU[rip]


    if o == 'я':
          if i != 1:  # вызов функции один раз из за того что добавляютиься удаленые элименты
                ia()
                i += 1
                rip = int(input('какой город убрать '))
                del IA[rip]



          else:
                p = 0
                for item in IA:
                      x = item.text
                      print(p, x)
                      p += 1
                rip = int(input('какой город убрать '))
                if rip > len(IA):
                      rip -= 1

                if rip < len(IU):
                      rip += 1
                del IA[rip]


    if o ==  ' ' :
            print('victory')



