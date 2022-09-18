def numeros_bcd(numero):
    bcd = {
        "0":"0000",
        "1":"0001",
        "2":"0010",
        "3":"0011",
        "4":"0100",
        "5":"0101",
        "6":"0110",
        "7":"0111",
        "8":"1000",
        "9":"1001",
        "A":"1010",
        "B":"1011",
        "C":"1100",
        "D":"1101",
        "E":"1110",
        "F":"1111"
        }
    return (bcd.get(numero, "número no es válido"))  
def numeros_hex(numero):
    bcd = {
        "0000":"0",
        "0001":"1",
        "0010":"2",
        "0011":"3",
        "0100":"4",
        "0101":"5",
        "0110":"6",
        "0111":"7",
        "1000":"8",
        "1001":"9",
        "1010":"A",
        "1011":"B",
        "1100":"C",
        "1101":"D",
        "1110":"E",
        "1111":"F"
        }
    return (bcd.get(numero, "número no es válido")) 
def desplazamiento(instruccion):
    numero=list(numeros_bcd(RegA[2])+numeros_bcd(RegA[3]))
    x=instruccion[6]
    if (instruccion[4] == "<"):
        for s in range(int(x)):
            numero.append("0") 
        for i in range(len(numero)):
            if i<=7:
                numero[i]=numero[i+int(x)]
        for s in range(int(x)):
            numero.pop()
    if (instruccion[4] == ">"):
        for s in range(int(x)):
            numero.insert(0,"0")
        numero=list(reversed(numero))   
        for i in range(len(numero)):
            if i<=7:
                numero[i]=numero[i+int(x)]
        for s in range(int(x)):
            numero.pop()
        numero=list(reversed(numero)) 
    num="".join(numero[:4])
    num2="".join(numero[4:])
    return numeros_hex(num)+numeros_hex(num2)

def rotacion(instruccion):
    numero=list(numeros_bcd(RegA[2])+numeros_bcd(RegA[3]))
    x=int(instruccion[9])
    if (instruccion[7] == "R"):
        for s in range(1,x+1):
                numero.insert(0,numero[-s])
        num="".join(numero[:4])
        num2="".join(numero[4:8])         
    if (instruccion[7] == "L"):
        for s in range(x):
                numero.append(numero[s])
        num="".join(numero[x:x+4])
        num2="".join(numero[x+4:])
    return numeros_hex(num)+numeros_hex(num2)   
#if __main__=="main":
RegA="0xBC"

# instruccion="RegA<<3"
instruccion="RegA>>3"
print(desplazamiento(instruccion))

# instruccionRotar="A RotarL 2"
# instruccionRotar="A RotarR 3"
# print(rotacion(instruccionRotar))  