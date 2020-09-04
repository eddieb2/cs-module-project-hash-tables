def word_count(s):
    cache = {}

    spl = s.split(" ")

    # print(spl)
    words = []
    for i in spl:
        s = ''.join(char for char in i if char.isalnum())
        words.append(s.lower())


    for word in words:
        if word.isalpha() is False:
            continue
        if word not in cache:
            cache[word] = 0

        cache[word] += 1

    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print(word_count('a a\ra\na\ta \t\r\n'))

    # print(cache)

    # (x == {'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1})