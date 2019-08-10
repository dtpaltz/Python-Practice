



def isRotation(s1, s2):
    n = len(s1)
    # /* Check that sl and s2 are equal length and not empty*/
    if n == s2.length() and n > 0:
        # /* Concatenate sl and sl within new buffer */
        return s2 in ''.join([s1, s1])
    return False



