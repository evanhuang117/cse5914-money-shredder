import "../style/Category.css";

function Category() {
  return (
    <div className="category">
      <div className="search">
        <form id="searchbar" role="search">
          <input
            type="search"
            id="query"
            name="q"
            placeholder="Search..."
            aria-label="Search through site content"
          ></input>
          <button>Search</button>
        </form>
      </div>
      <div className="result"></div>
    </div>
  );
}

export default Category;
