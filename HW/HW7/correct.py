

if __name__ == '__main__':
    width, height = map(int, input().split())
    input_matrix = [[0 for i in range(width)]for j in range(height)]
    for i in range(height):
        input_matrix[i] = list(map(int, input().split()))
    jumps = list(map(int, input().split()))
    #jumps.insert(0, 0)
    jumps.append(0)
    len_jump = len(jumps)
    dp = dict()
    dp[(0,0,0)] = input_matrix[0][0]
    det_row = 0 # if i + det_row > width not need to jump anymore
    det_col = 0 # 0 can jump, 1 can't jump
    det = 0
    for s in range(len_jump):
        det_row = 0
        for i in range(height):
            det_col = 0
            for j in range(width):
                try:
                    dp[(i, j, s)] == -2
                except:
                    det = 1
                else:
                    if det_col == 0:
                        if j == width - 1: # can't walk
                            if i < height - jumps[s] - 1: # can jump
                                try:
                                    dp[(i+1,j,s)] == -2
                                except:
                                    dp[(i+1,j,s)] = dp[(i,j,s)] + input_matrix[i+1][j]
                                else:
                                    dp[(i+1,j,s)] = min(dp[(i+1,j,s)],dp[(i,j,s)] + input_matrix[i+1][j])
                                try:
                                    dp[(i+jumps[s]+1,j,s+1)] == -2
                                except:
                                    dp[(i + jumps[s] + 1, j, s + 1)] = dp[(i, j, s)] + input_matrix[i + jumps[s] + 1][j]
                                else:
                                    dp[(i+jumps[s]+1,j,s+1)] = min(dp[(i+jumps[s]+1,j,s+1)],dp[(i,j,s)] + input_matrix[i+jumps[s]+1][j])
                            else: # can't jump but can walk
                                if i != height - 1:
                                    try:
                                        dp[(i + 1, j, s)] == -2
                                    except:
                                        dp[(i + 1, j, s)] = dp[(i, j, s)] + input_matrix[i+1][j]
                                    else:
                                        dp[(i + 1, j, s)] = min(dp[(i + 1, j, s)], dp[(i, j, s)] + input_matrix[i+1][j])
                        if j < width - jumps[s] - 1: # can jump
                            if j == width - jumps[s] - 2:
                                det_col = 1
                            if i < height - jumps[s] - 1: # can jump
                                try:
                                    dp[(i+1,j,s)] == -2
                                except:
                                    dp[(i+1,j,s)] = dp[(i,j,s)] + input_matrix[i+1][j]
                                else:
                                    dp[(i+1,j,s)] = min(dp[(i+1,j,s)],dp[(i,j,s)] + input_matrix[i+1][j])
                                try:
                                    dp[(i,j+1,s)] == -2
                                except:
                                    dp[(i,j+1,s)] = dp[(i,j,s)] + input_matrix[i][j+1]
                                else:
                                    dp[(i,j+1,s)] = min(dp[(i,j+1,s)],dp[(i,j,s)] + input_matrix[i][j+1])
                                try:
                                    dp[(i + jumps[s] + 1, j, s + 1)] == -2
                                except:
                                    dp[(i + jumps[s] + 1, j, s + 1)] = dp[(i, j, s)] + input_matrix[i + jumps[s] + 1][j]
                                else:
                                    dp[(i + jumps[s] + 1, j, s + 1)] = min(dp[(i + jumps[s] + 1, j, s + 1)],
                                                                           dp[(i, j, s)] + input_matrix[i + jumps[s] + 1][
                                                                               j])
                                try:
                                    dp[(i, j + jumps[s] + 1, s + 1)] == -2
                                except:
                                    dp[(i, j + jumps[s] + 1, s + 1)] = dp[(i, j, s)] + input_matrix[i][j + jumps[s] + 1]
                                else:
                                    dp[(i, j + jumps[s] + 1, s + 1)] = min(dp[(i, j + jumps[s] + 1, s + 1)],dp[(i, j, s)] + input_matrix[i][j + jumps[s] + 1])
                            if i == height - 1: # can't walk
                                try:
                                    dp[(i, j + 1, s)] == -2
                                except:
                                    dp[(i, j + 1, s)] = dp[(i, j, s)] + input_matrix[i][j + 1]
                                else:
                                    dp[(i, j + 1, s)] = min(dp[(i, j + 1, s)], dp[(i, j, s)] + input_matrix[i][j + 1])
                                try:
                                    dp[(i, j + jumps[s] + 1, s + 1)] == -2
                                except:
                                    dp[(i, j + jumps[s] + 1, s + 1)] = dp[(i, j, s)] + input_matrix[i][j + jumps[s] + 1]
                                else:
                                    dp[(i, j + jumps[s] + 1, s + 1)] = min(dp[(i, j + jumps[s] + 1, s + 1)],
                                                                           dp[(i, j, s)] + input_matrix[i][
                                                                               j + jumps[s] + 1])
                            if (i < height - 1)&(i >= height - jumps[s] - 1): #can walk
                                try:
                                    dp[(i + 1, j, s)] == -2
                                except:
                                    dp[(i + 1, j, s)] = dp[(i, j, s)] + input_matrix[i + 1][j]
                                else:
                                    dp[(i + 1, j, s)] = min(dp[(i + 1, j, s)], dp[(i, j, s)] + input_matrix[i + 1][j])
                                try:
                                    dp[(i,j+1,s)] == -2
                                except:
                                    dp[(i,j+1,s)] = dp[(i,j,s)] + input_matrix[i][j+1]
                                else:
                                    dp[(i,j+1,s)] = min(dp[(i,j+1,s)],dp[(i,j,s)] + input_matrix[i][j+1])
                                try:
                                    dp[(i, j + jumps[s] + 1, s + 1)] == -2
                                except:
                                    dp[(i, j + jumps[s] + 1, s + 1)] = dp[(i, j, s)] + input_matrix[i][j + jumps[s] + 1]
                                else:
                                    dp[(i, j + jumps[s] + 1, s + 1)] = min(dp[(i, j + jumps[s] + 1, s + 1)],
                                                                           dp[(i, j, s)] + input_matrix[i][
                                                                               j + jumps[s] + 1])
                        if (j >= width - jumps[s] - 1) & (j < width - 1): # can't jump but can walk
                            if i < height - jumps[s] - 1:  # can jump
                                try:
                                    dp[(i + 1, j, s)] == -2
                                except:
                                    dp[(i + 1, j, s)] = dp[(i, j, s)] + input_matrix[i + 1][j]
                                else:
                                    dp[(i + 1, j, s)] = min(dp[(i + 1, j, s)], dp[(i, j, s)] + input_matrix[i + 1][j])
                                try:
                                    dp[(i, j + 1, s)] == -2
                                except:
                                    dp[(i, j + 1, s)] = dp[(i, j, s)] + input_matrix[i][j + 1]
                                else:
                                    dp[(i, j + 1, s)] = min(dp[(i, j + 1, s)], dp[(i, j, s)] + input_matrix[i][j + 1])
                                try:
                                    dp[(i + jumps[s] + 1, j, s + 1)] == -2
                                except:
                                    dp[(i + jumps[s] + 1, j, s + 1)] = dp[(i, j, s)] + input_matrix[i + jumps[s] + 1][j]
                                else:
                                    dp[(i + jumps[s] + 1, j, s + 1)] = min(dp[(i + jumps[s] + 1, j, s + 1)],
                                                                           dp[(i, j, s)] + input_matrix[i + jumps[s] + 1][
                                                                               j])
                            if i == height - 1:  # can't walk
                                try:
                                    dp[(i,j+1,s)] == -2
                                except:
                                    dp[(i,j+1,s)] = dp[(i,j,s)] + input_matrix[i][j+1]
                                else:
                                    dp[(i,j+1,s)] = min(dp[(i,j+1,s)],dp[(i,j,s)] + input_matrix[i][j+1])
                            if (i < height - 1)&(i >= height - jumps[s] - 1):  # can walk
                                try:
                                    dp[(i + 1, j, s)] == -2
                                except:
                                    dp[(i + 1, j, s)] = dp[(i, j, s)] + input_matrix[i + 1][j]
                                else:
                                    dp[(i + 1, j, s)] = min(dp[(i + 1, j, s)], dp[(i, j, s)] + input_matrix[i + 1][j])
                                try:
                                    dp[(i,j+1,s)] == -2
                                except:
                                    dp[(i,j+1,s)] = dp[(i,j,s)] + input_matrix[i][j+1]
                                else:
                                    dp[(i,j+1,s)] = min(dp[(i,j+1,s)],dp[(i,j,s)] + input_matrix[i][j+1])
                    if det_col == 1: # can't jump for now
                        if j == width - 1: # can't walk
                            if i < height - jumps[s] - 1: # can jump
                                try:
                                    dp[(i+1,j,s)] == -2
                                except:
                                    dp[(i+1,j,s)] = dp[(i,j,s)] + input_matrix[i+1][j]
                                else:
                                    dp[(i+1,j,s)] = min(dp[(i+1,j,s)],dp[(i,j,s)] + input_matrix[i+1][j])
                                try:
                                    dp[(i+jumps[s]+1,j,s+1)] == -2
                                except:
                                    dp[(i + jumps[s] + 1, j, s + 1)] = dp[(i, j, s)] + input_matrix[i + jumps[s] + 1][j]
                                else:
                                    dp[(i+jumps[s]+1,j,s+1)] = min(dp[(i+jumps[s]+1,j,s+1)],dp[(i,j,s)] + input_matrix[i+jumps[s]+1][j])
                            else: # can't jump but can walk
                                if i != height - 1:
                                    try:
                                        dp[(i + 1, j, s)] == -2
                                    except:
                                        dp[(i + 1, j, s)] = dp[(i, j, s)] + input_matrix[i+1][j]
                                    else:
                                        dp[(i + 1, j, s)] = min(dp[(i + 1, j, s)], dp[(i, j, s)] + input_matrix[i+1][j])

                        else: # can't jump but can walk
                            if i < height - jumps[s] - 1:  # can jump
                                try:
                                    dp[(i + 1, j, s)] == -2
                                except:
                                    dp[(i + 1, j, s)] = dp[(i, j, s)] + input_matrix[i + 1][j]
                                else:
                                    dp[(i + 1, j, s)] = min(dp[(i + 1, j, s)], dp[(i, j, s)] + input_matrix[i + 1][j])
                                try:
                                    dp[(i, j + 1, s)] == -2
                                except:
                                    dp[(i, j + 1, s)] = dp[(i, j, s)] + input_matrix[i][j + 1]
                                else:
                                    dp[(i, j + 1, s)] = min(dp[(i, j + 1, s)], dp[(i, j, s)] + input_matrix[i][j + 1])
                                try:
                                    dp[(i + jumps[s] + 1, j, s + 1)] == -2
                                except:
                                    dp[(i + jumps[s] + 1, j, s + 1)] = dp[(i, j, s)] + input_matrix[i + jumps[s] + 1][j]
                                else:
                                    dp[(i + jumps[s] + 1, j, s + 1)] = min(dp[(i + jumps[s] + 1, j, s + 1)],
                                                                           dp[(i, j, s)] + input_matrix[i + jumps[s] + 1][
                                                                               j])
                            if i == height - 1:  # can't walk
                                try:
                                    dp[(i,j+1,s)] == -2
                                except:
                                    dp[(i,j+1,s)] = dp[(i,j,s)] + input_matrix[i][j+1]
                                else:
                                    dp[(i,j+1,s)] = min(dp[(i,j+1,s)],dp[(i,j,s)] + input_matrix[i][j+1])
                            if (i < height - 1)&(i >= height - jumps[s] - 1):  # can walk
                                try:
                                    dp[(i + 1, j, s)] == -2
                                except:
                                    dp[(i + 1, j, s)] = dp[(i, j, s)] + input_matrix[i + 1][j]
                                else:
                                    dp[(i + 1, j, s)] = min(dp[(i + 1, j, s)], dp[(i, j, s)] + input_matrix[i + 1][j])
                                try:
                                    dp[(i,j+1,s)] == -2
                                except:
                                    dp[(i,j+1,s)] = dp[(i,j,s)] + input_matrix[i][j+1]
                                else:
                                    dp[(i,j+1,s)] = min(dp[(i,j+1,s)],dp[(i,j,s)] + input_matrix[i][j+1])
    # renew near element
    #for i in range(height):
    #    for j in range(width):

    mini = dp[(height-1,width-1,0)]
    for i in range(len_jump ):
        try:
            if mini > dp[(height-1,width-1,i)]:
                mini = dp[(height-1,width-1,i)]
        except:
            det = 0
    print(mini)