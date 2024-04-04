from django.shortcuts import render
from PyDictionary import PyDictionary

def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dictionary = PyDictionary()

    if search:
        meaning = dictionary.meaning(search)
        synonyms = dictionary.synonym(search)
        antonyms = dictionary.antonym(search)
        translation_arabic = dictionary.translate(search, 'ar')
        translation_urdu = dictionary.translate(search, 'ur')
    else:
        # Handle case where search query is empty or None
        meaning = {}
        synonyms = []
        antonyms = []
        translation_arabic = ''
        translation_urdu = ''

    context = {
        'search': search,
        'meaning': meaning,
        'synonyms': synonyms if synonyms else ['No synonyms found'],
        'antonyms': antonyms if antonyms else ['No antonyms found'],
        'translation_arabic': translation_arabic if translation_arabic else 'No Arabic translation found',
        'translation_urdu': translation_urdu if translation_urdu else 'No Urdu translation found'
    }
    return render(request, 'word.html', context)
