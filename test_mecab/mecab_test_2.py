def init_mecab(dic_path=''):
   arg = ''  # 引数はここ
   if dic_path:
       arg = '-d ' + dic_path  # ユーザー辞書のpathをdic_pathへ
   m = MeCab.Tagger(arg)
   m.parseToNode('')  # バグ対策で空打ちする
   return m


def tokenize_mecab(text, m):
   mecab_nodes = m.parseToNode(text)
   surfaces = []
   while mecab_nodes:
       surfaces.append(mecab_nodes.surface)  # surfaceで表層形、featureで形態素情報
       mecab_nodes = mecab_nodes.next  # nextを忘れない
   return surfaces

text = 'これはテストです'
m = init_mecab(dic_path)
token = tokenized_mecab(text, m)
print(token)