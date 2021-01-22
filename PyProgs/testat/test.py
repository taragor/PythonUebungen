#!/usr/bin/python3
import unittest
import student

"""Test der Funktionen student.check_format und student.check_structure
das texinfo dateien auf Korrektheit prÃ¼ft
* check_format: 
  - Alle Zeilen mit Kommandos beginnen mit einem @ direkt gefolgt von
    dem Kommando aus ASCII-Kleinbuchstaben als separates Wort gefolgt
    von weiterem Inhalt auf dieser Zeile je nach Kommando
  - Die erste Zeile beginnt immer mit '\input texinfo'
  - Bevor eine weitere Zeile ohne Kommando kommt muss es eine 
    Zeile mit dem Kommando 'settitle' geben
  - Die letzte nichtleere Zeile ist immer das Kommando 'bye'
  Die Funktion checkformat erhÃ¤lt das vollstÃ¤ndig eingelesene Dokument
  als ein groÃŸer String und prÃ¼ft, ob das Dokument ordentlich formatiert
  ist. Die RÃ¼ckgabe ist ein Tupel 
  - (None, Fehlercode) falls ein Fehler auftritt.
    Fehlercode sind: 1 -> keine gute erste Zeile
                     2 -> keine settitle vor der ersten Nicht-Kommando-Zeile
                     3 -> Kein Kommando bye oder Zeilen nach bye oder 
                          Werte in bye Zeile
  - (zeilen, statistic), falls Dokument okay ist, wobei 
       zeilen: int, die Anzahl aller nichtleeren, nicht nur whitespace, Zeilen 
               auÃŸer der ersten, die keine Kommando-Zeilen sind
       statistic: dictionary, ein Abbildung von dem String des 
                  Kommando-Namens und der Anzahl des Vorkommens 
                  des Kommandos ist, also z.B. ist immer  'bye': 1 
                  Teil dieses Dictionaries

* check_structure
  Manche Kommandos bilden eine Klammer und haben ein entsprechendes 
  end-Kommando. 
  Zum Beispiel das Kommando 'titlepage':
    @titlepage
    @title Egal
    @end titlepage
  Suchen Sie in dem aktuellen Dokument nach allen Kommandos, die ein 
  end-Kommando haben und dann fÃ¼r Sie Klammer-Kommandos sind.
  Sie kÃ¶nnen davon ausgehen, dass die Dokument check_format bestehen.
  PrÃ¼fen Sie, ob das Dokument korrekt geklammert ist mit den je 
  Dokument gefundenen Klammer-Kommandos. Die RÃ¼ckgabe ist ein Tupel
  - (True, lis) bei korrekter Klammerung, lis ist die sortierte Liste 
                der erkannten Klammer-Kommandos
  - (None, line) bei fehlerhafter Klammerung die Zeile bei der die 
                 fehlerhafte Klammerung erkannt wurde
"""



class StudentTest(unittest.TestCase):
    "test class for student.check_format, student.check_structure"


    def test_a_check_format(self):
        print("Test: check_format")
        tests = [(SAMPLE_1a, "1a", 1), (SAMPLE_1b, "1b", 1),
                 (SAMPLE_2a, "2a", 2), (SAMPLE_2b, "2b", 2),
                 (SAMPLE_3a, "3a", 3), (SAMPLE_3b, "3b", 3)
                 ]
        for content, test, exp in tests:
            got = student.check_format(content)
            print("got for %s =" % test, got)
            print("  expected =", (None, exp))
            self.assertEqual((None, exp), got)

        # fine
        got = student.check_format(SAMPLE_DOC)
        print("gotsample      =", got)
        print("expectedsample = ", SAMPLE_EXPECTED)
        self.assertEqual(SAMPLE_EXPECTED, got) 

        got = student.check_format(SHORT_SAMPLE)
        print("gotshort      =", got)
        print("expectedshort = ", SHORT_SAMPLE_EXPECTED)
        self.assertEqual(SHORT_SAMPLE_EXPECTED, got) 



    def test_b_check_structure(self):
        print("Test: check_structure")
        tests = [SAMPLE_K1, SAMPLE_K2, SAMPLE_K3]
        for content, test, errlineno in tests:
            got = student.check_structure(content)
            errline = content.split("\n")[errlineno]
            print("got for %s =" % test, got)
            if len(got) > 1 and type(got[1] == int):
                print("  identifiziert Zeile: %s" % content.split("\n")[got[1]])
            else:
                print("kein Tupel oder kein Tupel mit int als zweiter Wert")
            print("  expected =", (None, errlineno))
            self.assertEqual((None, errlineno), got)

        # fine
        got = student.check_structure(SAMPLE_DOC)
        print("gotsample      =", got)
        print("expectedsample =", (True, sorted(SAMPLE_KLAMMERCMDS)))
        self.assertEqual((True, sorted(SAMPLE_KLAMMERCMDS)), got)
        
        got = student.check_structure(SHORT_SAMPLE)
        print("gotshort      =", got)
        print("expectedshort =", (True, sorted(SHORT_SAMPLE_KLAMMERCMDS)))
        self.assertEqual((True, sorted(SHORT_SAMPLE_KLAMMERCMDS)), got)



