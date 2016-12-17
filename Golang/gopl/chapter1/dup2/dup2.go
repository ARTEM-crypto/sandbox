package main

import (
  "bufio"
  "fmt"
  "os"
)

func main() {
  counts := make(map[string]int)
  files := os.Args[1:]
  dupfiles := make(map[int]string)

  if len(files) == 0 {
    countLines(os.Stdin, counts, "", dupfiles)
  } else {
    for _, arg := range files {
      f, err := os.Open(arg)
      if err != nil {
        fmt.Fprintf(os.Stderr, "dup2: %v\n", err)
        continue
      }
      countLines(f, counts, arg, dupfiles)
      f.Close()
    }
  }


  for line, n := range counts {
    if n > 1 {
      fmt.Printf("%d\t%s\n", n, line)
    }
  }
  fmt.Printf("%s\n%s", "Duplicated lines occours in flies:", dupfiles[1])
}

func countLines(f *os.File, counts map[string]int, filename string, dupfiles map[int]string) {
  input := bufio.NewScanner(f)
  dupCounter := 0
  for input.Scan() {
    if input.Text() == "" {
      break
    }
    line := input.Text()
    counts[line]++
    if counts[line] > 1 {
      dupCounter++
    }
    if dupCounter > 1 {
      dupfiles[1] += filename + "\n"
    }
  }
}
