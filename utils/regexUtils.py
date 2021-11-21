# -----------------------------------------------------------
# regexFunctions.py
# v.1.0
# Updated: 20211121
# ----------------------------------------------------------

"""
Collection of regex functions for searching patterns.
"""

import re

# -----------------------------------------------------------
# ISOLATE MATCHES ))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

def isolateMatch(stringText, searchPattern, replacePattern):
    """
    Function to find instances of a search pattern and only change specific ones.
    :param
        stringText:

        searchPattern:

        replacePattern:

    :return:
        [newString, numInstances, idxInstances]
    """
    # Search pattern to find.
    # Store number of instances that the pattern was found in string.
    numInstances = stringText.count(searchPattern)
    # Store length of search pattern string.
    lenPattern = len(searchPattern)

    # Store starting indices for each instance of found pattern in string.
    idxInstances = [_.start() for _ in re.finditer(searchPattern, stringText)]

    # If matches found.
    if len(idxInstances) > 0:
        # Store index for the right-most instance of found pattern.
        rIdxInstance = idxInstances[-1]

        # Compose new string.
        newString = stringText[:rIdxInstance] + replacePattern + stringText[(rIdxInstance + lenPattern):]

    else:
        newString = stringText

    return newString, numInstances, idxInstances

#************************************************************
# Function Test

text = "This string is a test of the isolateMatch function."
pattern = "is"
replace = "IIISSS"

found = isolateMatch(text, pattern, replace)
# Debug Log
print("New string: %s" % found[0])
print("# of Instances: %d" % found[1])
print("Indices of Instances: %s" % found[2])

# -----------------------------------------------------------
# ISOLATE MATCHES ))))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------