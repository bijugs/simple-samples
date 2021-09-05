package main

import (
  "fmt"
  "net/http"
)

func main() {
        res, err := http.Head("http://storage/simple-samples.jar")
	if err != nil {
		fmt.Println(err)
	}
        fmt.Println(res)
	if res.StatusCode != 200 {
		fmt.Println("Error code")
	}
}
