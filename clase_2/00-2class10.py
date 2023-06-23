dictionary = {"gato": "chat", "perro" : "chien", "caballo" : "cheval"}
words = ['gato', 'león', 'caballo' ]

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "no está en el dicionario")


dictionary = {"gato": "chat", "perro" : "chien", "caballo" : "cheval"}


dictionary['gato'] = 'minou' #MODIFICAR

dictionary['cisne'] = 'cygne'
dictionary.update({"pato":"canard"})
del dictionary["perro"]

print(dictionary)