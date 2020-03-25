
  
# Function to find mean. 
def mean(arr, n): 
      
    sum = 0
    for i in range(0, n): 
        sum = sum + arr[i] 
      
    return sum / n 
  
# Function to find covariance. 
def covariance(arr1, arr2, n): 
  
    sum = 0
    for i in range(0, n): 
        sum = (sum + (arr1[i] - mean(arr1, n)) *
                      (arr2[i] - mean(arr2, n))) 
      
    return sum / (n - 1) 
  
# Driver method 
arr1 = [65.21, 64.75, 65.26, 65.76, 65.96] 
n = len(arr1) 
  
arr2 = [67.25, 66.39, 66.12, 65.70, 66.64] 
m = len(arr2) 
  
if (m == n): 
    print (covariance(arr1, arr2, m)) 
  
# This code is contributed by Gitanjali. 