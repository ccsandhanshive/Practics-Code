def address(input1):
    if input1[0] is 'h':
        if 'http' in input1:
            protocolSeparator=input1.split("http")
            protocolSeparator[0]='http'
            if 'ru' in protocolSeparator[1]:
                protocolSeparator[1]=protocolSeparator[1].split("ru")
        else:
            protocolSeparator=input1.split("https")
            protocolSeparator[0]='https'
            if 'ru' in protocolSeparator[1]:
                protocolSeparator[1]=protocolSeparator[1].split("ru")
    elif input1[0] is 'f':
        if 'ftp' in input1:
                protocolSeparator=input1.split("ftp")
                protocolSeparator[0]='ftp'
                if 'ru' in protocolSeparator[1]:
                    protocolSeparator[1]=protocolSeparator[1].split("ru")
    return protocolSeparator[0]+"://"+protocolSeparator[1][0]+".ru/"+protocolSeparator[1][1]
        
        
url="httpsonrux"
url1="ftphttprurxrxrx"
url2="httpsmazicrudon"
print(address(url))
print(address(url1))
print(address(url2))
