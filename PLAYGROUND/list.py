if __name__ == '__main__':
    list=[]
    a=set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
    
        _=[]
        _.append(name)
        _.append(score)
        list.append(_)
    new_list=sorted(list,key=lambda x : x[1]) 
    print(list)
    print(new_list)
    print(len(new_list))
    # first_lowest=new_list[0][1]
    # for i in range(len(new_list)):
    #     if new_list[i][1] < first_lowest:
    #         first_lowest=new_list[i][1]
    # print(first_lowest) 
    # second_lowest=new_list[0][1]
    # for x in range(len(new_list)):
    #     if new_list[x][1] > first_lowest and new_list[x][1] < second_lowest:
    #         second_lowest=new_list[x][1]     
    score=str(score)
    set=set()
    for a in range(len(new_list)):
        for i in _:
            if i in set:
                print(_[a-1][0],end="")
            else:
                set.add(i)     
        


