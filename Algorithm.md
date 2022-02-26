# Algorithm 

## LEC 1

### Multiply

#### 1. x*y :from 0 add y times x

#### 2. normal method: O(n^2)

#### 3. Divide and conquer: O(n^log2(3))

![image-20211002152139616](C:\Users\Eric Zheng\AppData\Roaming\Typora\typora-user-images\image-20211002152139616.png)

#### 4.Gauss

![image-20211002152226742](C:\Users\Eric Zheng\AppData\Roaming\Typora\typora-user-images\image-20211002152226742.png)

![image-20211002152256540](C:\Users\Eric Zheng\AppData\Roaming\Typora\typora-user-images\image-20211002152256540.png)

### Euclid’s algorithm for greatest common divisor

![image-20211002151603390](C:\Users\Eric Zheng\AppData\Roaming\Typora\typora-user-images\image-20211002151603390.png)

## LEC 2

### Fibonacci

#### Fast Matrix Powering

|1 1| Fn        =            Fn+1  

|1 0|Fn-1                    Fn

### Master theorem

T(n)=aT(n/b)+c*n^d

T(n) = O(n^d) if d > logba

​			O(n^dlogn) if d = logba

​			O(n^logba) if d<logba

## LEC 3

#### matrix multiplication

1.O(n^3)

![image-20211002154121305](C:\Users\Eric Zheng\AppData\Roaming\Typora\typora-user-images\image-20211002154121305.png)

#### FFT(nlogn)

#### Cross Correlation(successive dot product)