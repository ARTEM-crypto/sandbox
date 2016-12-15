package main

import (
  "fmt"
  "strings"
  "time"
  "os"
)

func main() {
  var echo1Str, echo2Str, echo3Str, sep string
  echo1StartTime := time.Now()



  for i := 1; i < len(os.Args); i++ {
    echo1Str += sep + os.Args[i]
    sep = " "
  }
  fmt.Print("Echo1 result: " + echo1Str + ", it took ")
  echo1Time := time.Since(echo1StartTime).Seconds()
  fmt.Print(echo1Time)
  fmt.Println(" seconds")
  sep = ""



  echo2StartTime := time.Now()
  for _, arg := range os.Args[1:] {
    echo2Str += sep + arg
    sep = " "
  }
  fmt.Print("Echo2 result: " + echo2Str + ", it took ")
  echo2Time := time.Since(echo2StartTime).Seconds()
  fmt.Print(echo2Time)
  fmt.Println(" seconds")
  sep = ""


  echo3StartTime := time.Now()
  echo3Str = strings.Join(os.Args[1:], " ")
  fmt.Print("Echo3 result: " + echo3Str + ", it took ")
  echo3Time := time.Since(echo3StartTime).Seconds()
  fmt.Print(echo3Time)
  fmt.Println(" seconds")
}
