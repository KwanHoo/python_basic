# zip, unzip 라이브러리 

# zip : 합쳐줌
top = ['트린다미어', '일라오이', '피오라', '잭스']
jungle = ['렉사이', '엘리스', '리 신', '마스터이']

print(list(zip(top, jungle)))
# [('트린다미어', '렉사이'), ('일라오이', '엘리스'), ('피오라', '리 신'), ('잭스', '마스터이')]


# unzip : 분리 시켜줌  *
mixed = list(zip(top, jungle))
print(list(zip(*mixed))) # *을 넣음으로서 분리
#[('트린다미어', '일라오이', '피오라', '잭스'), ('렉사이', '엘리스', '리 신', '마스터이')]

topcarry, jugclass = zip(*mixed)
print(topcarry) # ('트린다미어', '일라오이', '피오라', '잭스')
print(jugclass) # ('렉사이', '엘리스', '리 신', '마스터이')