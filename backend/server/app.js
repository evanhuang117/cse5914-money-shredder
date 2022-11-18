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
// const client = new Client({ node: "http://0.0.0.0:9200/" });

app.get("/search_all", (req, res) => {
  async function run() {
    const result = await client.search(
      {
        index: "ebay",
        from: 0,
        body: {
          size: 5,
          query: {
            match_all: {},
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
    return res.send(result);
  }
  run();
});

app.post("/search_by_price", (req, res) => {
  // var price = req.body.price;
  var gte = req.body.gte;
  var lte = req.body.lte;

  console.log('gte = ', gte, 'lte = ', lte);
  async function run() {
    const result = await client.search(
      {
        index: "ebay",
        from: 0,
        body: {
          query: {
            range: {
              price: {
                gte: gte,
                lte: lte,
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
    // const log_st_qu = result.hits.hits[0]["_source"]["title"];
    // const log_st_cha = result.hits.hits[0]["_source"]["price"];
    // res.send(log_st_qu + log_st_cha);
    return res.send(result);
  }
  run();
});

app.post("/search_by_keyword", (req, res) => {
  var keyword = req.body.keyword;
  console.log('keyword = ', keyword);
  // var keyword = 'Taco';

  async function run() {
    const result = await client.search(
      {
        index: "ebay",
        from: 0,
        body: {
          size: 20,
          query: {
            multi_match: {
              query: keyword,
              fields: ["title"],
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
    res.send(result);
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
