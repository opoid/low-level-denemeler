a="lkafnjfyjtyaafkxfyuyfuumkkaaaaajnvjkxdfbnjskdfnvzvxclskclmldnvkjs" \
  "fmsfngrjvslkufdvygöuxbnrgtrtwçnjftyjnyj"
aku=set(a)
sayı=0
sonuç=[]
for h in aku:
    for i in a:
        if h==i:
            sayı+=1
            hmm=[h,sayı]
    sonuç+=[hmm]
    sayı=0
for p in sorted(sonuç):
    print("{} harfi {} defa geçiyor".format(p[0],p[1]))






















