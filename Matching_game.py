#spades="\u2660",heart="\u2665",clubs="\u2663",diamonds="\u2666"
import random
ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
suites =["\u2660" ,"\u2665","\u2663","\u2666"]
print('Καλωσορίσατε στο παιχνίδι μας!!!')
f=True
x=input("Παρακαλώ συμπληρώστε τον αριθμο παικτων:")
while f==True:
    while x.isnumeric()==False: #Ελεγχω αρχικα αν ειναι νουμερο το input και επειτα αν ειναι μεγαλυτερο του 2
        x=input("Δωθηκε δεδόμενο που δεν αποτελεί αριθμό.Συμπληρώστε ξανα:")
    if int(x)>=2: #Αν δωθουν παικτες παραπανω απο 2 τοτε τελειωνει η επαναληψη
        f=False
    else:
        x=input("Δωθηκε αριθμος παικτων μικρότερος του 2.Συμπληρώστε ξανα:")
y=input("Βαθμός δυσκολίας(Από το 1 εως το 3):")
while y!='1' and y!='2' and y!='3':
    y=input("Ο συγκεκριμένος βαθμος δυσκολίας δεν υπαρχει.Συμπληρώστε ξανα:")
bonus1=input("Κλασικό παιχνίδι ή παιχνίδι με επιπλέον πόντους απο σειρές(1 ή 2):")
while bonus1!="1" and bonus1!="2":
    bonus1=input("Λάθος δεδομένο.Κλασικό παιχνίδι ή παιχνίδι με επιπλέον πόντους απο σειρές(1 ή 2):")
def deckA(x,y,ranks,suites): #συναρτηση που επιστρεφει λιστα με τα διαθεσιμα χαρτια για καθε επιπεδο
    DeckofCards = []  # H λίστα που θα κρατάει τα  χαρτια
    # Χρησιμοποιώ τους βρόχους για να γεμίσω την λίστα
    for i in range (0,4) :
        for j in range (x,y) :
            DeckofCards=DeckofCards+[ranks[j]+suites[i]]
    return DeckofCards
def krummenh_lista(x): #συναρτηση που επιστρεφει λιστα με 'κλειστα' τραπουλοχαρτα
    llist=[]    
    for i in range (1,5):
        sublist=[["X"]*x]
        llist=llist+sublist
    return llist #λιστα με φυλλα που δεν εχουν ανοιξει
if y=='1':
    DeckofCards=deckA(9,13,ranks,suites)
    llist=krummenh_lista(4)
elif y=='2':
    DeckofCards=deckA(0,10,ranks,suites)
    llist=krummenh_lista(10)
else:
    DeckofCards=deckA(0,13,ranks,suites)
    llist=krummenh_lista(13)
random.shuffle(DeckofCards)#ανακατεύω την τράπουλα
#Βρισκω το μεγεθος του deck ετσι ωστε να δημιουργησω πινακα χωρις να ψαχνω σε ποιο επιπεδο παιζω
i=len(DeckofCards) 
sthles=i//4
deck=[]
sublist=[]
for i in range (1,5):
    for j in range (0,sthles):
        sublist=sublist+[DeckofCards[0]]
        DeckofCards.pop(0)
    deck=deck+[sublist]
    sublist=[]
#συναρτηση που εκτυπωνει λιστα σε μορφη πινακα
def pinakas(sthles,deck): 
    for i in range (0,sthles+1):
        if i==0:
            print(" ",end='   ')
        elif i<10:
            print(i,end='   ')
        else:
            print(i,end="  ")
    print('')
    for i in range (0,4):
        for j in range (-1,sthles):
            if j==-1:
                print(i+1,end="   ")
            elif len(deck[i][j])==3:
                print(deck[i][j],end=' ')
            elif len(deck[i][j])==2:
                print(deck[i][j],end='  ')
            else:
                print(deck[i][j],end='   ')
        print('')
pinakas(sthles,deck)
#(BONUS1)Συναρτηση που ελεγχει αν δυο χαρτια ανηκουν στην ιδια σειρα(BONUS1)
def bonus(a,b,kartes,bonus1,flag=True):
    if kartes[a][1]=="0":
        kartes[a]=kartes[a].replace('0','')
    elif kartes[b][1]=='0':
        kartes[b]=kartes[b].replace('0','')
    if kartes[a][1]==kartes[b][1] and bonus1=='2':
        if kartes[a][0]=="Q" or kartes[a][0]=="J" or kartes[a][0]=="K" or kartes[a][0]=="1" :
            points[n]=points[n]+10
        elif kartes[a][0]=='A':
            points[n]=points[n]+1
        else:
            points[n]=points[n]+int(kartes[a][0])
        if kartes[b][0]=="Q" or kartes[b][0]=="J" or kartes[b][0]=="K" or kartes[b][0]=='1':
            points[n]=points[n]+10
        elif kartes[b][0]=='A':
            points[n]=points[n]+1
        else:
            points[n]=points[n]+int(kartes[b][0])
        if flag==True:  
            print("Tαίριασμα σειράς.Παίκτη",n,"κερδίζεις σε πόντους το αρθροισμα των χαρτιών!")
    return points[n]
