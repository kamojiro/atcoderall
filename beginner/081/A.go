package main

import "fmt"

func main() {
	var s string
	var ans int = 0
	fmt.Scan(&s)
	for _,t := range s{
		if t == '1'{
			ans += 1
		}
	}
	fmt.Println(ans)

}
