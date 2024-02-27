def snake_to_camel(word):
    words = word.split('_')  # Split the word into parts on underscores
    camel_case_words = []
    
    for x in words:
        if x:  
            camel_case_words.append(x.capitalize())
        else:  
            camel_case_words.append('_')
    
    return ''.join(camel_case_words)
