FROM node:20-alpine
WORKDIR /app
COPY package*.json /app

RUN npm i --silent
# check react-scripts version in package.json
RUN npm i -g react-scripts@5.0.1

COPY . ./

CMD ["npm", "start" ]
