## 1 alloc for each resource
~~~
 99.000%   27.31s 
 99.000%   27.00s 
 99.000%   26.89s 
 99.000%   26.89s 
 99.000%   26.94s 
~~~

## proportional alloc for each resource
~~~
allocation {'root--consul': 6.0, 'root--frontend': 6.0, 'root--geo': 6.0, 'root--jaeger': 6.0, 'root--memcached-profile': 6.0, 'root--memcached-rate': 6.0, 'root--memcached-reserve': 6.0, 'root--mongodb-geo': 3.0, 'root--mongodb-profile': 3.0, 'root--mongodb-rate': 3.0, 'root--mongodb-recommendation': 3.0, 'root--mongodb-reservation': 3.0, 'root--mongodb-user': 3.0, 'root--profile': 6.0, 'root--rate': 6.0, 'root--recommendation': 6.0, 'root--reservation': 6.0, 'root--search': 6.0, 'root--user': 6.0}

 99.000%   18.55s 
 99.000%   18.55s 
 99.000%   20.64s 
 99.000%   20.23s 
 99.000%   18.96s 
 99.000%   16.34s 
 99.000%   20.97s 
~~~

### axdev bayesian opt
~~~
 99.000%   13.60s 
 99.000%   13.09s 
 99.000%   11.32s 
~~~