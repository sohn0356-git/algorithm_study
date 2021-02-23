Java

```java
package feb21_27_middle;
import java.util.Scanner;

public class star {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		
		for(int i=1; i<=a; i++) {
			for(int j=1; j<=a-i; j++) {
				System.out.print(" ");
			}
			 
			for(int k=0; k<2*i-1; k++) {
				System.out.print("*");
			}
			System.out.println();
		}
	}
}

```



Python

```python

n = input("숫자입력: ")
n=int(n)
s=0;

for i in range(1,n+1):
    print(' '*(n-i)+'*'*(2*i-1))
```

