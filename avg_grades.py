Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def avg_grades(g1,g2,g3):
	"""(number,number,number)->number
        return the average of the grades:g1,g2,g3

        >>>avg_grades(90,80,70)
        70.00
        """
	return float((g1+g2+g3)/3)
