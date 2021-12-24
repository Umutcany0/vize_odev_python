class yemektarifleri :
    def yemektarifleri_gir(self) :
        tarifAdi = input("Tarıf Adı : ")
        tarif.append(tarifAdi)
        while True :
            tarifasama = input('Tarif Asama Ekle(Asama Sonlandıysa "60" giriniz.) : ')
            if tarifAsama == "60" :
                yemektarifleri_listesi.append(tarif)
                tarif.append("\n")
                break
            else :
                tarif.append(tarifAsama)


    def goster(self) :
        number = len(yemektarifleri_listesi)
        print("Tüm Tarifler")
        for asama in tarif :
                print(asama)




def menua() :
    while True :
        print("\Yemek Tarifleri Gir : 1\nYemek Tarifleri Goster : 2\n Sonlandır : 3 ")
        secim = input("Yapmak İstediğiniz İşlem Numarasını Giriniz: ")
        islem = YemekTarifleri()
        if secim == "1" :
            islem.yemektarifleri_gir()
        elif secim == "2" :
            islem.goster()
        elif secim == "3" :
            exit(0)
        else :
            print("Hatalı İşlem Yaptınız.")



yemektarifleri_listesi = []
yemektarifleri = []

menua()
