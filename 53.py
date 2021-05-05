"""
演習3（num2freq）
リストが以下のように定義されています．

nums = [1,2,4,3,2,1,5,1]
このリストに対して，要素の出現数を格納した辞書num2freqを作成し，出力してください．これはnum2freq[要素] = 出現数となるような辞書で，例えばnum2freq[1] = 3です．

期待する出力：{1: 3, 2: 2, 4: 1, 3: 1, 5: 1}
"""

import collections
nums = [1,2,4,3,2,1,5,1]
num2freq=dict(collections.Counter(nums))
print(num2freq)