SAMPLE_1a = """@comment $Id@w{$}
@comment %**start of header
@include version.texi
@settitle GNU Sample @value{VERSION}
@syncodeindex pg cp
@comment %**end of header
@copying
This manual is for GNU Sample (version @value{VERSION}, @value{UPDATED}),
which is an example in the Texinfo documentation.
"""

SAMPLE_1b = """\\input textinfo   @c -*-texinfo-*-
@comment $Id@w{$}
@comment %**start of header
@include version.texi
@settitle GNU Sample @value{VERSION}
@syncodeindex pg cp
@comment %**end of header
@copying
This manual is for GNU Sample (version @value{VERSION}, @value{UPDATED}),
which is an example in the Texinfo documentation.
"""

SAMPLE_2a = """\\input texinfo   @c -*-texinfo-*-
@comment $Id@w{$}
@comment %**start of header
@include version.texi
This manual is for GNU Sample (version @value{VERSION}, @value{UPDATED}),
which is an example in the Texinfo documentation.

@settitle GNU Sample @value{VERSION}
@syncodeindex pg cp
@comment %**end of header
@copying
"""

SAMPLE_2b = """\\input texinfo
@comment $Id@w{$}
@comment %**start of header
@include version.texi
@settttitle GNU Sample @value{VERSION}
@syncodeindex pg cp
@comment %**end of header
@copying
This manual is for GNU Sample (version @value{VERSION}, @value{UPDATED}),
which is an example in the Texinfo documentation.
"""

SAMPLE_3a="""\\input texinfo   @c -*-texinfo-*-
@comment $Id@w{$}
@comment %**start of header
@include version.texi
@settitle GNU Sample @value{VERSION}
@syncodeindex pg cp
@comment %**end of header
@copying
This manual is for GNU Sample (version @value{VERSION}, @value{UPDATED}),
which is an example in the Texinfo documentation.

Copyright @copyright{} 2016 Free Software Foundation, Inc.

@quotation
Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3 or
any later version published by the Free Software Foundation; with no
Invariant Sections, with no Front-Cover Texts, and with no Back-Cover
Texts.  A copy of the license is included in the section entitled
``GNU Free Documentation License''.
@end quotation
@end copying
@good bye
"""

