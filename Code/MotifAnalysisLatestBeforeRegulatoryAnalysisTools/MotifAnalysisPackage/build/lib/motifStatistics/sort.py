#################################################################################################
# Functions to sort data in various formats.
#################################################################################################

#################################################################################################
##### LIBRARIES #################################################################################
#################################################################################################

import operator

#################################################################################################
##### FUNCTIONS #################################################################################
#################################################################################################

def sortBedDictionary(coordDict, field=0):
    """Sorts a bed dictionary by a given field.

    Keyword arguments:
    coordDict -- Dictionary of bed entries.
    field -- Number of the field in which the sort will be based. Start (and default) from 0 (pos1 field).

    Returns:
    sortedDict -- Sorted dictionary
    """
    # Sorting bed lists
    sortedDict = dict()
    for c in coordDict.keys():
        sortedDict[c] = sorted(coordDict[c],key=operator.itemgetter(field))
    return sortedDict

def sortTableRowsByCol(table, col=0, order="asc"):
    """Sorts a table's rows by a certain column value.

    Keyword arguments:
    table -- Table to be sorted.
    col -- Number of the column to perform the sort
    order -- Order of the sorting. asc = ascendent, desc = descendent.

    Returns:
    sortedTable -- Sorted dictionary
    """
    # Sorting bed lists
    sortedTable = sorted(table,key=operator.itemgetter(col))
    if(order == "asc"): return sortedTable
    else: return sortedTable[::-1]

def sortListByReference(unsortedList,referenceList):
    """Sorts a list based on a reference list

    Keyword arguments:
    unsortedList -- Unsorted list.
    referenceList -- Reference list.

    Returns:
    sortedList -- Sorted list based on reference.
    """
    # Sorting list based on reference
    sortedList = []
    for e in referenceList:
        if(e in unsortedList): sortedList.append(e)
    return sortedList


