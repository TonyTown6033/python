import jieba
txt = open("d:/Code/python/clsex0115/douluodalu.txt", "r",encoding='utf-8').read()
excludes={"自己","已经","没有","他们","一个","身体","我们","什么"\
          ,"就是","身上","虽然","不是","知道","时候","此时","能够",\
          "同时","天下","这个","之中","只是","如果","出现","你们","现在"}
words = jieba.lcut(txt)
counts={}
for word in words :
    if len(word)==1:
        continue
#    elif word=="孔明曰" :
#        rword="孔明"
#    elif word=="玄德" or word=="玄德曰" :
#        rword="刘备"
#    elif word=="关公" or word=="云长":
#        rword="关羽"
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
for i in range(8):
    word,count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
