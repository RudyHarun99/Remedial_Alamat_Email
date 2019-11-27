x = input('Input email: ')
def tes(x):
    x = x.replace('@', ' ')
    x = x.replace('.', ' ')
    xPisah = x.split(' ')

    if len(xPisah) != 3: 
        return 'EMAIL INVALID'
    else:
        namaUser = xPisah[0]
        namaHosting = xPisah[1]
        ekstensi = xPisah[2]
        if ekstensi.isalpha() == False or len(ekstensi) > 5:
            return 'EMAIL INVALID'    
        else:
            if namaHosting.isalnum() == True:
                if namaUser.isalnum() == True or '_' in namaUser or '-' in namaUser:
                    return 'EMAIL VALID'
                else:
                    return 'EMAIL INVALID'
            else:
                return 'EMAIL INVALID'
print(tes(x))