package main

import (
	"fmt"
	"io"
	"io/ioutil"
	"net/http"
	"os"
	"time"
	"path/filepath"
)

func main()  {
	start := time.Now()
	ch := make(chan string)
	filepath := filepath.Dir(os.Args[0]) + "/fetchall_data/data.txt"
	file, _ := os.OpenFile(filepath, os.O_APPEND|os.O_WRONLY, 0600)

	for _, url := range os.Args[1:] {
		go fetch(url, ch) // start a gorutine
	}
	for range os.Args[1:] {
		info := <-ch
		fmt.Print(info) // receive from channel ch
		io.WriteString(file, info)
	}
	fininfo := fmt.Sprintf("%.2fs elapsed\n", time.Since(start).Seconds())
	fmt.Print(fininfo)
	io.WriteString(file, fininfo)
	file.Close()
}

func fetch(url string, ch chan<- string)  {
	start := time.Now()
	resp, err := http.Get(url)
	if err != nil {
		ch <- fmt.Sprintln(err) // send to channel ch
		return
	}

	nbytes, err := io.Copy(ioutil.Discard, resp.Body)
	resp.Body.Close()
	if err != nil {
		ch <- fmt.Sprintf("while reading %s: %v\n", url, err)
		return
	}
	secs := time.Since(start).Seconds()
	ch <- fmt.Sprintf("%.2fs %7d %s\n", secs, nbytes, url)
}
