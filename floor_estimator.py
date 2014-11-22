def area ():
    # get the length and width of the area to be estimated from the user
    length = raw_input("Enter the Length of the Area to be estimated \n \
    in decimal running feet  :\n")
    width = raw_input("Enter the width :\n")

    # get the size of the tile to be used for the job
    tile_length = raw_input("Enter the length of the selected tile,\n \
    in decimal inches :\n")
    tile_width = raw_input("Enter the width of the selected tile,\n \
    in decimal inches :\n")
     # calculate data 
    floor_area = float(length) * float(width)
    tile_area = float(tile_length)* float(tile_width)

    tile_amount = floor_area/tile_area
    
    # return raw data
    return (length,width,floor_area,tile_amount)

# generate a floor report

def floorReport ():
    
    e,w,a,ta=area() # call to area function 
    e=round(e,2) # tidying up  the data 
    w=round(w,2)
    a=round(a,2)
    ta=round(ta)
    # add 2 extra tiles per 100 sqft of space
    test = a/100.
    print 'test {}'.format(test)
    #if a/100>1:
       # ta=int(ta)+2  # add t
    
    
    print "Length of area : {} feet.\n\
                Width of area : {} feet.\n \
                Area calculated : {} square meters \n\
                Amount of Tiles required for the job : {} each ".format(e,w,a,ta)

floorReport()


