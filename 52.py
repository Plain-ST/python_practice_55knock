"""
演習2（辞書の値ソート）
辞書が以下のように定義されています．

dic = {'two':324, 'four':830, 'three':493, 'one':172, 'five':1024}
この時，値で昇順ソートしたと考えた場合のキーの並びを出力してください．

期待する出力：['one', 'two', 'three', 'four', 'five']
"""

dic = {'two':324, 'four':830, 'three':493, 'one':172, 'five':1024} 
print([elem[0] for elem in sorted(list(dic.items()), key=lambda x:x[1])])