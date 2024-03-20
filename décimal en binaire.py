
ip = input('Veuillez écrire votre adresse ip').split(".")

print(ip)


print(type(ip[0]))


octet1 = '{:08b}'.format(int(ip[0]))

octet2 = '{:08b}'.format(int(ip[1]))

octet3 = '{:08b}'.format(int(ip[2]))

octet4 = '{:08b}'.format(int(ip[3]))


print(int(ip[0]),'.',int(ip[1]),'.',int(ip[2]),'.',int(ip[3]),'.',int(ip[3]))


print(str(octet1),'.',str(octet2),'.',str(octet3),'.',str(octet4))


if int(ip[0]) <= 126:
    print('C''est une classe A')

elif int(ip[0]) <= 191:
    print('C''est une classe B')

elif int(ip[0]) <= 223:
    print('C''est une classe C')

elif int(ip[0]) <= 239:
    print('C''est une classe D')


