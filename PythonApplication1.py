tab_num=0 #her açılış işaretinde bir tab daha ve her kapanışta azalması için sayı belirliyoruz
reg_doc=open('out.c','w',encoding="utf-8")#Çıktı dosyamızı burada belirtiyoruz eğer belirtilen isim yoksa otomatik oluşturuyor.
irreg_doc=open('main.c','r')#main.c dosyasını okuma modunda açıyoruz

for line in irreg_doc:#for döngüsüyle main.c dosyasını atadığımız değişkenin her satırını döndürüyoruz.
    if line[0]=="{":#açılış paranteziyse ilk satırı yazdırıp sonra değeri attırıyoruz
        if tab_num==0:
            satir=int(tab_num-1)*"\t"+line+"\n"#satıra tab_num değişkenimiz kadar tab ekleyip sonuna yeni satır için "\n" koyuyoruz
        else:
            satir=int(tab_num)*"\t"+line+"\n"
        tab_num+=1#açılış parantezinde değeri arttırdığımız satır
    elif line[0]=="}":#kapanış ise ilk tab sayısını azaltıp sonra satırı yazdırıyoruz
        tab_num-=1#tab numaramızı azalttığımız kısım
        satir=int(tab_num)*"\t"+line+"\n"
    else:
        satir=int(tab_num)*"\t"+line+"\n"
    reg_doc.write(satir)#her satırı işlemlerden geçirdikten sonra dosyaya yazdığımız kısım
    #Mustafa Uhud Durmuş 348345
    
