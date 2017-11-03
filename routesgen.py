

#tuple = Router1, Router2, Suffixe1, Suffixe2, ASN1, ASN2, Poids, Relation R1->R2

combinaisons = [
    ("2.1.0.1", "2.0.0.1", "2.1.0.0/24", "2.0.0.0/8", "1", "2", "2", "0"),
    ("2.1.0.1", "2.0.0.2", "2.1.0.0/24", "2.0.0.0/8", "1", "2", "2", "0"),
    ("2.1.0.1", "2.0.0.3", "2.1.0.0/24", "2.0.0.0/8", "1", "2", "8", "0")
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

print route(0);
print links();