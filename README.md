# go-rename-import

**Stability: alpha**

A small utility to rewrite Go imports. Ever found yourself afraid of moving directories in the source tree because you did not want to rewrite imports manually in hundreds of files? Well, let's put robots at work.

## Requirements

* Python 3

## Running

```
$ ./main.py <source_dir> <old_name> <new_name>
```

Example:

```diff
$ ./main.py ./sample "calls" "domain/core/calls"
./sample/server/main.go (8982 -> 9030)
--- /tmp/tmp4epnvub_	2018-05-21 12:31:32.528787091 +0300
+++ /tmp/tmp0vokc09_	2018-05-21 12:31:32.529787103 +0300
@@ -1,10 +1,10 @@
 package main
 
 import (
-	"calls/gate"
-	"calls/tracker"
-	"calls/tracker/driver"
-	_ "calls/tracker/driver/postgres"
+	"domain/core/calls/gate"
+	"domain/core/calls/tracker"
+	"domain/core/calls/tracker/driver"
+	_ "domain/core/calls/tracker/driver/postgres"
 	//"clients/beacon"
 	//"clients/beacon/redis"
 	"config"
```

Demo: https://asciinema.org/a/Ui7DrP5BZvvNVknR5zskxdyCD
