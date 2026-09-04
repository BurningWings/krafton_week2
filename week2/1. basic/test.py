def fibonacci(n):
    # TODO: 재귀를 이용해 n번째 피보나치 수를 반환하세요.
    if n==0 or n==1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def is_palindrome(s : str):
    # TODO: 알파벳/숫자만 추출하여 소문자로 변환 후 회문 여부를 반환하세요.
    db = []
    s= s.lower()
    for i in range(len(s)):
         if s[i].isalnum():
              db.append(s[i])
    db_1 =db[::-1]
    return db_1==db
    
def rotate_matrix_90(matrix):
    # TODO: N x N 배열을 시계방향으로 90도 회전한 새 배열을 반환하세요.
    n = len(matrix)
    result_1=[]
    for i in range(n):
        arr=[]
        for j in range(n):
            arr.append(0)              
        result_1.append(arr)

    
    for i in range(n):
        for j in range(n):
            result_1[j][n-i-1] = matrix[i][j]
    return result_1
def print_matrix(matrix):
    """배열을 보기 좋게 출력하는 헬퍼 함수"""
    for arr in matrix:
        print(arr)
    

def find_two_sum_pairs(nums, target):
    num = len(nums)
    p = []
    for i in range(num):
        for j in range(i+1,num):
            if nums[i]+nums[j]==target:
                p.append((i,j))
    return p




for i in range(5):
        result = fibonacci(i)
        print(f"fib({i}) = {result}")

users = "Mad!am"
result = is_palindrome(users)
print(result)

users = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
result = rotate_matrix_90(users)
print(print_matrix(result))

users = [2, 7, 11, 15]
target1 = 9
result = find_two_sum_pairs(users,target1)
print(result)
