import Filter from "../components/Filter";
import React from "react";
import axios from "axios";
import fakeData from "../fake_data.json";
import "../style/Content.css";
class Content extends React.Component {


  constructor(props) {
    super(props);
    this.state = {
      fullLists: null,
      items: null,
      // queued : "",
      budget: "",
      showTable: 'none'
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }



  handleSubmit(event) {
    const target = event.target;
    const value = target.value;
    const name = target.name;
    this.setState({
      showTable: "block",
      [name]: value,
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
      .then((data) => {
        const data_ = JSON.parse(JSON.stringify(data.data.hits.hits));
        this.setState({
          fullLists: data_,
          items: data_
        });
      });
  }

  getItems() {
    var rowData = this.state.fullLists;
    var data = rowData.filter((data) => (data._source.price.amount / data._source.price.divisor) < parseInt(this.state.budget));
    this.setState({
      items: data
    });
    //   return (
    //   <div className="row mb-2">
    //   {this.state.items.map((item)=>(
    //     <div className="col ">
    //     <div className="card rounded-4" style={{ width: "auto" }}>
    //       <img
    //         className="card-img-top img-top"
    //         src={item._source.images[0].url}
    //         alt="Card image cap"
    //       />
    //       <div className="card-body">
    //         <h5 className="card-title">{item._source.title}</h5>
    //         <p className="card-text">{item._source.description}</p>
    //         <a className="btn btn-primary">{item._index}</a>
    //       </div>
    //     </div>
    //   </div>
    //   ))}
    // </div>)
  }

  render() {
    if (this.state.fullLists == null) {
      return (<h1> Loading </h1>)
    } else {
      return (

        <div className="content">
          {/*SEARCH BAR*/}
          <div className="container mb-3 mt-3">
            <nav className="navbar justify-content-center">
              <form
                className="form-inline"
                onSubmit={(event) => this.handleSubmit(event)}
              >
                <div className="input-group">
                  <input
                    className="form-control mr-sm-2"
                    type="search"
                    placeholder="Search"
                    aria-label="Search"
                  />
                  <button
                    className="btn btn-outline-success my-2 my-sm-0"
                    type="submit"
                  >
                    Search
                  </button>
                </div>
              </form>
            </nav>
          </div>
          {/*FILETERS*/}
          <div className="container" id="result">
            <div className="row">
              {/* Display Filters on the left and results on the right */}
              <div className="col-3">
                {/* Filters */}
                <ul className="filter-container">
                  <div className="column">
                    <Filter label="Budget" />
                    <div class="col input-group">
                      <label class="input-group-text">Budget</label>
                      <input
                        type="text"
                        class="form-control"
                        id="budget"
                        name="budget"
                        placeholder="Enter budget"
                        value={this.state.budget}
                        onChange={(event) => this.handleChange(event)}
                      />
                      {/* <input type="text" class="form-control" id="budget" name = "budget" placeholder="Enter budget" /> */}
                    </div>
                  </div>
                  <Filter label="Category" />
                  <Filter label="Date" />
                  <Filter label="Stars" />
                </ul>
              </div>
              {/* Results */}
              <div className="col-9">
                <div className="row mb-2">
                  {this.state.items.map((item) => (
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
              </div>
            </div>
          </div>
        </div>

      );
    }
  }
}
export default Content;
