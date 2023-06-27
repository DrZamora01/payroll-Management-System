% rebase('layout.tpl', title='department')

<h3>Department: {{dept}}</h3>

<p>
<table class="table">
  <thead>
    <tr>
      <th>Emp ID</th>
      <th>Name</th>
      <th>Wage</th>
      <th>Hrs Worked</th>
      <th>Weekly Pay</th>
    </tr>
  </thead>
  <tbody>
    % for row in rows:
      <tr align="center">
        % for col in row:
          <td>{{col}}</td>
        % end
      </tr>
    % end
  </tbody>
</table>
</p>