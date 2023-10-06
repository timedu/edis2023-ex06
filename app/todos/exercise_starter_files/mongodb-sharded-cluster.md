
### 1. After starting the cluster, what services are running?


### 2. What roles do the services (nodes) play?

- In which nodes is the user's data stored?
- Which nodes, containing user data, form a replica set (give one of them)?
- Which nodes do clients connect to?


### 3. About the configuration 

- Which of the configuration files, in the scripts directory, initiate replica sets?
- What kind of information is given to the router during its initiation?


### 4. What response does mongosh give to the configuration server initialisation command?


### 5. What response does mongosh give to a shard initialisation command?


### 6. What response does mongosh give to the first command in the router initialisation script?


### 7. The response of the `sh.status()` command is divided into sections, one of which is *shardingVersion*. What other sections does the command response contain?


### 8. What commands should be run to get the following (see the specification) lines to print from `sh.status()`?


### 9. How many documents are there in the films collection after running the insert-many-films.js script?


### 10. How many film collection documents are in each shard?


### 11. Which shards contains drama films and how many?

