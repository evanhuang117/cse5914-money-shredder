import '../style/Content.css';
import fakeData from '../fake_data.json';
import React from "react";
import axios from 'axios';

class Content extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      items :fakeData, 
      // queued : "",
      budget:"",
      showTable:'none'
    };

    this.handleChange.bind(this);
    this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    const target = event.target;
    const value = target.value;
    const name = target.name;

    axios.get("http://localhost:7000/search_all", {
        params: {}
    }).then((data)=>{
      const data_ = JSON.parse(JSON.stringify(data.data.hits.hits));
      console.log('data_ = ', data_);
    });

    this.setState({
      showTable:"block",
      [name]: value
    });
    this.getItems();
    event.preventDefault();
  }

  handleChange(event) {
    const target = event.target;
    const value = target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
    // alert(String(this.state.budget))
  }
  getItems() {
    var rowData = this.state.items;
    var data = rowData.filter((number) => number.price < parseInt(this.state.budget));
    const rows = [];
    for(var i = 0; i < data.length; i++){
      const row = [];
      row.push(<th scope = "row">{i+1}</th>);
      row.push(<td><a href="www.osu.edu">{data[i].item}</a></td>);
      row.push(<td>${data[i].price}</td>);
      rows.push(
          <tr>
            {row}
          </tr>
      );
    }
    if(rows==null) return <tr></tr>
    return rows;
  }
  render() {
    return (
      <div id = "content">
        <div class="container">
          <form onSubmit={(event) => this.handleSubmit(event)}>
            <div class="row">
                <div class="col input-group">
                  <label class="input-group-text">Budget</label>
                  <input type="text" class="form-control" id="budget" name = "budget" placeholder="Enter budget" value = {this.state.budget} onChange={(event) => this.handleChange(event)}/>
                  {/* <input type="text" class="form-control" id="budget" name = "budget" placeholder="Enter budget" /> */}
                </div>
                <div class="col input-group">
                  <label class="input-group-text">Category</label>
                  <select class="form-select">
                    <option>food</option>
                    <option>beverage</option>
                    <option>health & beauty</option>
                    <option>home essentials</option>
                    <option>other</option>
                  </select>
                </div>
                <div class="col">
                  <label class="form-label"> </label>
                  <button type="submit" class="btn btn-primary">Submit</button>
                </div>
              </div>
          </form>
        </div>
        <div class = "container ps-4 mt-5" style={{display:this.state.showTable}}>
          <div class="row" id="mainListContainer">
            <div class="col-md-8 table-responsive">
              <table class="table table-striped">
                <thead>
                  <tr>
                    <th scope="col">Rank</th>
                    <th scope="col">Name</th>
                    <th scope="col">Price</th>
                  </tr>
                </thead>
                <tbody>
                  {this.getItems()}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
      
    );
  }



}

export default Content;
