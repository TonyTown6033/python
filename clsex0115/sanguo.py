import jieba
txt = open("/mnt/d/Code/python/clsex0115/sanguoyanyi.txt", "r",encoding='utf-8').read()
excludes={"将军","却说","丞相","二人","不可","荆州","不能","如此"\
          ,"商议","如何","主公","军士","左右","军马","引兵","次日","大喜","天下"}
words = jieba.lcut(txt)
counts={}
for word in words :
    if len(word)==1:
        continue
    elif word=="孔明曰" :
        rword="孔明"
    elif word=="玄德" or word=="玄德曰" :
        rword="刘备"
    elif word=="关公" or word=="云长":
        rword="关羽"
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
