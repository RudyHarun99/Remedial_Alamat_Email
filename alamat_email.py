def cekEmail():
    email=input('Input email : ')
    pisah=email.split('@')
    pisahTitik=pisah[1].split('.')
    namaUser=pisah[0]
    namaHosting=pisahTitik[0]
    ekstensi=pisahTitik[1]
    if ekstensi.isalpha() == False or len(ekstensi) > 5:
        print('EMAIL INVALID')    
    else:
        if namaHosting.isalnum() == True:
            if namaUser.isalnum() == True or '_' in namaUser or '-' in namaUser:
                print('EMAIL VALID')
            else:
                print('EMAIL INVALID')
        else:
            print('EMAIL INVALID')
cekEmail()