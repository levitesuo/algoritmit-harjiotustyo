
class LinkedList:
    '''
    Implementaatio doubly linked lististä josta poistaminen ja johon lisäminen on O(0) nopeaa.
    Listassa on hardkoodattu aloitus node joka löytyy paikasta size ** 2
    '''

    def __init__(self, size, start):
        self._size = size
        self.l = [[None, None] for _ in range(size + 1)]

        self.l[start] = [size, None]
        self.l[size][1] = start

        self.i = start

    def __str__(self):
        return str(self.get_list())

    def get_list(self):
        '''
        Transforms the linked list to a conventional list and returns it.
        '''
        l = []
        i = self._size
        while True:
            i = self.l[i][1]
            if i is None:
                return l
            l.append(self._l_to_t(i))

    def insert_after(self, next):
        '''
        Inserts given cell after the current cell.
        '''
        if self.l[self.i][1] is not None:
            self.l[self.l[self.i][1]][0] = next
        self.l[next] = [self.i, self.l[self.i][1]]
        self.l[self.i][1] = next

    def delete_if_able(self, cord):
        '''
        Deletes a cell if it exists.
        '''
        if self.l[cord] == [None, None]:
            return
        self.l[self.l[cord][0]][1] = self.l[cord][1]
        if self.l[cord][1] is not None:
            self.l[self.l[cord][1]][0] = self.l[cord][0]
        self.l[cord] = [None, None]

    def delete_current(self):
        '''

        '''
        self.l[self.l[self.i][0]][1] = self.l[self.i][1]
        if self.l[self.i][1] is not None and self.l[self.l[self.i][1]] is not None:
            self.l[self.l[self.i][1]][0] = self.l[self.i][0]
        self.l[self.i][0] = None

    def iterate(self):
        if self.l[self.i][1] is None:
            return False
        self.i = self.l[self.i][1]
        return True

    def get_i(self):
        return self._l_to_t(self.i)

    def empty(self):
        return self.l[self._size][1] is None

    def _l_to_t(self, i):
        return (i//self._size, i % self._size)

    def _t_to_l(self, cord):
        return (cord[0]*self._size + cord[1])