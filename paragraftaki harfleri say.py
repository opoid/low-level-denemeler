a="lkafnjfyjtyaafkxfyuyfuumkkaaaaajnvjkxdfbnjskdfnvzvxclskclmldnvkjs" \
  "fmsfngrjvslkufdvygöuxbnrgtrtwçnjftyjnyj"
aku=set(a) #a metninde geçen harfleri almak için küme haline getiriyorum çünkü kümelerde aynı veri birden fazla kez tekrar edemez
sayı=0 #sayı adlı 0 değerli bir değişken oluştur    
sonuç=[] #sonuç adlı boş bir liste tanımla
for harf in aku: #a kümesindeki her bir harf için
    for i in a:  #a metninin öğelerine bak
        if harf==i:  #eğer baktığın öğe eldeki harfe eşitse
            sayı+=1  #sayacı 1 arttır
            hmm=[harf,sayı] #bu bilgileri liste tipi bir değişkende tut
    sonuç+=[hmm] #başta tanımladığın listeyi yeni bilgileri ekleyerek güncelle
    sayı=0 #sayacı sıfırla
for p in sorted(sonuç): #listeyi alfabetik sıraya diz ve listenin öğeleri olan harf ve sayısı bilgisini..
    print("{} harfi {} defa geçiyor".format(p[0],p[1])) #..bu şekilde düzenlenmiş bir metnin içine doğru sırayla yerleştirerek ekrana yaz






















