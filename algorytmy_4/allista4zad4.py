class RootError(Exception):
    pass

class ChildError(Exception):
    pass

class ParentError(Exception):
    pass

#błędy, które będą wyświetlane jesli coś nie tak

class BinaryTreeByArray:
    #zaimplementowane metody, o które Pan prosił
    def __init__(self):
        self.data = [None]
        self.size = 0
        self.root = 0
        self.level = 0

    def set_root(self, value):
        if self.data[self.root] is not None:
            raise RootError("Root already exists")
        self.data[self.root] = value
        self.size += 1
        self.level += 1

    def add_left_child(self, parent, child_value):
        if self.data[parent] is None:
            raise ParentError("Parent doesn't exist")
        child = 2*parent + 1
        if len(self.data) - 1 < child:
            self.data += [None] * 2 ** self.level
            self.level += 1
        if self.data[child] is not None:
            raise ChildError("Child already exists")
        self.data[child] = child_value
        self.size += 1

    def get_left_child(self, parent):
        child = 2*parent + 1
        if self.data[child] is None:
            raise ChildError("Child doesn't exists")
        return self.data[child]

    def add_right_child(self, parent, child_value):
        if self.data[parent] is None:
            raise ParentError("Parent doesn't exist")
        child = 2*parent + 2
        if len(self.data) - 1 < child:
            self.data += [None] * 2 ** self.level
            self.level += 1
        if self.data[child] is not None:
            raise ChildError("Child already exists")
        self.data[child] = child_value
        self.size += 1

    def get_right_child(self, parent):
        child_index = 2*parent + 2
        if self.data[child_index] is None:
            raise ChildError("Child doesn't exists")
        return self.data[child_index]

    #usuwane wszystkie nody pod nodem usuwanym, metodą schodzenia po gałęziach i wracania nimi pętlą while
    def remove_node(self, value):
        i = value
        while True:
            if 2*i + 1 <= len(self.data)-1:
                if self.data[2*i+1] != None:
                    i = 2*i + 1
                elif self.data[2*i+2] != None:
                    i = 2*i + 2
                elif (self.data[2*i+1] == None and self.data[2*i+1] == None):
                    self.data[i] = None
                    if i%2 == 1:
                        if (i-1)/2 >= value:
                            i = (i-1)//2
                        else:
                            break
                    else:
                        if (i-2)/2 >= value:
                            i = (i-2)//2
                        else:
                            break
            else:
                self.data[i] = None
                if i % 2 == 1:
                    if (i - 1) / 2 >= value:
                        i = (i - 1) // 2
                    else:
                        break
                else:
                    if (i - 2) / 2 >= value:
                        i = (i - 2) // 2
                    else:
                        break
        return self.data

    #przedstawienie wizualne drzewa jako listy
    def __str__(self):
        return str(self.data)


d = BinaryTreeByArray()
d.set_root(1)
d.add_left_child(0,2)
d.add_right_child(0,3)
d.add_left_child(1,4)
d.add_left_child(3,5)
d.add_right_child(3,6)
print(d)
d.remove_node(0)
print(d)

