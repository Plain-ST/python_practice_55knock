"""
10. 文字列（format）
変数aに5を，変数bに3を代入し，これらの変数を用いて'5%3=2'という文字列を出力してください．

期待する出力：5%2=2
"""

a,b=5,3
print("{}%{}={}".format(a,b,a%b))