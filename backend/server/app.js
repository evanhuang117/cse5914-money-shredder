// const utils = require("./utils");

const express = require("express");
const app = express();
const port = 7001;

const cors = require("cors");

app.use(cors());
app.use(express.json());
app.listen(port, () => {
  console.log(`RUN http://localhost:${port}`);
});

("use strict");

const { Client } = require("@elastic/elasticsearch");

const client = new Client({ node: "http://elasticsearch:9200/" });

app.get("/search_all", (req, res) => {
  async function run() {
    const result = await client.search(
      {
        index: "ebay",
        size: 25,
        from: Math.floor(Math.random() * 100),
        query: {
          match_all: {},
        },
      },
      {
        ignore: [404],
        maxRetries: 3,
      }
    );

    console.log(result.hits.hits);
    console.log("end");
    const log_st_qu = result.hits.hits[0]["_source"]["product"];
    const log_st_cha = result.hits.hits[0]["_source"]["price"];
    // res.send(log_st_qu + log_st_cha);
    return res.send(result);
  }
  run();
});

app.get("/search_by_price", (req, res) => {
  // var quote = req.body.quote;
  // var gtr = req.body.gtr;
  // var lte = req.body.lte;

  async function run() {
    const result = await client.search(
      {
        index: "ebay",
        from: 0,
        body: {
          query: {
            range: {
              price: {
                gte: 100,
                lte: 1000,
                boost: 1.0,
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
    const log_st_qu = result.hits.hits[0]["_source"]["product"];
    const log_st_cha = result.hits.hits[0]["_source"]["price"];
    // res.send(log_st_qu + log_st_cha);
    return res.send(result);
  }
  run();
});

app.get("/search_by_type", (req, res) => {
  var quote = "c2";

  async function run() {
    const result = await client.search(
      {
        index: "ebay",
        from: 0,
        body: {
          query: {
            multi_match: {
              query: quote,
              fields: ["category"],
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
    const log_st_qu = result.hits.hits[0]["_source"]["product"];
    const log_st_cha = result.hits.hits[0]["_source"]["price"];
    res.send(log_st_qu + log_st_cha);
  }
  run();
});

app.get("/search_by_keyword", (req, res) => {
  var quote = "computer";

  async function run() {
    const result = await client.search(
      {
        index: "ebay",
        from: 0,
        body: {
          query: {
            multi_match: {
              query: quote,
              fields: ["product"],
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
    const log_st_qu = result.hits.hits[0]["_source"]["product"];
    const log_st_cha = result.hits.hits[0]["_source"]["price"];
    res.send(log_st_qu + log_st_cha);
  }
  run();
});

app.get("/es", (req, res) => {
  const products = [
    "soap",
    "computer",
    "bike",
    "moniter",
    "mouse",
    "phone",
    "keyborad",
    "shoes",
  ];
  const prices = [200, 500, 100, 200, 20, 1000, 100, 50];
  const category = ["c1", "c1", "c1", "c1", "c2", "c2", "c2", "c2"];

  async function run() {
    // Let's start by indexing some data

    let i = 0;
    while (i < products.length) {
      await client.index({
        index: "ebay",
        document: {
          product: products[i],
          price: prices[i],
          category: category[i],
        },
      });
      i++;
    }

    await client.indices.refresh({ index: "ebay" });

    // Let's search!
    // const result= await client.search({
    // 		index: 'ebay',
    // 		query: { match: { product: 'soap' }}
    // })

    // const result = await client.search({
    //     index: 'ebay',
    //     query: {
    //         dis_max: {
    //           queries: [
    //             {
    //               match: {
    //                 product: 'soap'
    //               }
    //             },
    //             {
    //               match: {
    //                 category: 'c1'
    //               }
    //             }
    //           ],
    //           tie_breaker: 0.3
    //         }
    //     }
    // })

    const result = await client.search({
      index: "ebay",
      query: {
        dis_max: {
          queries: [
            {
              match: {
                product: "soap",
              },
            },
            {
              match: {
                category: "c2",
              },
            },
          ],
          tie_breaker: 0.3,
        },
      },
    });

    console.log(result.hits.hits);
    const log_st_qu = result.hits.hits[0]["_source"]["product"];
    const log_st_cha = result.hits.hits[0]["_source"]["price"];
    res.send(log_st_qu + log_st_cha);
  }

  run();
});

// must search

// const response = await client.search({
//     index: 'ebay',
//     query: {
//       bool: {
//         must: {
//           match_all: {}
//         },
//         filter: {
//           term: {
//             status: 'active'
//           }
//         }
//       }
//     }
// })

// multiple condition search
// const result = await client.search({
//     index: 'ebay',
//     query: {
//         dis_max: {
//           queries: [
//             {
//               match: {
//                 product: 'soap'
//               }
//             },
//             {
//               match: {
//                 category: 'c1'
//               }
//             }
//           ],
//           tie_breaker: 0.3
//         }
//     }
// })
