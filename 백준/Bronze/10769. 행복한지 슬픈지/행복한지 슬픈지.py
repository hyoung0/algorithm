happy = ':-)'
sad = ':-('
sentence = input()

if happy not in sentence and sad not in sentence:
    print('none')
elif sentence.count(happy) == sentence.count(sad):
    print('unsure')
elif sentence.count(happy) > sentence.count(sad):
    print('happy')
elif sentence.count(happy) < sentence.count(sad):
    print('sad')      