#Συναρτηση που ελεγχει την καρτα αμα ειναι εγκυρος ο συνδυασμος και αμα υπαρχει στον πινακα
def elegxos(sthles,n,ar_kartas):
    def valerror():#Αποφευγω το ValueError σε περιπτωση που ο χρηστης δεν δωσει δεδομενα μορφης '1 2'
        while True:
            try:
                grammh,sthlh=input("Παίκτη "+str(n)+": Δώσε γραμμή και στήλη "+str(ar_kartas)+" κάρτας (πχ 1 10):").split()
            except ValueError:
                print("Δώθηκε δεδομένο που δεν είναι σύμφωνο με τις οδηγίες.")
                #Πισω στην αρχη της επαναληψης
                continue
            else:
                #Δωθηκε σωστο δεδομενο!
                #Βγαινουμε απο την επαναληψη.
                break
        return grammh,sthlh
    f=True
    grammh,sthlh=valerror()
    while f==True:
        while grammh.isnumeric()==False or sthlh.isnumeric()==False: #Ελεγχω αρχικα αν ειναι νουμερο το input και επειτα αν ειναι μεγαλυτερο του 2
            print("Δωθηκε δεδόμενο που δεν αποτελεί αριθμό.")
            grammh,sthlh=valerror()
        if (int(grammh)>=1 and int(grammh)<=4) and (int(sthlh)>=1 and int(sthlh)<=sthles): #Αν δωθουν παικτες παραπανω απο 2 τοτε τελειωνει η επαναληψη
            f=False
        else:
            print("Δωθηκε συνδυασμός εκτός των ορίων του πίνακα.")
            grammh,sthlh=valerror()
    return grammh,sthlh
