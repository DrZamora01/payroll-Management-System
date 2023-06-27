% rebase('layout.tpl', title='edit hours')


  <h2>Edit Employee Hours</h2>

  <form action="/editHours" method="post">
    
      <label for="eid">Employee ID:</label>
      <input type="text"  id="eid" name="eid" placeholder="employee ID">

    <br>

      <label for="hrs">Hours Worked:</label>
      <input type="text"  id="hrs" name="hrs" placeholder="Enter new hours worked">
   


    <button type="submit" class="btn btn-primary" value="Submit">Submit</button>
  </form>

