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
	<img src="https://leetcode.gallerycdn.vsassets.io/extensions/leetcode/vscode-leetcode/0.18.1/1652090923340/Microsoft.VisualStudio.Services.Icons.Default" alt="Logo" height="120">
	</a>
<h3 align="center">LeetCode</h3>
<p align="center">
	All my solutions in one place.
	<br />
	<a href="https://github.com/Vaansh/leetcode"><strong>Explore the page »</strong></a>
	<br />
	<br />
</p>
</p>

<!-- TEAM MEMBERS -->

## Current Status

<!-- SOLUTIONS_START -->
    
<table style='width:100%; text-align:left;'>
<tr>
<th style='text-align:center;'>Language</th>
<th style='text-align:center;'>Number of Solutions</th>
</tr>
<tr>
<td>Python</td>
<td>      93</td>
</tr>
<tr>
<td>Java</td>
<td>      15</td>
</tr>
</table>
    
<!-- SOLUTIONS_END -->



## Adding Solutions

1. Add file name to directory with the solution directly from LeetCode submission.

Example:

```
$ touch "python/1. Two Sum"     # create python sol.
$ vi "python/1. Two Sum"        # add python sol.
$ vi "java/1. Two Sum"          # edit java sol.
```

2. Run the `sh scripts/add.sh` utility script to count number of solutions, rename to file name, format code, commit with appropriate message (ex: `<language> : added/updated/deleted solution for problem 0001`), and push to repository.

Example:

```sh
$ sh scripts/add.sh
------------------------------
Language   Number of Solutions
------------------------------
Python     2
Java       2
------------------------------
Renamed 'python/1. Two Sum' to '0001-two-sum.py'

$ git log
commit  <hash> (HEAD -> main, origin/main)
Author: <name> <email>
Date:   <timestamp>
    python: added solution for problem 0001

commit  <hash>
Author: <name> <email>
Date:   <timestamp>
    java: updated solution for problem 0001
```
