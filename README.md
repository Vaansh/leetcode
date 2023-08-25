<!--
**       .@@@@@@@*  ,@@@@@@@@     @@@     .@@@@@@@    @@@,    @@@% (@@@@@@@@
**       .@@    @@@ ,@@          @@#@@    .@@    @@@  @@@@   @@@@% (@@
**       .@@@@@@@/  ,@@@@@@@    @@@ #@@   .@@     @@  @@ @@ @@/@@% (@@@@@@@
**       .@@    @@% ,@@        @@@@@@@@@  .@@    @@@  @@  @@@@ @@% (@@
**       .@@    #@@ ,@@@@@@@@ @@@     @@@ .@@@@@@.    @@  .@@  @@% (@@@@@@@@
-->

<!-- PROJECT LOGO -->
<br />
<p align="center">
	<a href="https://github.com/Vaansh/leetcode">
	<img src="https://scontent.fyto3-1.fna.fbcdn.net/v/t39.30808-6/305317853_616467910000160_3824851731065368025_n.png?_nc_cat=100&ccb=1-7&_nc_sid=09cbfe&_nc_aid=0&_nc_ohc=0A9m31hDRnwAX_Q0ZUJ&_nc_ht=scontent.fyto3-1.fna&oh=00_AfBo1Nu6rypCrNCAhz8suqrxPV6X7Cgse5zwQIpNkFPowQ&oe=64EE885B" alt="Logo" height="120">
	</a>
<h3 align="center">LeetCode</h3>
<p align="center">
	All my solutionns.
	<br />
	<a href="https://github.com/Vaansh/leetcode"><strong>Explore the page »</strong></a>
	<br />
	<br />
</p>
</p>

<h5 align="center">Adding Solutions:</h5>

1. Add file name to directory with the solution directly from LeetCode submission.

Example:

```
$ touch "python/1. Two Sum"     # create python sol.
$ vi "python/1. Two Sum"        # add python sol.
$ vi "java/1. Two Sum"          # edit java sol.
.
.
```

2. Run the `sh scripts/add.sh` utility script to count number of solutions, rename to file name, commit with appropriate message (ex: `<language> : added/updated/deleted solution for problem 0001`), and push to repository.

Example:

```sh
$ sh scripts/add.sh
number of problems solved: 12
Renamed 'python/1. Two Sum' to '0001-two-sum.py'
Writing objects: 100% (6/6), 1.11 KiB | 1.11 MiB/s, done.
.
.
To https://github.com/Vaansh/leetcode.git
   <hash>  main -> main

$ git log
commit  <hash> (HEAD -> main, origin/main)
Author: <name> <email>
Date:   <timestamp>
    python: added solution for problem 0001

commit  <hash> (HEAD -> main, origin/main)
Author: <name> <email>
Date:   <timestamp>
    java: updated solution for problem 0001
```
