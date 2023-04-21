def smash(word: list) -> str:
    return ''.join([''.join(i + " ") if i != word[-1] and len(word) != 1 \
                    else ''.join(i) for i in word]) 
    
