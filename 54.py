"""
演習4（word2freq）
今，文字列が以下のように与えられています．

doc = 'i bought an apple .\ni ate it .\nit is delicious .'
\nは改行記号なので，3つの文が3行に渡って書かれていることになります．
この文章中の単語を用いて，キーとして単語，値として出現数を持つような辞書word2freqを作成し，出力してください．
ただし，改行記号は単語に含めないでください．
ヒント：改行記号でsplitしてから空白でsplitすれば，単語に分割できます．

期待する出力：{'i': 2, 'bought': 1, 'an': 1, 'apple': 1, '.': 3, 'ate': 1, 'it': 2, 'is': 1, 'delicious': 1}
"""

import collections
doc = 'i bought an apple .\ni ate it .\nit is delicious .'
List=(''.join(doc.split('\n'))).split()
word2freq=dict(collections.Counter(List))
print(word2freq)