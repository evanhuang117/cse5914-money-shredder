import Filter from "../components/Filter";
import React from "react";
import axios from "axios";
import fakeData from "../fake_data.json";
import "../style/Content.css";
class Content extends React.Component {


  constructor(props) {
    super(props);
    this.state = {
      items : null, 
      // queued : "",
      budget:"",
      showTable:'none'
    };
    this.handleChange=this.handleChange.bind(this);
    this.handleSubmit= this.handleSubmit.bind(this);
  }

 
  
  handleSubmit(event) {
    const target = event.target;
    const value = target.value;
    const name = target.name;
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

  componentDidMount() {
    axios.get("http://localhost:7001/search_all")
      .then((data)=>{
        const data_ = JSON.parse(JSON.stringify(data.data.hits.hits));
        this.setState({
          items: data_
        });
    });
  }

  getItems() {
    var rowData = this.state.items;
    var data = rowData.filter((data) => (data._source.price.amount/data._source.price.divisor) < parseInt(this.state.budget));
    console.log(data);
    const rows = [];
    for(var i = 0; i < data.length; i++){
      const row = [];
      row.push(<th scope = "row">{i+1}</th>);
      row.push(<td><a href={data[i]._source.url}>{data[i]._source.title}</a></td>);
      row.push(<td>${data[i]._source.price.amount/data[i]._source.price.divisor}</td>);
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
    if (this.state.items == null){
      return ( <h1> Loading </h1>)
    }
    else{return (
      <div id = "content">
        <div class="container">
          <form onSubmit={(event) => this.handleSubmit(event)}>
            <div class="row">
                <div class="col input-group">
                  <label class="input-group-text">Budget</label>
                  <input type="text" class="form-control" id="budget" name = "budget" placeholder="Enter budget" value = {this.state.budget} onChange={(event) => this.handleChange(event)}/>
                  {/* <input type="text" class="form-control" id="budget" name = "budget" placeholder="Enter budget" /> */}
                </div>
              </div>
              <div className="row mb-2">
                {this.state.items.map((item)=>(
                  <div className="col ">
                  <div className="card rounded-4" style={{ width: "auto" }}>
                    <img
                      className="card-img-top img-top"
                      src={item._source.images[0].url}
                      alt="Card image cap"
                    />
                    <div className="card-body">
                      <h5 className="card-title">{item._source.title}</h5>
                      <p className="card-text">{item._source.description}</p>
                      <a className="btn btn-primary">{item._index}</a>
                    </div>
                  </div>
                </div>
                ))}
              </div>
          </form>
        </div>
      </div>
      
    );}  
  }
}
export default Content;
