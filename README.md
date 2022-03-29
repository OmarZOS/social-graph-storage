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

 - [ ] Nebula graph database. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/75)
   - [x] Deployment.
   - [x] Wrapper files.
     - [x] Insertion.
     - [ ] Retrieval.
 - [x] Neo4J graph database. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/90)
   - [x] Deployment.
   - [x] Wrapper files.
     - [x] Insertion.
     - [ ] Retrieval.
 - [x] Elasticsearch engine. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/80)
   - [x] Deployment.
   - [x] Wrapper files.
     - [x] Insertion.
     - [ ] Retrieval.
 - [ ] Current code consistency. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/75)
   - [x] Listening to data providers.
     - Rabbitmq.
   - [ ] Serving data.
     - [x] Basic server functionality.
     - [x] Advanced query handling.
   - [x] Data formats. 
      - NetworkX json graph.
 - [x] Indexing. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/75)
   - [x] Simple indexing. (though not simplistic)
   - [ ] Semantic indexing. (for more details, visit my repository [semantic-social-grapher](https://github.com/OmarZOS/semantic-social-grapher)) 
 - [x] Containerisation ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/90)
   - [x] Light footprint.
   - [x] Automation of deployment.



>---
>  **NOTES:**
>   - This component is supposed to listen to canals through a broker (rabbitmq in this case), therefore, it is imperative to deploy a broker or else the listening process will crash. 
>   - Keep in mind that every node/edge **must** have a field "{node,edge}_type":{user,tweet,post,...} like the following examples: "`node_type`":"user" , "`edge_type`":"friends_with". 
>
>---
