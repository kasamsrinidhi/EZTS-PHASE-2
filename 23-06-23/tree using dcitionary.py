#dictionary(forest of 3 trees)
Families={
           'srinidhi':
                      {'preethi':{'mithra','madhu'},
                       'bhavana':{'anuhya'}},
           'shreshta':
                      {'ankitha':{'teju'},
                       'yochana':{'ananaya'},
                       'gayathri':{'sadhvi'}},
           'rishika':
                     {'sam':'cat','ferret':'fox'}
           }
for parent ,children in Families.items():
    print(f"{parent} has {len(children)}kids(s):")
    print(f"{', and '.join([str(child)for child in [*children]])}")
 
