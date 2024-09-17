def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        check_word = root_word.lower()
        check_words = other_words[i].lower()
        if check_words in check_word or check_word in check_words:
            same_words.append(other_words[i])
        else:
            continue
    print(f'Слово: {root_word}, ряд слов: {same_words}')
single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