SAMPLE_3b="""\\input texinfo   @c -*-texinfo-*-
@comment $Id@w{$}
@comment %**start of header
@include version.texi
@settitle GNU Sample @value{VERSION}
@syncodeindex pg cp
@comment %**end of header
@copying
This manual is for GNU Sample (version @value{VERSION}, @value{UPDATED}),
which is an example in the Texinfo documentation.

Copyright @copyright{} 2016 Free Software Foundation, Inc.

@quotation
Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3 or
any later version published by the Free Software Foundation; with no
Invariant Sections, with no Front-Cover Texts, and with no Back-Cover
Texts.  A copy of the license is included in the section entitled
``GNU Free Documentation License''.
@end quotation
@end copying
@good bye
@bye bye
"""

        
# Original Sample        
SAMPLE_DOC="""\\input texinfo   @c -*-texinfo-*-
@comment $Id@w{$}
@comment %**start of header
@include version.texi
@settitle GNU Sample @value{VERSION}
@syncodeindex pg cp
@comment %**end of header
@copying
This manual is for GNU Sample (version @value{VERSION}, @value{UPDATED}),
which is an example in the Texinfo documentation.

Copyright @copyright{} 2016 Free Software Foundation, Inc.

@quotation
Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3 or
any later version published by the Free Software Foundation; with no
Invariant Sections, with no Front-Cover Texts, and with no Back-Cover
Texts.  A copy of the license is included in the section entitled
``GNU Free Documentation License''.
@end quotation
@end copying

@dircategory Texinfo documentation system
@direntry
* sample: (sample)Invoking sample.
@end direntry

@titlepage
@title GNU Sample
@subtitle for version @value{VERSION}, @value{UPDATED}
@author A.U. Thor (@email{bug-sample@@gnu.org})
@page
@vskip 0pt plus 1filll
@insertcopying
@end titlepage

@contents

@ifnottex
@node Top
@top GNU Sample

This manual is for GNU Sample (version @value{VERSION}, @value{UPDATED}).
@end ifnottex

@menu
* Invoking sample::
* GNU Free Documentation License::
* Index::
@end menu


@node Invoking sample
@chapter Invoking sample

@pindex sample
@cindex invoking @command{sample}

This is a sample manual.  There is no sample program to
invoke, but if there were, you could see its basic usage
and command line options here.


@node GNU Free Documentation License
@appendix GNU Free Documentation License

@include fdl.texi


@node Index
@unnumbered Index

@printindex cp

@bye
"""
SAMPLE_EXPECTED = (17,
                 {'comment': 3, 'include': 2, 'settitle': 1, 'syncodeindex': 1, 'copying': 1, 'quotation': 1, 'end': 6, 'dircategory': 1, 'direntry': 1, 'titlepage': 1, 'title': 1, 'subtitle': 1, 'author': 1, 'page': 1, 'vskip': 1, 'insertcopying': 1, 'contents': 1, 'ifnottex': 1, 'node': 4, 'top': 1, 'menu': 1, 'chapter': 1, 'pindex': 1, 'cindex': 1, 'appendix': 1, 'unnumbered': 1, 'printindex': 1, 'bye': 1})
SAMPLE_KLAMMERCMDS = sorted(["copying", "direntry", "ifnottex", "menu", "quotation", "titlepage", ])

SAMPLE_K1="""\\input texinfo   @c -*-texinfo-*-
@comment $Id@w{$}
@comment %**start of header
@include version.texi
@settitle GNU Sample @value{VERSION}
@syncodeindex pg cp
@comment %**end of header
@copying
This manual is for GNU Sample (version @value{VERSION}, @value{UPDATED}),
which is an example in the Texinfo documentation.

Copyright @copyright{} 2016 Free Software Foundation, Inc.

@quotation
Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3 or
any later version published by the Free Software Foundation; with no
Invariant Sections, with no Front-Cover Texts, and with no Back-Cover
Texts.  A copy of the license is included in the section entitled
``GNU Free Documentation License''.
@end quotation
@end copying

@dircategory Texinfo documentation system
@direntry
* sample: (sample)Invoking sample.
@end direntry

@titlepage
@title GNU Sample
@subtitle for version @value{VERSION}, @value{UPDATED}
@author A.U. Thor (@email{bug-sample@@gnu.org})
@page
@vskip 0pt plus 1filll
@insertcopying
@end titlepage

@contents

@ifnottex
@node Top
@top GNU Sample

This manual is for GNU Sample (version @value{VERSION}, @value{UPDATED}).
@end ifnottex

@menu
* Invoking sample::
* GNU Free Documentation License::
* Index::
@end menu


@node Invoking sample
@chapter Invoking sample

@pindex sample
@cindex invoking @command{sample}

@end menu

This is a sample manual.  There is no sample program to
invoke, but if there were, you could see its basic usage
and command line options here.


@node GNU Free Documentation License
@appendix GNU Free Documentation License

@include fdl.texi


@node Index
@unnumbered Index

@printindex cp

@bye
""", "k1", 59

SAMPLE_K2="""\\input texinfo   @c -*-texinfo-*-
@comment $Id@w{$}
@comment %**start of header
@include version.texi
@settitle GNU Sample @value{VERSION}
@syncodeindex pg cp
@comment %**end of header
@copying
This manual is for GNU Sample (version @value{VERSION}, @value{UPDATED}),
which is an example in the Texinfo documentation.

Copyright @copyright{} 2016 Free Software Foundation, Inc.

@quotation
Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3 or
any later version published by the Free Software Foundation; with no
Invariant Sections, with no Front-Cover Texts, and with no Back-Cover
Texts.  A copy of the license is included in the section entitled
``GNU Free Documentation License''.
@end quotation
@end copying

@dircategory Texinfo documentation system
@direntry
* sample: (sample)Invoking sample.
@end direntry

@titlepage
@title GNU Sample
@subtitle for version @value{VERSION}, @value{UPDATED}
@author A.U. Thor (@email{bug-sample@@gnu.org})
@page
@vskip 0pt plus 1filll
@insertcopying
@end titlepage

@contents

@ifnottex
@node Top
@top GNU Sample

This manual is for GNU Sample (version @value{VERSION}, @value{UPDATED}).
@end ifnottex

@menu
* Invoking sample::
* GNU Free Documentation License::
* Index::
@end menu


@node Invoking sample
@chapter Invoking sample

@pindex sample
@cindex invoking @command{sample}

This is a sample manual.  There is no sample program to
invoke, but if there were, you could see its basic usage
and command line options here.


@node GNU Free Documentation License
@end knoten
@appendix GNU Free Documentation License

@include fdl.texi


@node Index
@unnumbered Index

@printindex cp

@bye
""", "k2", 65

