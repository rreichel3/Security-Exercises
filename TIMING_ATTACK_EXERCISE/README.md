##Exercise Summary:
The purpose of this exercise is to teach the student about timing attacks, how to execute them and why they are dangerous.  A side purpose is for the student to be challenged to think about everything from a security lens - even down to the password comparison mechanism. 
##Instructions:
1. The student should first have the Go runtime and python installed. (https://golang.org/doc/install)
2. Next the student should run the Go executable (provided in the git repository) which should start the server
3. From there, the student is free to explore the login mechanism. The correct password is “test” which can be derived using a simple python program. 
4. To develop a program first you’ll want to understand how the password comaprison is implemented: 
```
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
```

5. Develop a program that exploits the delays in the time to help determine what the password is.  You may need to step through and run the program multiple times to figure it out but it is doable! Example is provided in the github repo as timingBruteforce.py

