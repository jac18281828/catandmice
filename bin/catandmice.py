#!/usr/bin/env python3
import sys
import unittest

# 13
#13,1,3,6,10,5,2,4,9,11,12,7
def skipcount(pos, n, visited):
    if len(visited) == 0:
        return (pos + n) % n
    for _ in range(n):
        pos = (pos + 1) % n
        while pos in visited:
            pos = (pos + 1) % n
    return pos

def checksequence(pos, n):
    miceremaining = n
    visited = set()
    while miceremaining > 1:
        pos = skipcount(pos, n, visited)
        visited.add(pos)
        if pos == 0:
            return False
        miceremaining -= 1
    pos = skipcount(pos, n, visited)
    return pos == 0 
                
def skipmice(n):
    if n < 1:
        return 0
    for i in range(n):
        if checksequence(i, n):
            return i
    return None

class skip_test(unittest.TestCase):
    def test_thirteen(self):
        self.assertEqual(5, skipmice(13))

    def test_one(self):
        self.assertEqual(0, skipmice(1))        

if __name__ == '__main__':
    if len(sys.argv) > 1:
        for num in sys.argv[1:]:
            pos = skipmice(int(num))
            if pos is not None and pos >= 0:
                print('%s, Yes, %d' % (num, pos))
            else:
                print('%s, No' % (num))
    else:
        unittest.main()
