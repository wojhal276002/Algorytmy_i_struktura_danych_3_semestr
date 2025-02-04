from collections.abc import MutableMapping
from random import randrange


class MapBase(MutableMapping):
    """Our own abstract base class that includes a nonpublic _Item class."""

    # ------------------------------- nested _Item class -------------------------------
    class _Item:
        """Lightweight composite to store key-value pairs as map items."""
        _slots_ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key  # compare items based on their keys

        def __ne__(self, other):
            return not (self == other)  # opposite of _eq_

        def __lt__(self, other):
            return self._key < other._key  # compare items based on their keys

        def __str__(self):
            return str(self._key)


class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression.
    Keys must be hashable and non-None.
    """

    def __init__(self, cap=11, p=109345121, lista=None):
        """Create an empty hash-table map.
        cap initial table size (default 11)
        p positive prime used for MAD (default 109345121)
        """
        self._table = cap * [None]
        self._n = 0  # number of entries in the map
        self._prime = p  # prime for MAD compression
        self._scale = 1 + randrange(p - 1)  # scale from 1 to p-1 for MAD
        self._shift = randrange(p)  # shift from 0 to p-1 for MAD
        self._lista = lista # własność do ustalania listy kluczy i ich indeksów

    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)  # may raise KeyError

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)  # subroutine maintains self._n
        if self._n > len(self._table) // 2:  # keep load factor <= 0.5
            self._resize(2 * len(self._table) - 1)  # number 2^x - 1 is often prime

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)  # may raise KeyError
        self._n -= 1

    def _resize(self, c):
        """Resize bucket array to capacity c and rehash all items."""
        old = list(self.items())  # use iteration to record existing items
        self._table = c * [None]  # then reset table to desired capacity
        self._n = 0  # n recomputed during subsequent adds
        for (k, v) in old:
            self[k] = v  # reinsert old key-value pair

class ProbeHashMap(HashMapBase):
    """Hash map implemented with linear probing for collision resolution."""
    _AVAIL = object() # sentinal marks locations of previous deletions
    def _is_available(self, j):
        """Return True if index j is available in table."""
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL
    def _find_slot(self, j, k):
        """Search for key k in bucket at index j.
        Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location.
        If no match found, success is False and index denotes first available slot.
        """
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j # mark this as first avail
                if self._table[j] is None:
                    return (False, firstAvail) # search has failed
            elif k == self._table[j]._key:
                return (True, j) # found a match
            j = (j + 1) % len(self._table) # keep looking (cyclically)
    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k)) # no match found
        return self._table[s]._value
    def _bucket_setitem(self, k):
        # dodanie elementu na odpowiednią pozycję przez odpowiednie rozwiązanie kolizji
        j = (3*k+5)%11
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k,j) # insert new item
            self._n += 1 # size has increased
        else:
            self._table[s]._value = j # overwrite existing
        if self._lista == None:
            self._lista = []
        self._lista.append((k,s))
    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error: ' + repr(k)) # no match found
        self._table[s] = ProbeHashMap._AVAIL # mark as vacated
    def __iter__(self):
        for j in range(len(self._table)): # scan entire table
            if not self._is_available(j):
                yield self._table[j]._key

    def index_list(self):
        # metoda do wyświetlnia kluczy i ich indeksów w kolejności ich dodawania
        return "Lista rozwiązań postaci (klucz: jego indeks) to " + f"{self._lista}"

    def __str__(self):
        #(troche pokraczna) metoda do wyświetlania tablicy asocjacyjnej
        return str([str(self._table[k]) for k in range(self._n)])

if __name__ == "__main__":
    a = ProbeHashMap()
    a._bucket_setitem(12)
    a._bucket_setitem(44)
    a._bucket_setitem(13)
    a._bucket_setitem(88)
    a._bucket_setitem(23)
    a._bucket_setitem(94)
    a._bucket_setitem(11)
    a._bucket_setitem(39)
    a._bucket_setitem(20)
    a._bucket_setitem(16)
    a._bucket_setitem(5)
    print(a)
    print(a.index_list())

