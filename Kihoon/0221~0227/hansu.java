package feb21_27_newbie;

/*
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 
등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. 
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 
첫째 줄에 1,000보다 작거나 같은 자연수 N이 주어진다.

첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.
*/
//한수 개념부터 잘 몰라서 풀이 보면서 함

import java.util.Scanner;

public class hansu {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int cnt = 0;
		
			if(N<100) {
				cnt=N;
			}
			else{
				cnt =99;
				for(int i=100; i<=N; i++) {
					int hun = i/100; 
					int ten = (i/10) % 10;
					int one = i -( (hun*100) + (ten*10));
					
					if(hun-ten == ten-one) {
						cnt++;
					}
				}
			}
		
			System.out.println(cnt);
		}
}

