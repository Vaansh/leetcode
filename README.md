# LeetCode

**Adding Solutions**

1. Add file name to directory with the solution directly from LeetCode submission. Example:

```
$ touch "1. Two Sum"
$ vi "1. Two Sum"
.
.
```

2. Run the `sh scripts/add.sh` utility script to count number of solutions, rename to file name, commit with appropriate message (ex: `added/updated/deleted solution for problem 0001`), and push to repository. Example:

```sh
$ sh scripts/add.sh
number of problems solved: 12
Renamed './1. Two Sum' to '0001-two-sum.py'
Writing objects: 100% (6/6), 1.11 KiB | 1.11 MiB/s, done.
.
.
To https://github.com/Vaansh/leetcode.git
   <hash>  main -> main

$ git log
commit  <hash> (HEAD -> main, origin/main)
Author: <name> <email>
Date:   <timestamp>
    added solution for problem 0001
```
