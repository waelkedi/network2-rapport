

#tuple = Router1, Router2, Suffixe1, Suffixe2, ASN1, ASN2, Poids, Relation R1->R2

#BigCarrier 1 1.0.0.0/8
#Spring 2 2.0.0.0/8
#iCompany 200 2.1/16
#Abilene 11537 3.0.0.0/24
#GEANT 20965 4.0.0.0/24
#BELNET 2611 4.1.0.0/24 et 1.1.0.0/24
#CERN 201 4.200.0.0/16 et 3.200.0.0/16
#UCLA 52 3.1.0.0/16 et 2.2.1.0/24
#UCL 65535 130.104.0.0/16
#ULg 65534 139.165.0.0/16


combinaisons = [
    #iCompany and Spring
    ("2.1.0.1", "2.0.0.1", "2.1/16", "2.0.0.0/8", "200", "2", "2", "0"),
    ("2.1.0.1", "2.0.0.2", "2.1/16", "2.0.0.0/8", "200", "2", "2", "0"),
    ("2.1.0.1", "2.0.0.3", "2.1/16", "2.0.0.0/8", "200", "2", "8", "0"),

    #Spring and BigCarrier
    ("2.0.0.1", "1.0.0.1", "2.0.0.0/8", "1.0.0.0/8", "2", "1", "65", "1"),
    ("2.0.0.2", "1.0.0.2", "2.0.0.0/8", "1.0.0.0/8", "2", "1", "70", "1"),
    ("2.0.0.3", "1.0.0.3", "2.0.0.0/8", "1.0.0.0/8", "2", "1", "70", "1"),
    ("2.0.0.4", "1.0.0.4", "2.0.0.0/8", "1.0.0.0/8", "2", "1", "75", "1"),

    #Spring and Abilene
    ("2.0.0.3", "3.0.0.1", "2.0.0.0/8", "3.0.0.0/24", "2", "11537", "1", "2"),
    
    #Spring and UCLA
    ("2.0.0.3", "3.1.0.1", "2.0.0.0/8", "3.1.0.0/16", "2", "52", "1", "2"), #red
    
    #Abilene and UCLA
    ("3.0.0.2", "3.1.0.1", "3.0.0.0/24", "3.1.0.0/16", "11537", "52", "1", "2"), #red
    ("3.0.0.2", "3.1.0.2", "3.0.0.0/24", "3.1.0.0/16", "11537", "52", "1", "2"), #red

    #BigCarrier and GEANT
    ("1.0.0.1", "4.0.0.2", "1.0.0.0/8", "4.0.0.0/16", "1", "20965", "1", "2"),
    ("1.0.0.2", "4.0.0.1", "1.0.0.0/8", "4.0.0.0/16", "1", "20965", "1", "2"),
    ("1.0.0.3", "4.0.0.1", "1.0.0.0/8", "4.0.0.0/16", "1", "20965", "1", "2"),

    #BigCarrier and BELNET
    ("1.0.0.2", "1.1.0.2", "1.0.0.0/8", "1.1.0.0/24", "1", "2611", "1", "2"),#red

    #Abiene and GEANT
    ("3.0.0.1", "4.0.0.1", "3.0.0.0/24", "4.0.0.0/24", "11537", "20965", "60", "1"),
    ("3.0.0.3", "4.0.0.3", "3.0.0.0/24", "4.0.0.0/24", "11537", "20965", "50", "1"),

    #Abilene and CERN
    ("3.0.0.3", "4.200.0.1", "3.0.0.0/24", "4.200.0.0/16", "11537", "201", "55", "2"),#red

    #GEANT and CERN
    ("4.0.0.3", "4.200.0.1", "4.0.0.0/24", "4.200.0.0/16", "20965", "201", "5", "2"),#red

    #GEANT and BELNET
    ("4.0.0.3", "1.1.0.1", "4.0.0.0/24", "1.1.0.0/24", "20965", "2611", "5", "2"),#red
    ("4.0.0.4", "1.1.0.2", "4.0.0.0/24", "1.1.0.0/24", "20965", "2611", "5", "2"),#red

    #BELNET and UCL
    ("1.1.0.1", "130.104.0.1", "1.1.0.0/24", "130.104.0.0/16", "2611", "65535", "1", "2"),
    ("1.1.0.2", "130.104.0.2", "1.1.0.0/24", "130.104.0.0/16", "2611", "65535", "1", "2"),

    #BELNET and ULg
    ("1.1.0.1", "139.165.0.1", "1.1.0.0/24", "139.165.0.0/16", "2611", "65534", "1", "2"),
    ("1.1.0.2", "139.165.0.2", "1.1.0.0/24", "139.165.0.0/16", "2611", "65534", "1", "2")
    

]


def link(i):
    s = ""
    s += "net add link " + combinaisons[i][0] + " " + combinaisons[i][1] + "\n"
    return s

def links():
    s =""
    for i in range(combinaisons.__len__()):
        s+=link(i)
    return s

def route(i):
    s=""
    s =s + "net node " + combinaisons[i][0] + " route add --oif=" + combinaisons[i][1] + " " + combinaisons[i][3] + " " + combinaisons[i][6] + "\n"
    s =s + "net node " + combinaisons[i][1] + " route add --oif=" + combinaisons[i][0] + " " + combinaisons[i][2] + " " + combinaisons[i][6] + "\n"
    return s

def routes():
    s=""
    for i in range(combinaisons.__len__()):
        s+=route(i)
    return s

def peering(i):
    s=""
    s+= "bgp router " + combinaisons[i][0]+ "\n"
    s+= "    add peer " + combinaisons[i][5] + " " + combinaisons[i][1] + "\n"
    s+= "    peer " + combinaisons[i][1] + " up\n"
    s+= "    exit\n"
    s+= "bgp router " + combinaisons[i][1]+ "\n"
    s+= "    add peer " + combinaisons[i][4] + " " + combinaisons[i][0] + "\n"
    s+= "    peer " + combinaisons[i][0] + " up\n"
    s+= "    exit\n"
    return s

def peerings():
    s=""
    for i in range(combinaisons.__len__()):
        s+=peering(i)
    return s

def genRoutes():
    s = links() + "\n" + routes() + "\n" + peerings() + "\n"
    return s


if __name__ == '__main__':
  f = open('routes.cbgp', 'w')
  f.write("print 'Running routes.cbgp\\n'\n\n")
  content = genRoutes()
  f.write(content)
  f.write("print 'END\\n'\n")
  f.close()
