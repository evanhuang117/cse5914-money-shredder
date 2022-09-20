import '../style/Content.css';
function Content() {
  return (
    <div class="container" id = "Content">
      <div class="row">
            <div class="col-md-8">
                  <div class="row align-items-center" >
                    <div class="col input-group">
                      <label class="input-group-text">Budget</label>
                      <input type="text" class="form-control" id="budget" placeholder="Enter budget" name="budget"/>
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
            </div>      
      </div>
  </div>
  );
}

export default Content;
