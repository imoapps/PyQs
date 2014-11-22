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
    tile_area = (float(tile_length)* float(tile_width))/144
    #get the amount of tile needed , raw data
    tile_amount = floor_area/tile_area

    # add 1 tile per 75 squarefeet  of area
    extra = floor_area/75
    extra=round(extra)
    tile_amount = tile_amount+extra
       
    # return raw data
    return (length,width,floor_area,tile_amount)

# generate a floor report

def floorReport ():    
    length,width,flr_area,tileAmount=area() # call to area function 
     # tidying up  the data
    flr_area=round(flr_area,2)
    tileAmount = int(round(tileAmount))

    #final output    
    print "\n\t Length of area : {} feet.\n\
                Width of area : {} feet.\n \
                Area calculated : {} square feet \n\
                Amount of Tiles required for the job : {} each ".format(length,
                                                                                            width,flr_area,tileAmount)

floorReport()

##............................>>>>>>> END
## MORE TO COME

