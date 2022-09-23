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

const client = new Client({ node: 'https://localhost:9200/',
                         auth: {
                                username: 'elastic',
                                password: 'Diyme7Yz_d2Rs*L4IVud'
                              },
                          tls: {
                                rejectUnauthorized: false
 },})

// elastic
// Diyme7Yz_d2Rs*L4IVud


app.get('/search_by_price', (req, res) => {

  // var quote = req.body.quote;
  // var gtr = req.body.gtr;
  // var lte = req.body.lte;

	async function run () {

	const result = await client.search(
      {
        index: 'ebay',
        from: 0,
        body: {
          query: {
            range: {
            	price : {
		          gte: 100,
		          lte: 1000,
              boost: 1.0
            	},
            },
          },
        },
      },
      {
        ignore: [404],
        maxRetries: 3,
      }
    );

	  console.log(result.hits.hits);
    console.log("end");
	  const log_st_qu = result.hits.hits[0]['_source']['product'];
	  const log_st_cha = result.hits.hits[0]['_source']['price'];
	  res.send(log_st_qu + log_st_cha);

	}
  run();

});


app.get('/search_by_keyword', (req, res) => {

  var quote = 'computer';

	async function run () {

	const result = await client.search(
      {
        index: 'ebay',
        from: 0,
        body: {
          query: {
            multi_match: {
              query: quote,
              fields: ["product"]
            },
          },
        },
      },
      {
        ignore: [404],
        maxRetries: 3,
      }
    );

	  console.log(result.hits.hits);
	  const log_st_qu = result.hits.hits[0]['_source']['product'];
	  const log_st_cha = result.hits.hits[0]['_source']['price'];
	  res.send(log_st_qu + log_st_cha);

	}
  run();

});


app.get('/es', (req, res) => {

	const products = ["soap", "computer", "bike",  "moniter", "mouse", "phone", "keyborad", "shoes"];
	const prices = [200, 500, 100, 200, 20, 1000, 100, 50];

	async function run () {
	  // Let's start by indexing some data

		let i = 0;
		while (i < products.length) {
			  await client.index({
			    index: 'ebay',
			    document: {
			      product: products[i],
			      price: prices[i]
			    }
			  })
		    i++;
		}

		await client.indices.refresh({ index: 'ebay' })

		// Let's search!
		const result= await client.search({
				index: 'ebay',
				query: { match: { product: 'soap' }}
		})

		console.log(result.hits.hits);
		const log_st_qu = result.hits.hits[0]['_source']['product'];
		const log_st_cha = result.hits.hits[0]['_source']['price'];
		res.send(log_st_qu + log_st_cha);
}

run();

});



// app.get('/update_data', (req, res) => {

//   var website = req.body.website;
//   var n_product = req.body.character;
//   var n_price = req.body.price;

//  async function run () {
//    await client.index({
//      index: website,
//      document: {
//        product: n_product,
//        price: n_price
//      }
//    })

//    await client.indices.refresh({ index: 'game-of-thrones' })
//  }

//   run();
// });