#generator kodów pocztowych
def generator_kodow_pocztowych(pierwszy_kod_pocz: str, ostatni_kod_pocz: str):
    przedrostek_pierw_kodu, przyrostek_pierw_kodu = map(int, pierwszy_kod_pocz.split('-'))
    #79 - 900
    przedrostek_ost_kodu, przyrostek_ost_kodu = map(int, ostatni_kod_pocz.split('-'))
    #80 - 155

    pozostaly_kod = []

    for przedrostek in range(przedrostek_pierw_kodu, przedrostek_ost_kodu + 1):
        if przedrostek == przedrostek_pierw_kodu:
            przyrostek_startowy = przyrostek_pierw_kodu
        else:
            przyrostek_startowy = 0
        
        if przedrostek == przedrostek_ost_kodu:
            przyrostek_koncowy = przyrostek_ost_kodu
        else:
            przyrostek_koncowy = 999
            #79 - 999

        for przyrostek in range(przyrostek_startowy, przyrostek_koncowy + 1):
            pozostaly_kod.append(f"{przedrostek:02d}-{przyrostek:03d}")
    
    return pozostaly_kod

pierwszy_kod_pocz = "79-900"
ostatni_kod_pocz = "80-155"
pozostaly_kod = generator_kodow_pocztowych(pierwszy_kod_pocz, ostatni_kod_pocz)
for kod_pocz in pozostaly_kod:
    print(kod_pocz)
