totalPrice=0
totalProductsPrice = 0
def calcShopPrice(price, count):
    finalPrice = price*count
    return finalPrice

def gasStation():
    while True:

        print('-----------------------------------------------------------------')
        print('Hansı növ benzin almaq istədiyinizi seçin ?')
        print('1. Aİ-95 (Premium) - 1.6₼/litr')
        print('2. Aİ-98 (Premium) - 1.9₼/litr')
        print('3. Aİ-92 (Premium) - 1.4₼/litr')
        print('4. Dizel (Premium) - 0.9₼/litr')
        
        gasType = input("Növü seçin:")
        if gasType.isnumeric():
            gasType=int(gasType)
        else:
            print('Bele bir proses movcud deyil')
            continue
        if gasType not in [1,2,3,4]:
            print('Bele bir proses movcud deyil')
            continue
        gasCurrentPrice = 0
        volume=0
        if(gasType == 1): gasCurrentPrice = 1.6
        elif(gasType == 2): gasCurrentPrice = 1.9
        elif(gasType == 3): gasCurrentPrice = 1.4
        elif(gasType == 4): gasCurrentPrice = 0.9
        
        
        print('-----------------------------------------------------------------')
        print("Ödənilən məbləğə görə almaq istəyirsiniz yoxsa litrə görə ?")
        print("1: Ödənilən məbləğə görə")
        print("2: Litrə görə")
        
        choice =input("Seçimi qeyd edin:")
        if choice.isnumeric():
            choice=int(choice)
        else:
            print('Bele bir proses movcud deyil')
            continue
        if(choice == 1):
            
            paidAmount = input('Məbləği daxil edin: ')
            if paidAmount.isnumeric():
                paidAmount=float(paidAmount)
            else:
                print('Bele bir proses movcud deyil')
                continue
            if paidAmount>0:
                pass
            else:
                print('Bele bir proses movcud deyil')
                continue
            totalPrice = paidAmount
            volume=paidAmount/gasCurrentPrice

        elif(choice == 2):
            volume = input('Litri daxil edin: ')
            if volume.isnumeric():
                volume=float(volume)
            else:
                print('Bele bir proses movcud deyil')
                continue
            if volume>0:
                pass
            else:
                print('Bele bir proses movcud deyil')
                continue
            totalPrice = round(volume * gasCurrentPrice, 2)
        else:
            print('Bele bir proses movcud deyil')
            continue
        print(f'Siz bu meblege:{totalPrice}₼, {volume}L benzin aldiniz')


        return totalPrice 

def shop():
    while True:
        print('-----------------------------------------------------------------')
        print('Nə almaq istəyirsiniz ?: ')
        print("1: Kola - 0.6₼")
        print("2: Hotdog - 1.2₼")
        print("3: Qogal - 0.70₼")
        print("4: Fanta - 0.60₼")
        print("5: Xacapuri - 1₼")
        print("0: Geri qayıt")
        
        choice =input("Seçimi qeyd edin:")
        if choice.isnumeric():
            choice=int(choice)
        else:
            print('Bele bir proses movcud deyil')
            continue
        print('-----------------------------------------------------------------')
        quantity =input("Neçə ədəd almaq istəyirsiniz ?: ")
        if quantity.isnumeric():
            quantity=int(quantity)
        else:
            print('Bele bir proses movcud deyil')
            continue
        if quantity>0:
            pass
        else:
            print('Bele bir proses movcud deyil')
            continue
        totalProductsPrice = 0
        
        if choice == 1:
            totalProductsPrice = calcShopPrice(0.6, quantity)
        elif choice == 2:
            totalProductsPrice = calcShopPrice(1.2, quantity)
        elif choice == 3:
            totalProductsPrice = calcShopPrice(0.70, quantity)
        elif choice == 4:
            totalProductsPrice = calcShopPrice(0.60, quantity)
        elif choice == 5:
            totalProductsPrice = calcShopPrice(1, quantity)
        else:
            print('Bele bir proses movcud deyil')
            continue
        print('-----------------------------------------------------------------')
        print("Siz ", round(totalProductsPrice, 2), "₼ dəyərində məhsul aldınız")
        return totalProductsPrice

def welcomeMessage():
    print("""
                                ██╗░░██╗░█████╗░░██████╗
                                ╚██╗██╔╝██╔══██╗██╔════╝
                                ░╚███╔╝░██║░░██║╚█████╗░
                                ░██╔██╗░██║░░██║░╚═══██╗
                                ██╔╝╚██╗╚█████╔╝██████╔╝
                                ╚═╝░░╚═╝░╚════╝░╚═════╝░
                                                    █
                                                    
        ░██████╗░███████╗██╗░░░░░███╗░░░███╗██╗░██████╗██╗███╗░░██╗██╗███████╗
        ██╔════╝░██╔════╝██║░░░░░████╗░████║██║██╔════╝██║████╗░██║██║╚════██║
        ██║░░██╗░█████╗░░██║░░░░░██╔████╔██║██║╚█████╗░██║██╔██╗██║██║░░███╔═╝
        ██║░░╚██╗██╔══╝░░██║░░░░░██║╚██╔╝██║██║░╚═══██╗██║██║╚████║██║██╔══╝░░
        ╚██████╔╝███████╗███████╗██║░╚═╝░██║██║██████╔╝██║██║░╚███║██║███████╗
        ░╚═════╝░╚══════╝╚══════╝╚═╝░░░░░╚═╝╚═╝╚═════╝░╚═╝╚═╝░░╚══╝╚═╝╚══════╝╝
        """)

