#################################################################################################
# Constants.
#################################################################################################

#################################################################################################
##### LIBRARIES #################################################################################
#################################################################################################


#################################################################################################
##### FUNCTIONS #################################################################################
#################################################################################################

def getChromList(x=True, y=True, m=True, reference=[]):
    """Returns a chromosome aliases list.

    Keyword arguments:
    x -- Wether the chrX will be present or not. (default True)
    y -- Wether the chrY will be present or not. (default True)
    m -- Wether the chrM will be present or not. (default True)
    reference -- List of dictionaries. The returned chromList will only contain entries that appear on any of these dictionaries.

    Returns:
    chromList -- List of chromosome aliases.
    """

    if(not reference): # Creating basic chromosome list
        chromList = ["chr"+str(e) for e in range(1,23)]
        if(x): chromList.append("chrX")
        if(y): chromList.append("chrY")
        if(m): chromList.append("chrM")
    else: # Filtering by reference
        chromList = []
        for n in [str(e) for e in range(1,23)] + ["X","Y","M"]:
            appears = False
            for d in reference:
                if("chr"+n in d.keys()):
                    appears = True
                    break
            if(appears): chromList.append("chr"+n)
    return chromList


