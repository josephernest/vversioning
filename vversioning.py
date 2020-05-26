#!/usr/bin/python3

"""
vversioning
===========
* detects the lines inside ==CHANGELOG== delimiters in files with extensions listed below (e.g. py, txt, js, c, cpp), or in such files inside ZIP archives
* lists the differences among these blocks in successive vetrsions

HOMEPAGE
https://github.com/josephernest/vversioning

USAGE
python vversioning.py           do it in current folder
python vversioning.py test/     do it in folder test/

==CHANGELOG==
* open encoding
* new project name
==CHANGELOG==
"""

FILEEXT = ['.txt', '.py', '.js', '.c', '.cpp']
ARCHIVEEXT = ['.zip']
import glob, zipfile, os, collections, re, sys
path = '.' if len(sys.argv) < 2 else sys.argv[1]
changes = collections.defaultdict(set)
for f in sorted(glob.glob(os.path.join(path, '*.*'))):
    if os.path.splitext(f)[1] in ARCHIVEEXT:
        z = zipfile.ZipFile(f, 'r')
        for g in z.namelist():
            if os.path.splitext(g)[1] in FILEEXT:
                changes[f].update([l for m in re.findall(r"^==CHANGELOG==(.*)^==CHANGELOG==", z.open(g).read().decode(), re.MULTILINE | re.DOTALL) for l in m.splitlines() if l != ''])
    elif os.path.splitext(f)[1] in FILEEXT:
        with open(f, 'r', encoding='utf8') as g:
            changes[f].update([l for m in re.findall(r"^==CHANGELOG==(.*)^==CHANGELOG==", g.read(), re.MULTILINE | re.DOTALL) for l in m.splitlines() if l != ''])
previous = set()
for f in sorted(changes.keys()):
    if changes[f] == set():
        continue
    print(f)
    print('\n'.join(changes[f] - previous))
    print("")
    previous = changes[f]
