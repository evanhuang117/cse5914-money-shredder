import "../style/Filters.css";
import React from "react";
import Filter from "../components/Filter";
class Filters extends React.Component {
  render() {
    return (
      <div className="left-container">
        <ul className="filter-container">
          <Filter label="Budget" />
          <Filter label="Category" />
          <Filter label="Date" />
          <Filter label="Stars" />
        </ul>
      </div>
    );
  }
}

export default Filters;
