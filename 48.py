"""
48. 例外処理
下記のように変数が作られています．

a = 0
b = 5
この時，a/bとb/aを出力してください．ただし，ゼロ割りが発生した時にはzero divisionを出力します．
例外処理を用いて書いてみると良いと思います．

期待する出力：0, zero division
"""

a,b=0,5
try:
    print(a/b)
except ZeroDivisionError:
    print('zero division')
try:
    print(b/a)
except ZeroDivisionError:
    print('zero division')