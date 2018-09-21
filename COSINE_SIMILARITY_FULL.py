import math


cal_v = dict()
cal_1 = dict()

dot_product = 0.0
x = 0
sum_1 = 0.0
sum_v = 0.0
def cosine_simil(cal_v,cal_1):
    global sum_1,sum_v,customer1_dictionary,variable_dictionary,dot_product,x
    for keys,values in cal_1.items():
        dot_product += cal_v[keys]*cal_1[keys]
    sum_1 = 0.0
    sum_v = 0.0
    for keys,values in customer1_dictionary.items():
        sum_1 += math.pow(values,2)
    for keys,values in variable_dictionary.items():
        sum_v += math.pow(values,2)
    cosine_similarity = (dot_product/(math.sqrt(sum_1) * math.sqrt(sum_v)))
    print('COSINE SIMILARITY :-- ',cosine_similarity,'  With CUSTOMER ID:---- ',x)
    dot_product=0.0


customer1_dictionary = dict()
file = open('ratings.csv')
for line in file:
    if(int(line.split(',')[0])==1):
        customer1_dictionary[int(line.split(',')[1])]=float(line.split(',')[2])
    else:
        break

for x in range(2,672):
    variable_dictionary = dict()
    file2 = open('ratings.csv')
    for line2 in file2:
        if(int(line2.split(',')[0])>x):
            break
        elif(int(line2.split(',')[0])==x):
            variable_dictionary[int(line2.split(',')[1])]=float(line2.split(',')[2])

    final_customer1_dict = dict()
    final_variable_dict = dict()

    for keys,values in customer1_dictionary.items():
        if(keys in variable_dictionary):
            final_customer1_dict[keys]=values
            final_variable_dict[keys]=variable_dictionary[keys]
    if(final_variable_dict):
        cosine_simil(final_variable_dict,final_customer1_dict)
