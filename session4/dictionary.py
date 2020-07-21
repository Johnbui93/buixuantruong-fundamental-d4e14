#person = ['truong',93, 165,63,'hai phong',True, False,1]
#init
person_dict = {
'name':'truong',
'yob':93,
'height': 165,
'weight':63, 
}
if 'nam' in person_dict:  #check if key in dictionary
    print(person_dict['nam'])
#print(person_dict['yob'])  #read one
#name = person_dict['name']
person_dict['job'] = 'dev'  #create
person_dict['name'] = 'John' #update
del person_dict['weight']
for key in person_dict:
    print(person_dict[key])