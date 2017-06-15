# Tips

## 代表的な調べ方
<b>共通操作や主な機能・特徴については覚えた方が良い</b>。しかし、細かい個々の関数については覚える必要はない。<font color="red">個々の機能が必要になった時に「調べて使える」ようになろう。すなわち「調べ方」を学ぶ</font>必要がある。


- 主な調べ方1: help()
  - 簡易ドキュメントhelpを使って調べる例。
    - help(str)
    - help(str.find)
- 主な調べ方2: 公式ドキュメント（リファレンス）
  - 公式ドキュメント（リファレンス）を使って調べる方法（≒ [pydoc3](https://docs.python.jp/3/library/pydoc.html)）
    - [公式ドキュメント](https://docs.python.org/3/) で strオブジェクトを調べる。（どんなキーワードで調べるのが良いだろうか？）
      - [strオブジェクトについて](https://docs.python.org/3/library/string.html#module-string)
      - [標準オブジェクトについて](https://docs.python.org/3/library/stdtypes.html?#string-methods)
- 主な調べ方3
  - 該当オブジェクトについて、どんな関数が用意されているかを調べる
    - 例えばstrオブジェクトについて調べたい場合。
      1. インタプリタ上でstrオブジェクトを保存した変数を用意する。ここでは``temp = 'hoge'``と保存したとする。
      2. インタプリタ上で「変数名.」と入力した状態でTABキーで補完しようとすると、どのような関数が用意されてるかの一覧が出力される。前述の例に合わせて、``temp.``まで入力してTABキーを押すと次のように出力される。一覧によると、例えば「capitalize(」という関数が用意されているらしい。この関数について調べたいなら ``help(temp.capitalize) ``として、help()を利用しよう。

```
>>> temp = 'hoge'
>>> temp.
temp.__add__(           temp.__rmod__(          temp.istitle(
temp.__class__(         temp.__rmul__(          temp.isupper(
temp.__contains__(      temp.__setattr__(       temp.join(
temp.__delattr__(       temp.__sizeof__(        temp.ljust(
temp.__dir__(           temp.__str__(           temp.lower(
temp.__doc__            temp.__subclasshook__(  temp.lstrip(
temp.__eq__(            temp.capitalize(        temp.maketrans(
temp.__format__(        temp.casefold(          temp.partition(
temp.__ge__(            temp.center(            temp.replace(
temp.__getattribute__(  temp.count(             temp.rfind(
temp.__getitem__(       temp.encode(            temp.rindex(
temp.__getnewargs__(    temp.endswith(          temp.rjust(
temp.__gt__(            temp.expandtabs(        temp.rpartition(
temp.__hash__(          temp.find(              temp.rsplit(
temp.__init__(          temp.format(            temp.rstrip(
temp.__iter__(          temp.format_map(        temp.split(
temp.__le__(            temp.index(             temp.splitlines(
temp.__len__(           temp.isalnum(           temp.startswith(
temp.__lt__(            temp.isalpha(           temp.strip(
temp.__mod__(           temp.isdecimal(         temp.swapcase(
temp.__mul__(           temp.isdigit(           temp.title(
temp.__ne__(            temp.isidentifier(      temp.translate(
temp.__new__(           temp.islower(           temp.upper(
temp.__reduce__(        temp.isnumeric(         temp.zfill(
temp.__reduce_ex__(     temp.isprintable(
temp.__repr__(          temp.isspace(

# 例えば「temp.capitalize(」があるらしい。
# どんな関数なのか調べてみるにはヘルプを使おう。
>>> help(temp.capitalize)
Help on built-in function capitalize:

capitalize(...) method of builtins.str instance
    S.capitalize() -> str

    Return a capitalized version of S, i.e. make the first character
    have upper case and the rest lower case.
```
