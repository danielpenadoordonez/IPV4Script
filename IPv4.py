from IPExceptions import InvalidIpFormat, InvalidIpRange
from time import sleep

def valida_IP(ip):
    'Validaciones para IP ingresada'
    #Valida que solo hayan digitos en cada octeto
    def isAllDigits(octet):
        if not octet.isdigit():
            raise InvalidIpFormat

    #Valida que cada octeto este en el rango correcto
    def isInRange(octet):
        octet = int(octet)
        if octet < 0 or octet > 255:
            raise InvalidIpRange
    
    #Valida que el formato este correto con un punto entre cada octeto
    def isFormatValid():
        dots = 0
        for char in '.'.join(ip):
            if char == '.':
                dots += 1
        if dots != 3:
            raise InvalidIpFormat
    
    list(map(isAllDigits, ip))
    list(map(isInRange, ip))
    isFormatValid()

def get_Ip_Class(ip):
    #Se extrae el primer octeto de la IP para ver a que clase pertenece
    firstOctet = int(ip[0])
    if firstOctet <= 127:
        return "Clase A"
    elif firstOctet <= 191:
        return "Clase B"
    elif firstOctet <= 223:
        return "Clase C"
    elif firstOctet <= 239:
        return "Clase D"
    elif firstOctet <= 255:
        return "Clase E"
    return None

def get_Ip_Type(ip):
    #Se pasan todos los octetos de string a int por medio de una funcion lambda y la funcion map()
    ip = list(map(lambda octet : int(octet), ip))
    if ip[0] == 10:
        return "IP Privada"
    if ip[0] == 172 and ip[1] == 16 or ip[0] == 172 and ip[1] == 31:
        return "IP Privada"
    if ip[0] == 192 and ip[1] == 168:
        return "IP Privada"
    return "IP Publica"

invalidIp = True
while invalidIp:
    try:
        IP_ADDRESS = input("Ingrese una direccion IP: ")
        IP_ADDRESS = IP_ADDRESS.split('.')
        valida_IP(IP_ADDRESS)
        invalidIp = False
    except KeyboardInterrupt:
        exit()
    except InvalidIpRange:
        print("IP Invalida: Cada Octeto debe estar entre 0 y 255")
        sleep(1)
    except InvalidIpFormat:
        print("IP Invalida: Error de Formato, son 4 octetos con digitos separados por punto(.)")
        sleep(1)


print(
f"""
----------------------------------------------
|                   |                        |
| {get_Ip_Class(IP_ADDRESS)}           |      {get_Ip_Type(IP_ADDRESS)}        |
|                   |                        |
----------------------------------------------
"""
)
