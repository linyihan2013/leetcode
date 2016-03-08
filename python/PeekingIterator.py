class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.peeked = False
        self.nextElem = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.peeked == False:
            self.peeked = True
            self.nextElem = self.iterator.next()
        return self.nextElem

    def next(self):
        """
        :rtype: int
        """
        if self.peeked:
            self.peeked = False
            nextElem = self.nextElem
            self.nextElem = None
            return nextElem
        return self.iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.peeked or self.iterator.hasNext()