def pig_it(text):
    
   return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())

# print(pig_it('Pig latin is cool')) #'igPay atinlay siay oolcay')
# print(pig_it('This is my string')) #'hisTay siay ymay tringsay')
print(pig_it('O tempora o mores !'))  # Oay emporatay oay oresmay !