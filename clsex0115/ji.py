import jieba
txt = open("d:/Code/python/clsex0115/xiyouji.txt", "r",encoding='utf-8').read()
excludes={"一个","那里","怎么","我们","不知","两个","甚么","只见"\
         ,"不是","原来","不敢","闻言","如何","什么","下载"}
words = jieba.lcut(txt)
counts={}
for word in words :
    if len(word)==1:
        continue
    elif word=="行者" or word=="大圣" or word=="老孙" :
        rword="悟空"
    elif word=="师父" or word=="三藏" or word=="长老" :
        rword="唐僧"
    elif word=="悟净" or word=="沙和尚":
        rword="沙僧"
    elif word=="呆子":
        rword="八戒"
    else:
        rword=word

#    if rword in counts:
#        counts[rword]=counts[rword]+1
#    else:
#        counts[rword]=1
    counts[rword] = counts.get(rword,0) + 1
for word in excludes:
    del counts[word]
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(9):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
