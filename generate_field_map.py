
import random

draw_chip = 0
# フィールドマップ作成
def generate_field_map():

    # 何マス塗ったか
    
    field_map = []

    for i in range(20):
        list_ = []

        for j in range(20):
            list_.append(0)

        field_map.append(list_)


    def box_3x3( x_b3 , y_b3 ):
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                field_map[ x_b3 + i ][ y_b3 + j ] = 1

    def box_5x5( x_b5 , y_b5 ):
        for i in [-2,-1,0,1,2]:
            for j in [-2,-1,0,1,2]:
                field_map[ x_b5 + i ][ y_b5 + j ] = 1

    # 初期位置
    x_gfm = random.randint(3,16)
    y_gfm = random.randint(3,16)

    ( x_gfm_start, y_gfm_start ) = ( x_gfm, y_gfm )


    # 塗るのみ
    def draw_map( x_branch, y_branch ):
        if x_branch <= 0 or x_branch >= 19 or y_branch <= 0 or y_branch >= 19:
            return

        if field_map[x_branch][y_branch] > 0:
            return

        field_map[x_branch][y_branch] = 1

    # 塗り拡げる
    def branch( x_branch, y_branch , count_branch ):

        if x_branch <= 0 or x_branch >= 19 or y_branch <= 0 or y_branch >= 19:
            return

        if field_map[x_branch][y_branch] > 0:
            return


        if True:
            field_map[x_branch][y_branch] = 1

            for x_random in [-1,0,1]:
                for y_random in [-1,0,1]:

                    if random.randint(0,10) <= 4 and count_branch <= 0:
                        continue

                    if x_random * y_random :
                        continue

                    if x_random == 0 and y_random == 0 :
                        continue

                    range_int = random.randint(4,5)

                    for i in range(range_int):
                        if i == range_int - 1:

                            branch(
                                x_branch + x_random * (i+1) , 
                                y_branch +  y_random * (i+1) ,
                                count_branch - 1
                            )

                            break

                        draw_map( x_branch +  x_random * (i+1) , y_branch +  y_random * (i+1) )

    # 実際に作る
    #box_5x5( x_gfm , y_gfm )

    branch( x_gfm , y_gfm , 2)



    return ( field_map, x_gfm_start, y_gfm_start )