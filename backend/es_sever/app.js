const utils = require("./utils");

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

// default display
app.get('/', (req, res) => {
    res.send('Hello World!');
  });

// set access API
app.get("/item_query", function(req, res) {
    const result = db.query('select * from Item');
    console.log('data: ', result);
    return res.send(result)
});


app.post("/depost_order", function(req, res) {
  var names = req.body.names;
  var quantity = req.body.quantity;
  var user_uid = req.body.user_uid;

  order_wait_name.push(names);
  order_wait_quantity.push(quantity);

  const uid_exist_flag = utils.check_uid(user_uid);
  if (uid_exist_flag == false){
    utils.set_up_user_order_table(user_uid);
  }
  exist_user_order = utils.check_user_order(user_uid);

  names.forEach((id_, index) => {
    const quan = quantity[index];
    var update_oder = quan + exist_user_order[id_];
    const result1 = db.query(`UPDATE Item_order SET quantity = ${update_oder} WHERE Id = ${id_} AND customerId = '${user_uid}';`);
    // console.log('depost_order 1: ', result1);
  });

  console.log('order_wait_name ', order_wait_name);
  console.log('order_wait_quantity: ', order_wait_quantity);
  return res.send('')

});
