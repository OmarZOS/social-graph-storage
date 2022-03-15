# Social graph storage

 This repository holds the storage component inside of the phoros project, it is mainly consisted of a data listening functionality, an indexing functionality, a database deployment files, wrappers and a server to provide inserted data.

## Getting started:

#### Databases:

##### Nebula Database:

    cd databases-config/nebula/ & docker-compose up -d

##### Elasticsearch engine:

    cd ../databases-config/elasticsearch/ & docker-compose up -d

#### social Storage server:

    docker-compose up -d

## Progress:

 - [ ] Nebula graph database. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/70)
   - [x] Deployment.
   - [x] Wrapper files.
 - [ ] Elasticsearch engine. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/40)
   - [x] Deployment.
   - [ ] Wrapper files.
 - [ ] Current code consistency. ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/20)
   - [x] Rabbitmq listening to data providers.
   - [ ] Serving data.
     - [x] Basic server functionality.
     - [ ] Mediation with databases.
     - [ ] Advanced query handling.


   - [ ] Semantic index. (for more details, visit my repository [semantic-social-indexer](https://github.com/OmarZOS/semantic-social-indexer)) ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/10)
     - [x] Twitter.
     - [ ] Facebook.
     - [ ] Youtube.
 - [ ] Containerisation ![](https://us-central1-progress-markdown.cloudfunctions.net/progress/90)
   - [x] Smaller fingerprint.
   - [ ] Automation of deployment.

## Dependencies:
   - This component is supposed to listen to canals through a broker (rabbitmq in this case), therefore, it is imperative to deploy a broker or else the listening process will crash 

