from pysnmp.hlapi import *

def batteryLevel(user, authKey_sai, priveKey_sai, host, oid):
    level = ''
    iterator = getCmd(
        SnmpEngine(),
        UsmUserData(user, authKey=authKey_sai, privKey=priveKey_sai),
        UdpTransportTarget((host, 161)),
        ContextData(),
        # ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
        ObjectType(ObjectIdentity(oid))
    )
 
    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
 
    if errorIndication:
        print(errorIndication)
 
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(), errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
 
    else:
        for varBind in varBinds:
            code = str(varBind[0].prettyPrint())
            level = int(varBind[1])
            print('Tiempo restante de batería: ' + str(level) + ' Minutos')
            print('Codigo de MIB: ' + str(code))
 
    return level
