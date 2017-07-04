#
# htmlStripper.py
#
#  Sample code for stripping HTML markup tags and scripts from
#  HTML source files.
#
# Copyright (c) 2006, 2016, Paul McGuire
#
from contextlib import closing
import urllib.request, urllib.parse, urllib.error
from cPyparsing import (makeHTMLTags, SkipTo, commonHTMLEntity, replaceHTMLEntity,
    htmlComment, anyOpenTag, anyCloseTag, LineEnd, OneOrMore, replaceWith)

scriptOpen,scriptClose = makeHTMLTags("script")
scriptBody = scriptOpen + SkipTo(scriptClose) + scriptClose
commonHTMLEntity.setParseAction(replaceHTMLEntity)

# get some HTML
targetURL = "http://wiki.python.org/moin/PythonDecoratorLibrary"
with closing(urllib.request.urlopen( targetURL )) as targetPage:
    targetHTML = targetPage.read().decode("UTF-8")

# first pass, strip out tags and translate entities
firstPass = (htmlComment | scriptBody | commonHTMLEntity |
             anyOpenTag | anyCloseTag ).suppress().transformString(targetHTML)

# first pass leaves many blank lines, collapse these down
repeatedNewlines = LineEnd() + OneOrMore(LineEnd())
repeatedNewlines.setParseAction(replaceWith("\n\n"))
secondPass = repeatedNewlines.transformString(firstPass)

print(secondPass)
