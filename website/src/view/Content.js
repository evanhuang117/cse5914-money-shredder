import '../style/Content.css';
import React from "react";
class Content extends React.Component {

  constructor(props) {
    super(props);
    this.state = {items : "hi!", queued : ""};

    this.handleChange.bind(this);
    this.handleSubmit.bind(this);
  }

  handleSubmit(event) {
    //alert(String(this.state.queued));
    this.setState({items : String(this.state.queued)});
    event.preventDefault();
  }

  handleChange(event) {
    this.setState({queued : event.target.value})
  }

  render() {
    return (
      <div class="container" id = "Content">
        <div class="row">
            <div class="col-md-8">
                    <form onSubmit={(event) => this.handleSubmit(event)}>
                    <div class="row align-items-center" >
                        <div class="col input-group">
                          <label class="input-group-text">Budget</label>
                          <input type="text" class="form-control" id="budget" placeholder="Enter budget" onChange={(event) => this.handleChange(event)} name="budget"/>
                        </div>
                        <div class="col input-group">
                          <label class="input-group-text">Category</label>
                          <select class="form-select">
                            <option>1</option>
                            <option>2</option>
                            <option>3</option>
                            <option>4</option>
                          </select>
                        </div>
                        <div class="col">
                          <label class="form-label"> </label>
                          <button type="submit" class="btn btn-primary">Submit</button>
                        </div>
                    </div>
                    </form>
              </div>      
        </div>
        <div class= "row" id="mainListContainer">
            <div class="col-md-8">
              <table class="item-table">
                <tr>
                  <th>Rank</th>
                  <th>Name</th>
                  <th>Price</th>
                </tr>
                {this.getItems()}
              </table>
            </div>
        </div>
    </div>
    );
  }

  getItems() {
    const rows = [];
    for(var i = 0; i < this.state.items.length; i++){
        const row = [];
        row.push(<td>{i+1}</td>);
        row.push(<td><a href="www.osu.edu">{this.state.items[i]}</a></td>);
        row.push(<td>$10000</td>);
        rows.push(<tr>{row}</tr>);
    }
    return rows;
  }

}

export default Content;
