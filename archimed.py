# mg = pgV
# m = pV 
WATER_DENSITY = 1000  


def is_floating(mass, submerged, density):
    
    archimedes = WATER_DENSITY * submerged
    
    
    return archimedes >= mass




if __name__ == "__main__":
    is_floating(50 , 100 , 5)