from function import *
    
welcomeMessage()
i=0
while(True):
    if i==0:

        print('Hansı imkanlardan faydalanmaq istəyirsiniz ? ')
        print('1. Benzin Stansiyası')
        print('2. Mağaza')
        print('0. Çıxış')
        choice = int(input('Seçiminizi daxil edin: '))
        if(choice == 0): 
            print('𝙂𝙤𝙧𝙪𝙨𝙚𝙣𝙚𝙙𝙚𝙠')
            break
        if(choice == 1):
            totalPrice += gasStation()

        if(choice == 2):
            totalProductsPrice += shop()
            

        i+=1
    else:
        print('Hansı imkanlardan faydalanmaq istəyirsiniz ? ')
        print('1. Benzin Stansiyası')
        print('2. Mağaza')
        print('3. Meblegi goster')
        print('0. Çıxış')
        choice = int(input('Seçiminizi daxil edin: '))
        if(choice == 0): 
                print(f"""-----------------------------------------------------------------')
                Mağazaya ödəniləcək məbləğ:  {totalProductsPrice} ₼
                Benzin stansiyasina ödəniləcək məbləğ:  {totalPrice} ₼
                Ümumi məbləğ: {totalProductsPrice + totalPrice} ₼
                Ödəniş hansı növdə olacaq ?
                1. Nağd
                2. Terminal İlə""")
                choice = int(input('Ödəniş növünü seçin: '))
                print("Ödəniş uğurla nəticələndi!")
                print("""
            ▒█▀▀█ ▀█▀ ▒█▀▀▀█ ▀█▀ 　 ▒█▀▀▀█ ▒█▀▀▀ ▒█▀▀█ ▒█▀▀▄ ▀█▀ ▒█░░▒█ ▀█▀ ▒█▄░▒█ ▀█▀ ▒█▀▀▀█ 　 ▒█░▒█ ▒█▀▀█ ▒█░▒█ ▒█░▒█ ▒█▄░▒█ 
            ▒█▀▀▄ ▒█░ ░▄▄▄▀▀ ▒█░ 　 ░▀▀▀▄▄ ▒█▀▀▀ ▒█░░░ ▒█░▒█ ▒█░ ▒█▄▄▄█ ▒█░ ▒█▒█▒█ ▒█░ ░▄▄▄▀▀ 　 ▒█░▒█ ▒█░░░ ▒█▀▀█ ▒█░▒█ ▒█▒█▒█ 
            ▒█▄▄█ ▄█▄ ▒█▄▄▄█ ▄█▄ 　 ▒█▄▄▄█ ▒█▄▄▄ ▒█▄▄█ ▒█▄▄▀ ▄█▄ ░░▒█░░ ▄█▄ ▒█░░▀█ ▄█▄ ▒█▄▄▄█ 　 ░▀▄▄▀ ▒█▄▄█ ▒█░▒█ ░▀▄▄▀ ▒█░░▀█ 

            ▀▀█▀▀ ▒█▀▀▀ ▒█▀▀▀█ ▒█░▒█ ▒█▀▀▀ ▒█░▄▀ ▒█░▄▀ ▒█░▒█ ▒█▀▀█ 　 ▒█▀▀▀ ▒█▀▀▄ ▀█▀ ▒█▀▀█ ▀█▀ ▒█░▄▀ 
            ░▒█░░ ▒█▀▀▀ ░▀▀▀▄▄ ▒█▀▀█ ▒█▀▀▀ ▒█▀▄░ ▒█▀▄░ ▒█░▒█ ▒█▄▄▀ 　 ▒█▀▀▀ ▒█░▒█ ▒█░ ▒█▄▄▀ ▒█░ ▒█▀▄░ 
            ░▒█░░ ▒█▄▄▄ ▒█▄▄▄█ ▒█░▒█ ▒█▄▄▄ ▒█░▒█ ▒█░▒█ ░▀▄▄▀ ▒█░▒█ 　 ▒█▄▄▄ ▒█▄▄▀ ▄█▄ ▒█░▒█ ▄█▄ ▒█░▒█
          """)
                break
        elif(choice == 1):
            totalPrice += gasStation()

        elif(choice == 2):
            totalProductsPrice += shop()
            
        elif choice==3:
            print(f'Odenilecek mebleg:{totalPrice+totalProductsPrice}')
        else:
            print("Bele bir proses movcud deyil")
            continue
