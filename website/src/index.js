import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min";
import Filters from "./view/Filters";
import Header from "./view/Header";
import Footer from "./view/Footer";
import reportWebVitals from "./reportWebVitals";
import Content from "./view/Content";
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <div>
      <Header /> {/* Display Header */}
      <Content />
      {/* Display SearchBar */}
      {/* <SearchBar />  */}
      {/* <div className="filters-and-results"> */}
        {/* Display Filters on the left and results on the right */}
        {/* <Filters /> */}
        {/* <Results /> */}
      {/* </div> */}
      <Footer />
    </div>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
