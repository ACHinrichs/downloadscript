config = {};

config["email"]={};

lectures=[["DSAL Uebungen", # Name
           b"<a href=\"\/Lehre\/SS17\/DSA\/Uebung\d+.pdf", #REG_FINDSTRING
           b"<a href=\"\/Lehre\/SS17\/DSA\/", # REG_SUBSTRING
           r"http://algo.rwth-aachen.de/Lehre/SS17/DSA/", # URL_MATERIALS
           r"http://algo.rwth-aachen.de/Lehre/SS17/DSA.php", # URL_LECTURENOTES
           r"out/" #OUT DIR
],
          ["DSAL Vorlesungen", # Name
           b"<a href=\"\/Lehre\/SS17\/DSA\/v\d+.pdf", #REG_FINDSTRING
           b"<a href=\"\/Lehre\/SS17\/DSA\/", # REG_SUBSTRING
           r"http://algo.rwth-aachen.de/Lehre/SS17/DSA/", # URL_MATERIALS
           r"http://algo.rwth-aachen.de/Lehre/SS17/DSA.php", # URL_LECTURENOTES
           r"out/" #OUT DIR
          ],
          ["DSAL Globaluebungen", # Name
           b"<a href=\"\/Lehre\/SS17\/DSA\/Loesung-Tutoraufgaben\d+.pdf", #REG_FINDSTRING
           b"<a href=\"\/Lehre\/SS17\/DSA\/", # REG_SUBSTRING
           r"http://algo.rwth-aachen.de/Lehre/SS17/DSA/", # URL_MATERIALS
           r"http://algo.rwth-aachen.de/Lehre/SS17/DSA.php", # URL_LECTURENOTES
           r"out/" #OUT DIR
          ]
]
