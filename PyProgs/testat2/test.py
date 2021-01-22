#!/usr/bin/python3
import unittest
import student

lengths = [
    7, 7, 6, 8, 5, 4, 11, 12, 16
    ]

def report_got(what, header, lines):
    print("  " + what)
    print("  header: %s" % str(header))
    print("   lines: %s" % str("\n          ".join(map(str, lines))))

def show(header, entries):
    "fÃ¼r sie zum probieren, wird nicht verwendet"
    for entry in entries:
        for h in header:
            print(entry[h], end=" ")
        print()


class StudentTest(unittest.TestCase):
    "test class for student.readcsv"


    def check_len(self, exp_perline, exp_line, header, lines):
        self.assertEqual(exp_perline, len(header))
        for line in lines:
            self.assertEqual(exp_perline, len(line))
            if exp_line is not None:
                for i, part in enumerate(exp_line):
                    self.assertEqual(lengths[part], len(line[header[i]]))

    def test_afilter(self):
        print("test_afilter")
        header, lines = student.readcsv("bsp.csv", "")
        report_got("a1", header, lines)
        self.check_len(9, None, header, lines)
        header, lines = student.readcsv("bsp.csv", "matnr")
        report_got("a2", header, lines)
        self.check_len(1, [2], header, lines)

    def test_bsome(self):
        header, lines = student.readcsv("bsp.csv", "vorname", "name", "matnr", "semester", "alter", "note", "entfwohnort")
        report_got("b1", header, lines)
        self.check_len(7, [0, 1, 2, 3, 4, 5, 6], header, lines)
        header, lines = student.readcsv("bsp.csv", "ame", "no", "kommentar2")
        report_got("b2", header, lines)
        self.check_len(5, [0, 1, 5, 6], header, lines)

if __name__ == '__main__':
    unittest.main()