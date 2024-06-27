import string


def create_hashtag(s):
    s_cleaned = ''.join([char for char in s if char not in string.punctuation and char != ' '])

    words = s_cleaned.split()
    words_capitalized = [word.capitalize() for word in words]

    hashtag = '#' + ''.join(words_capitalized)

    if len(hashtag) > 140:
        hashtag = hashtag[:140]

    return hashtag


print(create_hashtag('Python Community'))  # #PythonCommunity
print(create_hashtag('i like python community!'))  # #ILikePythonCommunity
print(create_hashtag('Should, I. subscribe? Yes!'))  # #ShouldISubscribeYes
