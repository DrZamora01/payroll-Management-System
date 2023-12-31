import sqlite3
from bottle import route, run, request, template, error


@route('/', method='GET')
def index():
    data = {'title': 'Welcome!'} 
    return template('welcome', data)   # show list of links

#@route('/login', method='POST')
#def login():
#    return template('login_page')  # assume login successful

@route ('/getDepartment', method = ['GET', 'POST'])
def department():

    if request.method == 'GET':
        return template('dept_form')
    else:
        dept = request.forms.get("dept")
        conn = sqlite3.connect("payroll.db") # Database
        cur = conn.cursor()

        sql = '''SELECT pay_data.emp_id, emp_name, wage, hrs_worked FROM employees JOIN 
        pay_data where pay_data.emp_id
       = employees.emp_id and employees.department = ?'''
        cur.execute(sql, (dept,))

        rows = cur.fetchall()
        cur.close()
        hrs = 0
        wage  = 0

        if rows:

            dataList = []
            for row in rows:
                eid, name, wage, hrs = row #unpack tuple
                if hrs <= 40:
                    payout = wage * hrs

                else:
                    ot_pay = (hrs - 40) * 1.5 * wage
                    payout =(wage * 40 ) + ot_pay

                emp = (eid, name, wage, hrs, payout)
                dataList.append(emp)

            data = {'rows': dataList, 'dept': dept}
            return template('show_department', data)
        else:   
           data ={ 'msg' : 'no such username'}
           return template ('status', data)



@route ('/editHours', method=['GET', 'POST'])  # update hours worked
def edit_hrs():
    if request.method == 'GET':
        return template('edit_hours')
    else:
        hrs = request.forms.get('hrs')  # post methods
        eid = request.forms.get('eid')

    try:
        conn = sqlite3.connect("payroll.db")
        cur = conn.cursor()

        sql1 = '''SELECT emp_id, emp_name, department FROM employees WHERE emp_id = ?'''
        cur.execute(sql1,(eid,))
        result = cur.fetchone()

        emp_id = result[0]
        emp_name = result[1]
        dept = result[2]

            # update hours worked
        sql2 = '''UPDATE pay_data SET hrs_worked = ? WHERE emp_id = ?'''
        cur.execute(sql2, (hrs, eid))
        if result:
           conn.commit()
           cur.close()
           return template('status', {'emp_id': emp_id, 'emp_name': emp_name, 'dept': dept, 'hrs': hrs})
            
    except:

            data = {'msg': 'Employee not found'}
            return template('status', data)

    finally:
            cur.close()
      

        
run(host='localhost', port=8080) 