SAMPLE_K3="""\\input texinfo   @c -*-texinfo-*-
@comment $Id@w{$}
@comment %**start of header
@include version.texi
@settitle GNU Sample @value{VERSION}
@syncodeindex pg cp
@comment %**end of header
@copying
This manual is for GNU Sample (version @value{VERSION}, @value{UPDATED}),
which is an example in the Texinfo documentation.

Copyright @copyright{} 2016 Free Software Foundation, Inc.

@quotation
Permission is granted to copy, distribute and/or modify this document
under the terms of the GNU Free Documentation License, Version 1.3 or
any later version published by the Free Software Foundation; with no
Invariant Sections, with no Front-Cover Texts, and with no Back-Cover
Texts.  A copy of the license is included in the section entitled
``GNU Free Documentation License''.
@end copying
@end quotation

@dircategory Texinfo documentation system
@direntry
* sample: (sample)Invoking sample.
@end direntry

@titlepage
@title GNU Sample
@subtitle for version @value{VERSION}, @value{UPDATED}
@author A.U. Thor (@email{bug-sample@@gnu.org})
@page
@vskip 0pt plus 1filll
@insertcopying
@end titlepage

@contents

@ifnottex
@node Top
@top GNU Sample

This manual is for GNU Sample (version @value{VERSION}, @value{UPDATED}).
@end ifnottex

@menu
* Invoking sample::
* GNU Free Documentation License::
* Index::
@end menu


@node Invoking sample
@chapter Invoking sample

@pindex sample
@cindex invoking @command{sample}

This is a sample manual.  There is no sample program to
invoke, but if there were, you could see its basic usage
and command line options here.


@node GNU Free Documentation License
@appendix GNU Free Documentation License

@include fdl.texi


@node Index
@unnumbered Index

@printindex cp

@bye
""", "k3", 20


SHORT_SAMPLE = """\\input texinfo
@settitle Sample Manual 1.0

@copying
This is a short example of a complete Texinfo file.

Copyright @copyright{} 2016 Free Software Foundation, Inc.
@end copying

@titlepage
@title Sample Title
@page
@vskip 0pt plus 1filll
@insertcopying
@end titlepage

@c Output the table of the contents at the beginning.
@contents

@ifnottex
@node Top
@top GNU Sample

This manual is for GNU Sample
(version @value{VERSION}, @value{UPDATED}).
@end ifnottex

@menu
* First Chapter::    The first chapter is the
                      only chapter in this sample.
* Index::            Complete index.
@end menu


@node First Chapter
@chapter First Chapter

@cindex chapter, first

This is the first chapter.
@cindex index entry, another

Here is a numbered list.

@enumerate
@item
This is the first item.

@item
This is the second item.
@end enumerate


@node Index
@unnumbered Index

@printindex cp

@bye
"""
SHORT_SAMPLE_EXPECTED = (11,
                         {'bye': 1,
                          'c': 1,
                          'chapter': 1,
                          'cindex': 2,
                          'contents': 1,
                          'copying': 1,
                          'end': 5,
                          'enumerate': 1,
                          'ifnottex': 1,
                          'insertcopying': 1,
                          'item': 2,
                          'menu': 1,
                          'node': 3,
                          'page': 1,
                          'printindex': 1,
                          'settitle': 1,
                          'title': 1,
                          'titlepage': 1,
                          'top': 1,
                          'unnumbered': 1,
                          'vskip': 1})
SHORT_SAMPLE_KLAMMERCMDS = sorted(['copying', 'enumerate', 'ifnottex',
                                   'menu', 'titlepage'])


if __name__ == '__main__':
    unittest.main()