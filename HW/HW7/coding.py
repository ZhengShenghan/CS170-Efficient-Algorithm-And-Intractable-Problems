

if __name__ == '__main__':
    width, height = map(int, input().split())
    input_matrix = [[0 for i in range(width)]for j in range(height)]
    for i in range(height):
        input_matrix[i] = list(map(int, input().split()))
    jumps = list(map(int, input().split()))
    #jumps.insert(0, 0)
    jumps.append(0)
    len_jump = len(jumps)
    for i in range(len_jump):
        if jumps[i]>=width-1 & jumps[i]>= height-1:
            jumps = jumps[0:i]
    len_jump = len(jumps)
    dp = dict()
    dp[(0,0,0)] = input_matrix[0][0]
    det_row = 0 # if i + det_row > width not need to jump anymore 0 can jump
    det_col = 0 # 0 can jump, 1 can't jump
    det = 0
    det_break_jump = 0
    det_jump = 1
    mini = -1
    det_mini = 0
    for s in range(len_jump):
        det_row = 0
        if s==1:
            mini = dp[(height-1,width-1,0)]
            det_mini = 1
        if s>1:
            mini = min(mini,dp[height-1,width-1,s-1])
        #else:
            #mini = min(mini, dp[(i,j,s-1)])
        #else:

        if (det_jump == 0):
            break
        det_jump = 0
        for i in range(height):
            det_col = 0
            if i + jumps[s] + 1 > height - 1: # can't jump row for now
                det_row = 1
            for j in range(width):
                if j + jumps[s] + 1 > width - 1: # col can't jump for now
                    det_col = 1
                try:
                    dp[(i, j, s)] == -2
                except:
                    det = 1
                else:
                    if det_col == 1: # col can't jump
                        if det_row == 0: # row can jump
                            if j == width - 1: # col can't walk
                                # if i < height - jumps[s] - 1: # can jump
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
                                    det_jump = 1
                                else:
                                    if dp[(i+jumps[s]+1,j,s+1)] >= dp[(i,j,s)] + input_matrix[i+jumps[s]+1][j]:
                                        dp[(i+jumps[s]+1,j,s+1)] = dp[(i,j,s)] + input_matrix[i+jumps[s]+1][j]
                                        det_jump = 1
                            else: # col can walk
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
                                    dp[(i+jumps[s]+1,j,s+1)] == -2
                                except:
                                    dp[(i + jumps[s] + 1, j, s + 1)] = dp[(i, j, s)] + input_matrix[i + jumps[s] + 1][j]
                                    det_jump = 1
                                else:
                                    if dp[(i+jumps[s]+1,j,s+1)] >= dp[(i,j,s)] + input_matrix[i+jumps[s]+1][j]:
                                        dp[(i+jumps[s]+1,j,s+1)] = dp[(i,j,s)] + input_matrix[i+jumps[s]+1][j]
                                        det_jump = 1
                        else: # det_row = 1 row can't jump
                            if j == width - 1: # col can't walk
                                if i != height - 1: # row can walk
                                    try:
                                        dp[(i+1,j,s)] == -2
                                    except:
                                        dp[(i+1,j,s)] = dp[(i,j,s)] + input_matrix[i+1][j]
                                    else:
                                        dp[(i+1,j,s)] = min(dp[(i+1,j,s)],dp[(i,j,s)] + input_matrix[i+1][j])
                            else: # col can walk
                                if i != height - 1: # row can walk
                                    try:
                                        dp[(i+1,j,s)] == -2
                                    except:
                                        dp[(i+1,j,s)] = dp[(i,j,s)] + input_matrix[i+1][j]
                                    else:
                                        dp[(i+1,j,s)] = min(dp[(i+1,j,s)],dp[(i,j,s)] + input_matrix[i+1][j])
                                    try:
                                        dp[(i, j + 1, s)] == -2
                                    except:
                                        dp[(i, j + 1, s)] = dp[(i, j, s)] + input_matrix[i][j + 1]
                                    else:
                                        dp[(i, j + 1, s)] = min(dp[(i, j + 1, s)],
                                                                dp[(i, j, s)] + input_matrix[i][j + 1])
                                else: # row can't walk

                                    try:
                                        dp[(i,j+1,s)] == -2
                                    except:
                                        dp[(i,j+1,s)] = dp[(i,j,s)] + input_matrix[i][j+1]
                                    else:
                                        dp[(i,j+1,s)] = min(dp[(i,j+1,s)],dp[(i,j,s)] + input_matrix[i][j+1])

                    else: # det_col = 0, col can jump
                        if det_row == 0:# row can jump
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
                                det_jump = 1
                            else:
                                if dp[(i + jumps[s] + 1,j,s+1)] >= dp[(i, j, s)] + input_matrix[i + jumps[s] + 1][j]:
                                    dp[(i + jumps[s] + 1, j, s + 1)] = dp[(i, j, s)] + input_matrix[i + jumps[s] + 1][j]
                                    det_jump = 1
                            try:
                                dp[(i, j + jumps[s] + 1, s + 1)] == -2
                            except:
                                dp[(i, j + jumps[s] + 1, s + 1)] = dp[(i, j, s)] + input_matrix[i][j+ jumps[s] + 1]
                                det_jump = 1
                            else:
                                if dp[(i, j + jumps[s] + 1, s + 1)] >= dp[(i, j, s)] + input_matrix[i][j + jumps[s] + 1]:
                                    dp[(i, j + jumps[s] + 1, s + 1)] = dp[(i, j, s)] + input_matrix[i][j + jumps[s] + 1]
                                    det_jump = 1
                        else: # det_row = 1  row can't jump
                            if i == height - 1:  # row can't walk
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
                                    det_jump = 1
                                else:
                                    if dp[(i, j + jumps[s] + 1, s + 1)] >= dp[(i, j, s)] + input_matrix[i][j + jumps[s] + 1]:
                                        dp[(i, j + jumps[s] + 1, s + 1)] = dp[(i, j, s)] + input_matrix[i][j + jumps[s] + 1]
                                        det_jump = 1
                            else:  # row can walk
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
                                    dp[(i, j + jumps[s] + 1, s + 1)] == -2
                                except:
                                    dp[(i, j + jumps[s] + 1, s + 1)] = dp[(i, j, s)] + input_matrix[i][j+ jumps[s] + 1]
                                    det_jump = 1
                                else:
                                    if dp[(i, j + jumps[s] + 1, s + 1)] >= dp[(i, j, s)] + input_matrix[i][j + jumps[s] + 1]:
                                        dp[(i, j + jumps[s] + 1, s + 1)] = dp[(i, j, s)] + input_matrix[i][j + jumps[s] + 1]
                                        det_jump = 1

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