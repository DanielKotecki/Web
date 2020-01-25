from zeep import Client

client=Client(wsdl='http://localhost:52210/WebService.asmx?WSDL')
#client.service.ladowanie('Henryk',"Felicjan",'mail@gamail.com','Sosnowiec')
#print(client.service.Baza())        

while True:

    print("1.Wyświetl cała bazę")
    print("2.Dodaj do Bazy")
    print("3.Usuń z bazy")
    print("4.Wyświetl tylko dostępne")
    print("5.Zmień status dostępności samochodu")
    print("6.Wyjście")
    zmiena=int(input("podaj:"))
    if zmiena==1:
        print(client.service.Baza())
    elif zmiena==2:
        marka=input("Podaj markę samochodu:")
        model=input("Podaj model:")
        moc_silnika=int(input("Podaj moc silnika:"))
        client.service.ladowanie(marka,model,moc_silnika)
        
    elif zmiena==3:
        identyfikator= int(input("podaj id samochodu który chcesz usunąć z bazy danych"))
        print(client.service.usuwanie(identyfikator))
    elif zmiena==4:
         print(client.service.tylkoDostepne())
    elif zmiena==5:
        identyfikator= int(input("podaj id samochodu którego zmodyfikować dostępność"))
        print("1.Zmień na niedostępne")
        print("2.Zmień na dostępne")
        wpisana=int(input("Podaj:"))
        if wpisana==1:
            print(client.service.modDosN(identyfikator))

        elif wpisana==2:
             print(client.service.modDosT(identyfikator))
        
    elif zmiena==6:
        break
        
   
    