# lua info

```
root@hr-client-aws-886d6c959-bplqs:/# lua -v
Lua 5.1.5  Copyright (C) 1994-2012 Lua.org, PUC-Rio
root@hr-client-aws-886d6c959-bplqs:/# luarocks --version
/usr/bin/luarocks 2.4.2
LuaRocks main command-line interface

root@hr-client-aws-886d6c959-bplqs:/# luarocks list

Installed rocks:
----------------

luasocket
   3.0.0-1 (installed) - /usr/local/lib/luarocks/rocks
```

# Run
```
./wrk -D exp -t 2 -c 2 -d 30 -L -s ./scripts/hotel-reservation/mixed-workload_type_1.lua http://frontend.default.svc.cluster.local:5000 -R 2
```