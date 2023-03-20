from math import radians, cos, sin, asin, sqrt

def compute_distance(lat1, lat2, lon1, lon2):
	"""
    A function to compute the distance between two points on earth 
    given their coordinates, based on the Haversine Formula.
    """

	# Radius of earth in kilometers.
	R = 6371

	lat1, lat2, lon1, lon2 = [radians(el) for el in [lat1, lat2, lon1, lon2]]
	
	# Haversine formula
	dlon = lon2 - lon1
	dlat = lat2 - lat1
	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

	c = 2 * asin(sqrt(a))
	
	
	return(c * R)