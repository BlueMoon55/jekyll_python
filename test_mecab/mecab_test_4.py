import MeCab as mc
t = mc.Tagger('-Ochasen')
sentence = u"今日は朝から良い天気ですが、夕方から雨が降りそう。外出時は、傘を忘れないようにね"
print(sentence)
sentence = sentence.replace('\n', ' ')
text = sentence.encode('utf-8')
print(text.decode('utf-8'))
node = t.parseToNode(text)
print(node)
while(node):
  if node.surface != "": # ヘッダとフッタを除外
    print(node.surface, '/t', node.feature)
  node = node.next
  print(node)
  if node is None:
    break