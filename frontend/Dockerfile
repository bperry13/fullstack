FROM node:20-alpine
WORKDIR /app
COPY package*.json /app

RUN npm i --silent
# check react-scripts version in package.json
RUN npm i -g react-scripts@5.0.1

# copy the source code to the docker image
COPY . ./

#start node.js 
CMD ["npm", "start" ]
