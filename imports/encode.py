import math


def affine_cypher(akey=int,bkey=int,usr_msg=str):
    alphabet={
        0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",
        13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}
    if akey not in [1,3,5,7,9,11,15,17,19,21,13,25]:
        return "Err Key Length Invalid"
    cypher = {}
    for i,letter in enumerate(alphabet.values()):
        x=(akey*i+bkey)%26
        cypher[letter] = x
    alphabet[" "]= " "
    cypher[" "]=" "
    returnmsg = [] 
    usr_msg=usr_msg.lower()
    for i, letter in enumerate(usr_msg):
        returnmsg.append(alphabet[cypher[letter]])
    return "".join(returnmsg)

def transposition_cypher(columns = int,key=str,usr_msg=str):
    alphabet={
        "a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7,"i":8,"j":9,"k":10,"l":11,"m":12,
        "n":13,"o":14,"p":15,"q":16,"r":17,"s":18,"t":19,"u":20,"v":21,"w":22,"x":23,"y":24,"z":25}
    n=0
    order=[]
    while n<columns:
        order.append(alphabet[key[n]]+1)
        n=n+1
    temporder=order[:]
    ordering=order[:]
    temporder.sort()
    n=0
    index=0 
    for i in temporder:
        index=order.index(i)
        order[index]=""
        ordering[index] = n 
        n+=1     
    m=0
    placeholder=[0]*columns
    rows = math.ceil(len(usr_msg)/columns)
    matrix = []
    msglist=[letter for letter in usr_msg]
    while len(msglist)%columns !=0:
        msglist.append(" ")
    returnmsg=[]
    for i in range(columns):
        for j in range(rows):
            returnmsg.append(msglist[columns*j+ordering[i]])
    return ''.join(returnmsg)

def vigenere_cypher(key1,usr_msg):
    keylist = []
    for letter in key1:
        if letter == " ":
            continue
        keylist.append(letter)
    num2alpha={
        0:"a",1:"b",2:"c",3:"d",4:"e",5:"f",6:"g",7:"h",8:"i",9:"j",10:"k",11:"l",12:"m",
        13:"n",14:"o",15:"p",16:"q",17:"r",18:"s",19:"t",20:"u",21:"v",22:"w",23:"x",24:"y",25:"z"}
    alpha2num={num2alpha[index]:index for index in num2alpha}
    shiftlist = [alpha2num[i] for i in keylist]
    return_msg = []
    for i,letter in enumerate(usr_msg):
        x = (alpha2num[letter]+shiftlist[i%len(shiftlist)])%26
        return_msg.append(num2alpha[x])
    return ''.join(return_msg)
