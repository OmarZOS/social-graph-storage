<p align="center">
  <img src="https://nebula-graph.io/img/nav-nebula-logo.png"/>
  <br> English | <a href="README_zh-CN.md">中文</a>
  <br>A distributed, scalable, lightning-fast graph database<br>
</p>

There are multiple ways to deploy Nebula Graph, but using Docker Compose is usually considered to be a fast starter. This repository provides a convenient solution to deploy Nebula Graph with Docker Compose.

Choose a nebula-docker-compose branch before you start. The following table lists the most popular nebula-docker-compose branches and the corresponding Nebula Graph GitHub branches and versions.

For minor version of docker images(2.6.2 for instance), please check tags from the docker hub i.e. [here](https://hub.docker.com/r/vesoft/nebula-graphd/tags).


## Documentation:

### Launching:

    docker-compose up -d

### Getting access to the console host:
    
    # if it is a docker container:
    sudo docker exec -it nebula-console sh

### Running nGQL statements:

#### Statement mode:

    nebula-console -u root -p nebula --address graphd --port 9669 -e "some ngql statement" 

#### Script mode:
In order to run multiple queries, use the following instructions:

    nebula-console -u root -p nebula --address graphd --port 9669 -f filename.nGQL

##### Making a script:
    I have made a simple script *ngqlBuilder.py* to generate Node creation instructions (TAGS in nebula), the instrucitons are printed to the standard output. I have redirected them using pipes. 

#### Querying:
    MATCH (n:user)
    RETURN n;