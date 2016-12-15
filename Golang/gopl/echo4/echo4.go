package main

import (
  "fmt"
  "os"
)

func main() {
  for index, arg := range os.Args[1:] {
    fmt.Print(index)
    fmt.Println(" - index, " + arg + " - value")
  }
}