points=[0]+[0]*int(x)
flag=True
while flag==True:
    n=1
    while n<=int(x):
        kartes=[]
        mhtairiasma=[]#Σε αυτον αποθηκευω τις συντεταγμενες σε περιπτωση που δεν ταιριαζουν τα φυλλα
        grammh,sthlh=elegxos(sthles,n,"Πρώτης")
        grammh,sthlh=int(grammh)-1,int(sthlh)-1
        while llist[grammh][sthlh]!="X": #Ελέγχω αν η κάρτα είναι ήδη ανοιχτή(Καρτα 1)
            print("Παίκτη",n,",δυστυχώς η καρτα αυτή είναι ηδη ανοιχτή.")
            grammh,sthlh=elegxos(sthles,n,"Πρώτης")
            grammh,sthlh=int(grammh)-1,int(sthlh)-1
        llist[grammh][sthlh]=deck[grammh][sthlh]
        mhtairiasma=mhtairiasma+[grammh]+[sthlh]
        kartes=kartes+[deck[grammh][sthlh]]
        pinakas(sthles,llist)
        grammh,sthlh=elegxos(sthles,n,"Δεύτερης")
        grammh,sthlh=int(grammh)-1,int(sthlh)-1
        while llist[grammh][sthlh]!="X": #Ελέγχω αν η κάρτα είναι ήδη ανοιχτή(Καρτα 2)
            print("Παίκτη",n,",δυστυχώς η καρτα αυτή είναι ηδη ανοιχτή.")
            grammh,sthlh=elegxos(sthles,n,"Δεύτερης")
            grammh,sthlh=int(grammh)-1,int(sthlh)-1
        llist[grammh][sthlh]=deck[grammh][sthlh]
        mhtairiasma=mhtairiasma+[grammh]+[sthlh]
        kartes=kartes+[deck[grammh][sthlh]]
        pinakas(sthles,llist)
        if kartes[0][0]=='J' and 'J'==kartes[1][0]:
            p=10
            points[n]=points[n]+p
            print("+"+str(p)+" "+"Επιτυχές ταίριασμα παικτη",n,".Έχεις συνολικά",points[n],"πόντους και Ξαναπαίζεις!")
            n=n
        elif kartes[0][0]=='K' and 'K'==kartes[1][0]:
            p=10
            points[n]=points[n]+p
            print("+"+str(p)+" "+"Επιτυχές ταίριασμα παικτη",n,".Έχεις συνολικά",points[n],"πόντους και ο επομενος παικτης χανει την σειρα του!")
            n=n+2
        elif kartes[0][0]=='Q' and 'Q'==kartes[1][0]:
            p=10
            points[n]=points[n]+p
            print("+"+str(p)+" "+"Επιτυχές ταίριασμα παικτη",n,".Έχεις συνολικά",points[n],"πόντους!")
            n=n+1
        elif kartes[0][0]==kartes[1][0]:
            if kartes[0][0]=="1" :
                p=10
                points[n]=points[n]+p
            elif kartes[0][0]=="A" :
                p=1
                points[n]=points[n]+p
            else: 
                p=int(kartes[0][0])
                points[n]=points[n]+p
            print("+"+str(p)+" "+"Επιτυχές ταίριασμα παικτη",n,".Έχεις συνολικά",points[n],"πόντους!")
            n=n+1
        elif (kartes[0][0]=='Q' and 'K'==kartes[1][0]) or (kartes[0][0]=='K' and 'Q'==kartes[1][0]):
            print('Δικαιωμα για τρίτη κάρτα')
            grammh,sthlh=elegxos(sthles,n,"Τρίτης")
            grammh,sthlh=int(grammh)-1,int(sthlh)-1
            while llist[grammh][sthlh]!="X": #Ελέγχω αν η κάρτα είναι ήδη ανοιχτή(Καρτα 3)
                print("Παίκτη",n,",δυστυχώς η καρτα αυτή είναι ηδη ανοιχτή.")
                grammh,sthlh=elegxos(sthles,n,"Τρίτης")
                grammh,sthlh=int(grammh)-1,int(sthlh)-1
            llist[grammh][sthlh]=deck[grammh][sthlh]
            kartes=kartes+[deck[grammh][sthlh]]
            pinakas(sthles,llist)
            if kartes[0][0]==kartes[1][0]:
                points[n]=bonus(0,2,kartes,bonus1)
                points[n]=bonus(1,2,kartes,bonus1)
                llist[grammh][sthlh]='X'
                p=10
                points[n]=points[n]+p
                print("+"+str(p)+" "+"Επιτυχές ταίριασμα παικτη",n,".Έχεις συνολικά",points[n],"πόντους!")
                pinakas(sthles,llist)
            elif kartes[1][0]==kartes[2][0]:
                points[n]=bonus(0,2,kartes,bonus1)
                points[n]=bonus(0,1,kartes,bonus1)
                llist[mhtairiasma[0]][mhtairiasma[1]]="X"
                p=10
                points[n]=points[n]+p
                print("+"+str(p)+" "+"Επιτυχές ταίριασμα παικτη",n,".Έχεις συνολικά",points[n],"πόντους!")
                pinakas(sthles,llist)
            elif kartes[0][0]==kartes[2][0]:
                points[n]=bonus(0,2,kartes,bonus1)
                points[n]=bonus(1,2,kartes,bonus1)
                llist[mhtairiasma[2]][mhtairiasma[3]]="X"
                p=10
                points[n]=points[n]+p
                print("+"+str(p)+" "+"Επιτυχές ταίριασμα παικτη",n,".Έχεις συνολικά",points[n],"πόντους!")
                pinakas(sthles,llist)
            else:
                k=points[n]
                s=k
                i=0
                points[n]=bonus(0,1,kartes,bonus1,False)
                if points[n]>s:
                    i=1
                s=points[n]
                points[n]=bonus(1,2,kartes,bonus1,False)
                if points[n]>s:
                    i+=1
                s=points[n]
                points[n]=bonus(0,2,kartes,bonus1,False)
                if points[n]>s:
                    i+=1
                if i==3:
                    s=points[n]
                    points[n]=points[n]-(s-k)//2
                if i>=1:
                    print("Tαίριασμα σειράς.Παίκτη",n,"κερδίζεις σε πόντους το αρθροισμα των χαρτιών!")
                print("Μη επιτυχές ταίριασμα συμβόλου.Οι κάρτες κλείνουν!Έχεις συνολικά",points[n],"πόντους!")
                llist[grammh][sthlh]='X'
                llist[mhtairiasma[0]][mhtairiasma[1]]="X"
                llist[mhtairiasma[2]][mhtairiasma[3]]="X"
                pinakas(sthles,llist)
            n=n+1
        else:
            points[n]=bonus(0,1,kartes,bonus1)
            print("Μη επιτυχές ταίριασμα συμβόλου.Οι κάρτες κλείνουν!Έχεις συνολικά",points[n],"πόντους!")
            llist[mhtairiasma[0]][mhtairiasma[1]]="X"
            llist[mhtairiasma[2]][mhtairiasma[3]]="X"
            pinakas(sthles,llist)
            n=n+1
        f=True
        for i in range (0,4): #Ελέγχω αν η κρυφη λιστα εχει αλλα κλειστα φυλλα.Αν οχι τερματιζει το παιχνιδι.
            for j in range (0,sthles):
                if llist[i][j]=='X':
                    f=False
        if f==True:
            n=int(x)+1
            flag=False
print('Game Over')
print("Νικητής ο παίκτης",points.index(max(points)),'με',max(points),"πόντους!")






        
        
        





        
   


