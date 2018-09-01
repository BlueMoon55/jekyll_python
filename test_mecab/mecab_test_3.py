import MeCab
mecab = MeCab.Tagger ("-Ochasen")
print(mecab.parse("もっと熱くなれよ"))