#Find the longest list 

lists=[[1,2,3],[1,1,1,1,1],[2,2,3,3],[999,99,99,9,29329,9439493],[100,200,300]]
longest_list_number=len(lists[0])
longest_list= lists[0]

for inner_list in lists:
    length_of_list=len(inner_list)

    if length_of_list > longest_list_number:
       longest_list_number=length_of_list
       longest_list=inner_list
       
print(f'The longest list is: {longest_list} and it\'s length is: {longest_list_number}')
