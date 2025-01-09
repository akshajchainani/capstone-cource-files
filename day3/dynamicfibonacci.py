def fibo(n):
    dp = [0] * (n + 1)  # Initialize the dp array
    dp[1] = 1  # Base case: F(1) = 1
  
    for i in range(2, n + 1):  # Start from index 2
        dp[i] = dp[i - 1] + dp[i - 2]  # Compute Fibonacci value for dp[i]
    
    return dp[n]  # Return the nth Fibonacci number
  
n = 3
print(f"Fibonacci of {n}:", fibo(n))
