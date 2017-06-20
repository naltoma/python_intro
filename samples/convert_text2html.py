"""文字列処理のコード例: テキストファイルにHTML形式でURLを埋め込む。

処理対象: text (str型オブジェクト)
URLを埋め込む対照語: keyword (str型オブジェクト)
埋め込みたいURL: url (str型オブジェクト)

case1:
　テキストファイル全体を小文字変換し、
　指定されたkeywordと一致するならURL埋め込みテキストに置換。
　事前に小文字変換してるため、置換後のテキストが小文字になってる点がやや不満。

case2:
　str.split()で分割し、リストを複製した上で要素毎に処理。
　単語毎に小文字変換しているため、変換前の単語を利用して置換後のテキストを生成。
　単語毎に処理しているため単語数が増えると遅くなるのがやや不満。
"""

def convert_text2html_case1(text, keyword, url):
    source = text.lower()
    if keyword in source:
        linked_html = '<a href="{0}">{1}</a>'.format(url, keyword)
        embed_text = source.replace(keyword, linked_html)
    return embed_text

def convert_text2html_case2(text, keyword, url):
    words = text.split(' ')
    target = words[:]
    for index, value in enumerate(words):
        if keyword == value.lower():
            target[index] = '<a href="{0}">{1}</a>'.format(url, value)
    embed_text = ' '.join(target)
    return embed_text


text = 'Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly brackets or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java.[22][23] The language provides constructs intended to enable writing clear programs on both a small and large scale.[24]'
keyword = 'python'
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
result = convert_text2html_case1(text, keyword, url)

with open('output.html', 'w') as f:
    f.write(result)
