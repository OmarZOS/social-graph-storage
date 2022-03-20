# Social graph storage

 This repository holds the storage component inside of the phoros project, it is mainly consisted of a data listening functionality, an indexing functionality, a database deployment files, wrappers and a server to provide inserted data.

## Getting started:

#### Databases:

##### - Nebula Database:

    cd databases-config/nebula/ & docker-compose up -d

##### - Elasticsearch engine:

    cd ../databases-config/elasticsearch/ & docker-compose up -d

#### Social Storage server:

    docker-compose up -d

## Progress:

 - [ ] Nebula graph database. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/70)
   - [x] Deployment.
   - [x] Wrapper files.
 - [x] Elasticsearch engine. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/80)
   - [x] Deployment.
   - [x] Wrapper files.
 - [ ] Current code consistency. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/69)
   - [x] Listening to data providers.
     - Rabbitmq.
   - [ ] Serving data.
     - [x] Basic server functionality.
     - [ ] Advanced query handling.
   - [x] Data formats. 
      - NetworkX json graph.
 - [x] Indexing. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/75)
   - [x] Simple indexing.
   - [ ] Semantic indexing. (for more details, visit my repository [semantic-social-grapher](https://github.com/OmarZOS/semantic-social-grapher)) 
     -  Twitter.
 - [x] Containerisation ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/90)
   - [x] Light footprint.
   - [x] Automation of deployment.

## Dependencies:
   - This component is supposed to listen to canals through a broker (rabbitmq in this case), therefore, it is imperative to deploy a broker or else the listening process will crash. 
   - Keep in mind that every node/edge **must** have a field "other":(user|tweet|post...) like the following examples: *"other":"user"* , "other":"friends_with". 

