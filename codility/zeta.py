# Codility Zeta challenge
# https://codility.com/demo/take-sample-test/zeta2011/
def solution (A, K):
    dp = [(0, 0) for _ in A[0]] # (down, right)
    dp[0] = (K, 0)
    for row in A:
        balls_going_right = 0
        for i in range(len(dp)):
            if row[i] == 0:
                dp[i] = (dp[i][0], balls_going_right)
            if row[i] == -1:
                overall_balls = dp[i][0] + balls_going_right
                balls_going_right = overall_balls / 2
                dp[i] = (overall_balls - balls_going_right,
                         balls_going_right)
            elif row[i] == 1:
                overall_balls = dp[i][0] + balls_going_right
                balls_going_down = overall_balls / 2
                balls_going_right = overall_balls - balls_going_down
                dp[i] = (balls_going_down, balls_going_right)

    return dp[-1][0]

if __name__ == '__main__':
    print solution([[-1, 0, -1], [1, 0, 0]], 4) # should == 1
    print solution([[1]], 9) # should == 4
    print solution([[-1]], 9) # should == 5
