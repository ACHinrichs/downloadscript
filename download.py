import downloadscript.downloadscript as ds
print("Fetching Uebungunen for DSAL=========")

ds.REG_FINDSTRING  = b"<a href=\"\/Lehre\/SS17\/DSA\/Uebung\d+.pdf"
ds.REG_SUBSTRING   = b"<a href=\"\/Lehre\/SS17\/DSA\/"
ds.URL_MATERIALS   = r"http://algo.rwth-aachen.de/Lehre/SS17/DSA/"
ds.URL_LECTURENOTES= r"http://algo.rwth-aachen.de/Lehre/SS17/DSA.php"
ds.OUT_DIR     = r"Uebungen/"
ds.download()
print("Fetching Vorlesungen================")

ds.REG_FINDSTRING  = b"<a href=\"\/Lehre\/SS17\/DSA\/v\d+.pdf"
ds.REG_SUBSTRING   = b"<a href=\"\/Lehre\/SS17\/DSA\/"
ds.URL_MATERIALS   = r"http://algo.rwth-aachen.de/Lehre/SS17/DSA/"
ds.URL_LECTURENOTES= r"http://algo.rwth-aachen.de/Lehre/SS17/DSA.php"
ds.OUT_DIR     = r"Vorlesungen/"
ds.download()
