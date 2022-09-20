// const utils = require("./utils");

const express = require("express");
const app = express();
const port = 7000;

const cors = require('cors');

const corsOptions ={
    origin:'http://localhost:3000',
    credentials:true,
    optionSuccessStatus:200
}


app.use(cors(corsOptions));

// set access port
app.use(express.json());
app.listen(port, () => {
  console.log(`RUN http://localhost:${port}`);
});

'use strict'

const {Client} = require('@elastic/elasticsearch')
const client = new Client({ node: 'http://localhost:9200'})


app.get('/update_data', (req, res) => {

	async function run () {
	  await client.index({
	    index: 'game-of-thrones',
	    document: {
	      character: 'Ned Stark',
	      quote: 'Winter is coming.'
	    }
	  })

	  await client.indices.refresh({ index: 'game-of-thrones' })}

  run();
});

app.get('/search', (req, res) => {

async function run () {
  const result= await client.search({
    index: 'game-of-thrones',
    query: {
      match: { quote: 'winter' }
    }
  })
  console.log(result.hits.hits);
  const log_st_qu = result.hits.hits[0]['_source']['quote'];
  const log_st_cha = result.hits.hits[0]['_source']['character'];
  res.send(log_st_qu + log_st_cha);

}
  run();

});

app.get('/es', (req, res) => {

	async function run () {
	  // Let's start by indexing some data
	  await client.index({
	    index: 'game-of-thrones',
	    document: {
	      character: 'Ned Stark',
	      quote: 'Winter is coming.'
	    }
	  })

	  await client.index({
	    index: 'game-of-thrones',
	    document: {
	      character: 'Daenerys Targaryen',
	      quote: 'I am the blood of the dragon.'
	    }
	  })

	  // here we are forcing an index refresh, otherwise we will not
	  // get any result in the consequent search
	  await client.indices.refresh({ index: 'game-of-thrones' })

	  // Let's search!
	  const result= await client.search({
	    index: 'game-of-thrones',
	    query: {
	      match: { quote: 'winter' }
	    }
	  })

	  console.log(result.hits.hits);
	  const log_st_qu = result.hits.hits[0]['_source']['quote'];
	  const log_st_cha = result.hits.hits[0]['_source']['character'];
	  res.send(log_st_qu + log_st_cha);
}

run();

});


// // default display
// app.get('/', (req, res) => {
//     res.send('Hello World!');
//   });
