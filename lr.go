package main

import (
  "fmt"
  "io/ioutil"
  "os"
  "os/exec"
  "regexp"
)


var indexed int = 0//used for counting the file
//not used just a custom test function
func execute(command string) string {
  command_output, err := exec.Command(command).Output()
  if err != nil {
    ex := fmt.Errorf("%v", err)
    fmt.Println(ex)
    return "Error occured ->"
  } else {
    return string(command_output)
  }
}

func check(e error) {
  if e != nil {
    panic(e)
  }
}

func readfile(file_path string) string {
  databytes, err := ioutil.ReadFile(file_path)
  check(err)
  return string(databytes)
}

func finder(path string, target string) {
  files, err := ioutil.ReadDir(path)
  check(err)
  for _, file := range files {
    name := file.Name()
    if file.IsDir() {
      finder(path+"/"+name, target)
    } else {
      //fmt.Println(file.Name())
      target_set, err := regexp.MatchString(target, readfile(path+"/"+name))
      check(err)
      if(target_set == true){
        fmt.Println("File->", file.Name(), "Present in file:", target_set)
        indexed = indexed + 1
      }
    }
  }
}

  func main() {
    //files,err := ioutil.ReadDir("/tmp/")
    //check(err)
    // for _,file := range files{
    //fmt.Println(file.Name(), file.IsDir())
    //}

    target := os.Args[2]
    path := os.Args[1]
    if(path == ""){
      fmt.Println("Enter path and target")}
    finder(path, target)
    if(indexed == 0){
      fmt.Println("Found in None of the files in the path")}
    //current_data := readfile("/tmp/coo")
    //re, err := regexp.Compile("umang")
    //check(err)
    //match := re.FindStringIndex(current_data)
    //fmt.Println(match)
  }
