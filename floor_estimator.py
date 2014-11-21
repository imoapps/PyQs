def area (l , w):
    area= l * w
    return area()
w = 15.5
l = 21.25
living_area = l * w
w = 4.58
l = 8.75
verandah_area = l * w
w = 5
l = 10
laundry_area = l * w
w = 1.16
l = 4.33
less = l * w
w = 15.5
l = 21.25
radius1 = 2.5
radius2 = 3.67

step_area = (22/7)*(radius2 *2)
total_area= living_area+verandah_area+laundry_area+step_area - less
tile_length= 24/12 ##input("Enter Tile Length: "  )
tile_area = tile_length*tile_length
tile_amount = total_area/tile_area
tile_per_box = 12
boxes = tile_amount/tile_per_box

print (total_area,tile_amount,boxes )
