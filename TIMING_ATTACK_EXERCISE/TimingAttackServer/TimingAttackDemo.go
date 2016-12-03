package main

import (
    "log"
    "net/http"
    "html/template"
    "time"
)

var loggedInTemplate, _ = template.ParseFiles("loggedin.html")
var accessDeniedTemplate, _ = template.ParseFiles("accessDenied.html")

func handleRoot(w http.ResponseWriter, r *http.Request) {
    if r.Method == "GET" {
        t, _ := template.ParseFiles("root.html")
        t.Execute(w, nil)
    } else {
        http.Error(w, "Invalid request method.", 405)
    }
}
func comparePasswords(s1, s2 string) bool{
    if len(s1) != len(s2) {
        return false
    }
    time.Sleep(1 * time.Millisecond)
    for i := 0; i < len(s1); i++ {
        if s1[i] != s2[i] {
            return false
        }
        time.Sleep(1 * time.Millisecond)
    }
    return true

}

func handleLogin (w http.ResponseWriter, r *http.Request) {
    if r.URL.Path != "/login" {
            http.NotFound(w, r)
            return
        }

    if r.Method == "POST" {
        r.ParseForm()
        if r.FormValue("username") == "admin" {
            if comparePasswords(r.FormValue("password"), "test") {
                loggedInTemplate.Execute(w, nil)  
            } else {
                accessDeniedTemplate.Execute(w, nil)  
            }
        }
    } else {
        http.Error(w, "Invalid request method.", 405)
    }
}

func main() {
    http.HandleFunc("/", handleRoot)
    http.HandleFunc("/login", handleLogin)

    log.Fatal(http.ListenAndServe("0.0.0.0:8080", nil))
}