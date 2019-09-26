class ListEquals(object):

    @staticmethod
    def equals(list1, list2):
        if list1 == list2:
            return True
        else:
            c_list = list1.copy()

            for attr in c_list:
                if attr in list2:
                    j = 0
                    for j in range(len(list2)):
                        if attr == list2[j]:
                            list2.pop(j)
                            break
                    i = 0
                    for i in range(len(list1)):
                        if attr == list1[i]:
                            list1.pop(i)
                            break
            if list1:
                print(f'Need to delete fields: {list1}')
            if list2:
                print(f'Need to add fields: {list2}')
            return not list1 and not list2
