def replace_word():
    
    str = "Bom dia! Bora estudar Python!"
    word_to_replace = input("Digite a palavra que quer substituir: ")
    word_to_replacecement = input("Digite a palavra para substituir: ")
    print(str.replace(word_to_replace, word_to_replacecement ))
    
replace_word()