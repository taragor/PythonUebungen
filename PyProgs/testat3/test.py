#!/usr/bin/python3
import unittest
import student
from itertools import count, islice

class GeneratorTest(unittest.TestCase):
    "test class for genx"


    def show(self, what, args, expected, got):
        print("%s(%s)"% (what, args))
        print("  expected = %s\n  got      = %s" % (str(expected), str(got)))
        
    def test_a_skip(self):
        what = "skip"
        print("test_%s" % what)
        expected = [1, 2, 4, 7, 11, 16]
        got = list(student.skip(list(range(1, 21)))) # mit list
        self.show("skip", "list(range(1, 21))", expected, got)
        self.assertEqual(expected, got)
        expected = [1, 2, 4, 7, 11, 16]
        got = list(student.skip(range(1, 21))) # mit range
        self.show("skip", "range(1, 21)", expected, got)
        self.assertEqual(expected, got)
        expected = [1, 2, 4, 7, 11, 16]
        got = list(student.skip((e for e in range(1, 21)))) # mit gen
        self.show("skip", "range(1, 21)", expected, got)
        self.assertEqual(expected, got)
        s = "supercalifragilisticexpialidocious"
        expected = "suearixo"
        got = "".join(list((student.skip(s))))
        self.show("skip", s, expected, got)
        self.assertEqual(expected, got)
        # unendlicher Generator
        expected = [2, 4, 8, 14, 22, 32, 44, 58, 74, 92]
        gerade_zahlen = count(2, 2)
        gen = student.skip(gerade_zahlen)
        got = list(islice(gen, 0, 10))
        self.show("skip", "islice(count(2, 2), 1, 10)", expected, got)
        self.assertEqual(expected, got)
        # leer
        expected = []
        got = list(student.skip(range(1, 1))) # leer
        self.show("skip", "range(1, 1)", expected, got)
        self.assertEqual(expected, got)

    def test_b_fill(self):
        print("test_fill")
        expected = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2]        
        got = list(student.fill([1, 3, 6, 2]))
        self.show("fill", "[1, 3, 6, 2]", expected, got)
        self.assertEqual(expected, got)
        expected = [1, 2, 3, 2, 1]        
        got = list(student.fill([1, 2, 3, 2, 1]))
        self.show("fill", "[1, 3, 6, 2]", expected, got)
        self.assertEqual(expected, got)
        expected = [1, 0, -1, -2]        
        got = list(student.fill([1, -2]))
        self.show("fill", "[1, -2]", expected, got)
        self.assertEqual(expected, got)
        expected = [1, 0, -1, -2]        
        got = list(student.fill([1, 0, -2]))
        self.show("fill", "[1, 0, -2]", expected, got)
        self.assertEqual(expected, got)
        expected = [] 
        got = list(student.fill([])) # leer
        self.show("fill", "[]", expected, got)
        self.assertEqual(expected, got)
        # Generator
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6]
        got = list(student.fill((e for e in (1, 8, 7, 2, 6)))) # leer
        self.show("fill", "(e for e in (1, 8, 7, 2, 6))", expected, got)
        self.assertEqual(expected, got)
        # unendlicher Generator
        expected = list(range(1, 21))
        ungerade_zahlen = count(1, 2)
        gen = student.fill(ungerade_zahlen)
        got = list(islice(gen, 0, 20))
        self.show("skip", "islice(count(1, 2), 1, 21)", expected, got)
        self.assertEqual(expected, got)
        expected = []
        got = list(student.skip(range(1, 1))) # leer
        self.show("skip", "range(1, 1)", expected, got)
        self.assertEqual(expected, got)
        


if __name__ == '__main__':
    unittest.main()