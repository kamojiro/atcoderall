package main

import "fmt"

func main() {
	var N, ans int
	var now int
	fmt.Scan(&N)
	A := make([]int, N)
	for i := 0; i < N; i++ {
		fmt.Scan(&A[i])
	}
	for i := 1; i < 40; i++ {
		now = 1
		for j := 0; j < N; j++ {
			if A[j]%2 == 0 {
				A[j] /= 2
			}else{
				now = 0
				break
			}
		}
		if now == 0 {
			break
		}else{
			ans = i
		}
	}
	fmt.Println(ans)
}
