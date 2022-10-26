import "../style/Filters.css";
import moment from "moment";
import React, { useState } from "react";
import DateRangePicker from "react-bootstrap-daterangepicker";
import "bootstrap-daterangepicker/daterangepicker.css";

const Filter = (props) => {
  const [open, setOPen] = useState(false);
  /*toggle function*/
  const toggle = () => {
    setOPen(!open);
  };
  const handleEvent = (event, picker) => {
    console.log(picker.startDate);
  };
  return (
    <div>
      <div className="filter" onClick={toggle}>
        <h1 className="filter-name mb-0">{props.label}</h1>
        <div className="filter-button">+</div>
      </div>
      {open && props.label == "Budget" && (
        <div className="filter-list">
          <div className="single-filter">
            <input type="checkbox" />
            <h4>$1-10</h4>
          </div>
          <div className="single-filter">
            <input type="checkbox" />
            <h4>$10-50</h4>
          </div>
          <div className="single-filter">
            <input type="checkbox" />
            <h4>$101-150</h4>
          </div>
        </div>
      )}
      {open && props.label == "Category" && (
        <div className="filter-list">
          <div className="single-filter">
            <input type="checkbox" />
            <h4>Food</h4>
          </div>
          <div className="single-filter">
            <input type="checkbox" />
            <h4>Grocery</h4>
          </div>
          <div className="single-filter">
            <input type="checkbox" />
            <h4>Home</h4>
          </div>
          <div className="single-filter">
            <input type="checkbox" />
            <h4>Game</h4>
          </div>
        </div>
      )}
      {open && props.label == "Date" && (
        <div className="filter-list">
          <DateRangePicker
            onEvent={handleEvent}
            initialSettings={{ startDate: "1/1/2014", endDate: "3/1/2014" }}
          >
            <input type="text" className="form-control" />
          </DateRangePicker>
        </div>
      )}
      {open && props.label == "Stars" && (
        <div className="filter-list">
          <div className="single-filter">
            <input type="checkbox" />
            <h4>1</h4>
          </div>
          <div className="single-filter">
            <input type="checkbox" />
            <h4>2</h4>
          </div>
          <div className="single-filter">
            <input type="checkbox" />
            <h4>3</h4>
          </div>
          <div className="single-filter">
            <input type="checkbox" />
            <h4>4</h4>
          </div>
        </div>
      )}
    </div>
  );
};

export default Filter;
