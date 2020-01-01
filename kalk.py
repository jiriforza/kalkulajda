print('* - násobení\n+ - sčítání')

vstup = str(input('-> '))


while(vstup !='0'):




    def split(word): 
        return [char for char in word] 
        
    word=vstup
    A=(split(word))
    I = 0
    K = 0
    HH = 0
    Bs = ''
    Cs = ''
    Blen = 0
    Clen = 0
    vys = 0
    delka = len(A)

    B = [None] * delka
    C = [None] * delka

    if '*' in vstup:
        while(I<delka):
            if A[I]=='*':
                print('našel jsem hvězdu')
                while(K<I):
                    B[K]=A[K]
                    K = K + 1
                print(B)
                HH = I + 1
                K = 0
                while(HH<(delka)):
                    C[K]=A[HH]
                    K = K + 1
                    HH = HH + 1
                print(C)
            I = I + 1
        O = 1
        while(O!=0):
            if B[Blen] == None:
                O = 0
            Blen = Blen + 1
        Blen = Blen - 1 
        print(Blen)

        O = 1
        while(O!=0):
            if C[Clen] == None:
                O = 0
            Clen = Clen + 1
        Clen = Clen - 1 
        print(Clen)

        I=0

        while(I<Blen):
            Bs = Bs + B[I]
            I = I + 1
        #print(Bs)
        Bs = int(Bs)
        print(Bs)

        I=0

        while(I<Clen):
            Cs = Cs + C[I]
            I = I + 1
        #print(Cs)
        Cs = int(Cs)
        print(Cs)

        vys = (Bs*Cs)
        print('Výsledek je ',vys)
        
        


    if '+' in vstup:
        while(I<delka):
            if A[I]=='+':
                print('našel jsem plus')
                while(K<I):
                    B[K]=A[K]
                    K = K + 1
                print(B)
                HH = I + 1
                K = 0
                while(HH<(delka)):
                    C[K]=A[HH]
                    K = K + 1
                    HH = HH + 1
                print(C)
            I = I + 1
        O = 1
        while(O!=0):
            if B[Blen] == None:
                O = 0
            Blen = Blen + 1
        Blen = Blen - 1 
        print(Blen)

        O = 1
        while(O!=0):
            if C[Clen] == None:
                O = 0
            Clen = Clen + 1
        Clen = Clen - 1 
        print(Clen)

        I=0

        while(I<Blen):
            Bs = Bs + B[I]
            I = I + 1
        #print(Bs)
        Bs = int(Bs)
        print(Bs)

        I=0

        while(I<Clen):
            Cs = Cs + C[I]
            I = I + 1
        #print(Cs)
        Cs = int(Cs)
        print(Cs)

        vys = (Bs+Cs)
        print('Výsledek je ',vys)
    vstup = str(input('-> '))