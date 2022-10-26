import Filter from "../components/Filter";
import React from "react";
import axios from "axios";
import fakeData from "../fake_data.json";
import "../style/Content.css";
class Content extends React.Component {
  constructor(props) {
    super(props);

    this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    event.preventDefault();
    console.log("gang");
    axios
      .get("http://localhost:7001/search_all", {
        params: {},
      })
      .then((data) => {
        const data_ = JSON.parse(JSON.stringify(data.data.hits.hits));
        console.log("data_ = ", data_);
      });
  }

  render() {
    return (
      <div className="content">
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
        <div className="container" id="result">
          <div className="row">
            {/* Display Filters on the left and results on the right */}
            <div className="col-3">
              {/* Filters */}
              <ul className="filter-container">
                <Filter label="Budget" />
                <Filter label="Category" />
                <Filter label="Date" />
                <Filter label="Stars" />
              </ul>
            </div>
            <div className="col-9">
              {/* Results */}
              <div className="row mb-3">
                <div className="col ">
                  <div className="card rounded-4" style={{ width: "auto" }}>
                    <img
                      className="card-img-top img-top"
                      src={require("../img/coffee.jpeg")}
                      alt="Card image cap"
                    />
                    <div className="card-body">
                      <h5 className="card-title">Product Name</h5>
                      <p className="card-text">Description</p>
                      <a className="btn btn-primary">Amazon</a>
                    </div>
                  </div>
                </div>
                <div className="col ">
                  <div className="card rounded-4" style={{ width: "auto" }}>
                    <img
                      className="card-img-top img-top"
                      src={require("../img/coffee.jpeg")}
                      alt="Card image cap"
                    />
                    <div className="card-body">
                      <h5 className="card-title">Product Name</h5>
                      <p className="card-text">Description</p>
                      <a className="btn btn-primary">Amazon</a>
                    </div>
                  </div>
                </div>
              </div>
              <div className="row mb-2">
                <div className="col ">
                  <div className="card rounded-4" style={{ width: "auto" }}>
                    <img
                      className="card-img-top img-top"
                      src={require("../img/coffee.jpeg")}
                      alt="Card image cap"
                    />
                    <div className="card-body">
                      <h5 className="card-title">Product Name</h5>
                      <p className="card-text">Description</p>
                      <a className="btn btn-primary">Amazon</a>
                    </div>
                  </div>
                </div>
                <div className="col ">
                  <div className="card rounded-4" style={{ width: "auto" }}>
                    <img
                      className="card-img-top img-top"
                      src={require("../img/coffee.jpeg")}
                      alt="Card image cap"
                    />
                    <div className="card-body">
                      <h5 className="card-title">Product Name</h5>
                      <p className="card-text">Description</p>
                      <a className="btn btn-primary">Amazon</a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
export default Content;
