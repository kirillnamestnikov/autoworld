from app.models import Post


def ff(vhod):
    zapros = ""
    l = Post.query.all()
    list = []
    for el in l:
        list.append(el.car_brand)
    list2 = []
    vhod = vhod.lower()
    for i in list:
        list2.append(i.lower())
    if vhod.lower() in list2:
        return list[list2.index(vhod)]
    alph = [chr(i) for i in range(ord("a"), ord("z") + 1)]
    alph_rus = [chr(i) for i in range(ord("а"), ord("я") + 1)]
    check = [int(i) for i in range(-1, -30, -1)]
    DicLetter = {}
    DicLetterCopy = {}
    DicLetterCopy2 = {}
    DL = {}
    DL_2 = {}
    check_list = []
    check_dic = {}
    for i in alph:
        DL[i] = 0
    for i in alph_rus:
        DL_2[i] = 0
    for i in vhod.lower():
        if i in alph:
            DL[i] += 1
    for i in alph:
        check_list.append(DL[i])
    for i in list:
        i = i.lower()
        prom_dic = {}
        prom = []
        for k in alph:
            prom_dic[k] = 0
        for j in i:
            if j in prom_dic:
                prom_dic[j] += 1
        for k in alph:
            prom.append(prom_dic[k])
        check_dic[i] = prom
    ans, name = 1000, ""
    for j in list2:
        s = 0
        for i in range(len(alph)):
            if check_dic[j][i] != 0:
                s += check_dic[j][i] - check_list[i]
            name = j
        if s < ans:
            ans = s
            prom_name = name
    if prom_name != "":
        r = list[list2.index(prom_name)]
        return r
    for i in range(len(alph)):
        DicLetterCopy[alph[i]] = 0
        DicLetterCopy2[alph[i]] = 0
    col_vo, prom2, ans, endl, PrCop = [], [], [], [], []
    vhod = vhod.lower()
    dictionary = {}
    DictionaryCar = {}
    for i in vhod:
        if i.isalpha():
            zapros += i
        else:
            zapros += ""
    for i in range(len(list)):
        for j in range(len(alph)):
            DicLetter[alph[j]] = 0
        for j in list[i]:
            DicLetter[j] = DicLetter.get(j, 0) + 1
        DictionaryCar[list[i]] = dictionary.values()
        prom = []
        for j in DicLetter.values():
            prom.append(j)
        prom2.append(prom)
        dictionary[list[i]] = prom
    DicLetter = DicLetterCopy2
    for i in range(len(zapros)):
        for j in zapros[i]:
            DicLetter[j] = DicLetter.get(j, 0) + 1
        for j in DicLetter.values():
            ans.append(j)
        DicLetter = DicLetterCopy2
    PrCop = prom2
    for i in range(len(prom2)):
        for j in range(len(prom2[0])):
            prom2[i][j] -= ans[j]
    flag = True
    for i in range(len(prom2)):
        for j in check:
            if j in prom2[i]:
                flag = False
        if flag:
            endl.append(sum(prom2[i]))
        else:
            endl.append(100)
            flag = True
    answer = endl.index(min(endl))
    #return list[answer]
    return prom_name


