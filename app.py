from flask import Flask, render_template, request, redirect, url_for
import psycopg2
import ast

conn = None
cur = None
user = None
id = None

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/login', methods = ['POST'])
def login():
    global conn
    global cur
    global user
    global id
    if(conn is not None):
        conn.close()
    if(conn is not None):
        cur.close()
    user = request.form.get("userName")
    id = request.form.get("id")
    password = request.form.get("password")
    try:
        conn = psycopg2.connect(dbname = "dockwarehouse_mgt", user = user, password = password, host = "localhost")
    except:
        return render_template('error.html', data = {"message": "You are not authorized to access the database"})
    cur = conn.cursor()
    return redirect(url_for("select", data = {"user": user, "id": id}))


@app.route('/select')
def select():
    user = ast.literal_eval(request.args["data"])["user"]
    id = ast.literal_eval(request.args["data"])["id"]
    table = None
    if(user == 'po_products_mgr'):
        command1 = "select product_id, product_name from product where po_id = {}".format(id)
        command2 =  "select item_id, product_id, product_name, quantity, weight, dangerous_good, order_id from items natural join product where po_id = {}".format(id)
        command3 = "select po_id,po_name,po_street,po_city,po_state from purchasing_organization where po_id = {}".format(id)
        command4 = "select po_contact from purchasing_organization_po_contact where po_id = {}".format(id)
        command5 = "select location_id,l_street,l_city,l_state,type from location where po_id = {}".format(id)
        command6 = "select location_id,l_contact,type from  location natural join location_l_contact"
        cur.execute(command1)
        products = cur.fetchall()
        cur.execute(command2)
        items = cur.fetchall()
        cur.execute(command3)
        purchasing_organization = cur.fetchall()
        cur.execute(command4)
        purchasing_organization_po_contact = cur.fetchall()
        cur.execute(command5)
        location = cur.fetchall()
        cur.execute(command6)
        location_l_contact = cur.fetchall()
        return render_template('select.html', data = {"user": user, "id": id, "products": products, "items": items, "purchasing_organization": purchasing_organization, "purchasing_organization_po_contact":purchasing_organization_po_contact, "location":location, "location_l_contact":location_l_contact})
    elif(user == 'po_shipment_mgr'):
        command1 = "select product_id, product_name from product where po_id = {}".format(id)
        command2 = "select item_id, product_id, product_name, quantity, weight, dangerous_good, order_id from items natural join product where po_id = {}".format(id)
        command3 = "select order_id,alloted_date,dock,total_quantity,special_instrs,carrier_id,location_id from orders where po_id = {}".format(id)
        command4 = "select carrier_id,c_name,c_contact from carrier_c_contact natural join carrier"
        command5 = "select po_contact from purchasing_organization_po_contact where po_id = {}".format(id)
        command6 = "select location_id,l_street,l_city,l_state,type from location where po_id = {}".format(id)
        command7 = "select location_id,l_contact,type from  location natural join location_l_contact"
        command8 = "select carrier_id,c_name,c_street,c_city,c_state from carrier"
        command9 = "select po_id,po_name,po_street,po_city,po_state from purchasing_organization where po_id = {}".format(id)
        command10 = "select appointment_id,d_name,d_id,license_plate,proposed_date,status,d_contact,carrier_id from appointment where po_id = {} ".format(id)
        command11 = "select carrier_id,deadline from requests where po_id = {}".format(id)
        cur.execute(command1)
        products = cur.fetchall()
        cur.execute(command2)
        items = cur.fetchall()
        cur.execute(command3)
        orders = cur.fetchall()
        cur.execute(command4)
        carrier_c_contact = cur.fetchall()
        cur.execute(command5)
        purchasing_organization_po_contact = cur.fetchall()
        cur.execute(command6)
        location = cur.fetchall()
        cur.execute(command7)
        location_l_contact = cur.fetchall()
        cur.execute(command8)
        carrier = cur.fetchall()
        cur.execute(command9)
        purchasing_organization = cur.fetchall()
        cur.execute(command10)
        appointment = cur.fetchall()
        cur.execute(command11)
        requests = cur.fetchall()
        return render_template('select.html',data = {"user":user,"id":id,"products":products,"items":items,"orders":orders,"carrier_c_contact":carrier_c_contact,"purchasing_organization_po_contact":purchasing_organization_po_contact,"location":location,"location_l_contact":location_l_contact,"carrier":carrier,"purchasing_organization":purchasing_organization,"appointment":appointment,"requests":requests})
    else:
        command1 = "select appointment_id,d_name, d_id, license_plate, proposed_date, status, d_contact, po_id, po_name from appointment natural join purchasing_organization where carrier_id = {};".format(id)
        command2 = "select po_id,deadline from requests where carrier_id = {};".format(id)
        command3 = "select order_id,alloted_date,dock,total_quantity,special_instrs,po_id,location_id,po_name from orders natural join purchasing_organization where carrier_id = {};".format(id)
        command4 = "select carrier_id,c_contact from carrier_c_contact where carrier_id = {};".format(id)
        command5 = "select po_contact,po_name, po_id from purchasing_organization_po_contact natural join purchasing_organization;"

        command6 = "select carrier_id,c_name,c_street,c_city,c_state from carrier where carrier_id = {};".format(id)
        command7 = "select l_contact,location_id,type,po_name from purchasing_organization right join location on location.po_id = purchasing_organization.po_id natural join location_l_contact;"
        command8 = "select location_id,l_street,l_city,l_state,type,po_name from purchasing_organization right join location on location.po_id = purchasing_organization.po_id;"
        command9 = "select po_id,po_name,po_street,po_city,po_state from purchasing_organization;"
        cur.execute(command1)
        appointments = cur.fetchall()
        cur.execute(command2)
        requests = cur.fetchall()
        cur.execute(command3)
        orders = cur.fetchall()
        cur.execute(command6)
        carrier = cur.fetchall()
        cur.execute(command4)
        carrier_c_contact = cur.fetchall()
        cur.execute(command5)
        purchasing_organization_po_contact = cur.fetchall()
        cur.execute(command7)
        location_l_contact = cur.fetchall()
        cur.execute(command8)
        location = cur.fetchall()
        cur.execute(command9)
        purchasing_organization = cur.fetchall()
        return render_template('select.html', data = {"user": user, "id": id, "appointments": appointments,"requests": requests, "orders": orders, "carrier":carrier,"carrier_c_contact":carrier_c_contact,"purchasing_organization_po_contact":purchasing_organization_po_contact,"location_l_contact":location_l_contact,"location":location,"purchasing_organization":purchasing_organization})
    

@app.route('/form/<table>/<op>/<tid>', methods = ["POST", "GET"])
def form(table, tid, op):
    global user
    global id
    if(op == "update"):
        if(user == 'po_products_mgr'):
            command1 = "select product_id, product_name from product where po_id = {} and product_id = {};".format(id, tid)
            command2 =  "select item_id, product_id, product_name, quantity, weight, dangerous_good, order_id from items natural join product where po_id = {} and item_id = {}".format(id, tid)
            command3 = "select po_contact from purchasing_organization_po_contact where po_id = {} and po_contact = '{}'".format(id, tid)
            command4 = "select location_id,l_street,l_city,l_state,type from location where po_id = {} ".format(id)
            command5 = "select location_id,l_contact,type from location natural join location_l_contact where location_id={}".format(tid)
            if(table == "product"):
                cur.execute(command1)
                default = cur.fetchall()
            elif(table == "items"):
                cur.execute(command2)
                default = cur.fetchall()
            elif(table == "purchasing_organization_po_contact"):
                cur.execute(command3)
                default = cur.fetchall()
            elif(table == "location"):
                cur.execute(command4)
                default = cur.fetchall()
            elif(table == "location_l_contact"):
                cur.execute(command5)
                default = cur.fetchall()
            return render_template('update.html', data = {"user": user, "id": id, "table": table, "default": default, "tid": tid})
        elif(user == 'po_shipment_mgr'):
            command1 = "select product_id, product_name from product where po_id = {} and product_id = {};".format(id, tid)
            command2 = "select item_id,product_id,product_name,quantity,weight,dangerous_good,order_id from items natural join product where po_id = {} and item_id = {}".format(id,tid)
            command3 = "select order_id,alloted_date,dock,total_quantity,special_instrs,carrier_id,location_id from orders where po_id = {} and order_id={}".format(id,tid)
            command4 = "select carrier_id,c_contact from carrier_c_contact carrier_id = {}".format(tid)
            command5 = "select po_contact from purchasing_organization_po_contact where po_id = {} and po_contact = '{}'".format(id, tid)
            command6 = "select location_id,l_street,l_city,l_state,type from location where po_id = {} ".format(id)
            command7 = "select location_id,l_contact,type from location natural join location_l_contact where location_id={}".format(tid)
            command8 = "select carrier_id,c_name,c_street,c_city,c_state from carrier where carrier_id = {}".format(tid)
            command9 = "select po_id,po_name,po_street,po_city,po_state from purchasing_organization where po_id = {}".format(id)
            command10 = "select appointment_id,d_name,d_id,license_plate,proposed_date,status,d_contact,carrier_id from appointment where po_id = {} and appointment_id = {} ".format(id,tid)
            command11 = "select carrier_id,deadline from requests where po_id = {} and carrier_id = {} ".format(id,tid)
            if(table == "product"):
                cur.execute(command1)
                default = cur.fetchall()
            elif(table == "items"):
                cur.execute(command2)
                default = cur.fetchall()
            elif(table=="orders"):
                cur.execute(command3)
                default = cur.fetchall()
            elif(table=="carrier_c_contact"):
                cur.execute(command4)
                default = cur.fetchall()
            elif(table=="purchasing_organization_po_contact"):
                cur.execute(command5)
                default = cur.fetchall()
            elif(table=="location"):
                cur.execute(command6)
                default = cur.fetchall()
            elif(table=="location_l_contact"):
                cur.execute(command7)
                default = cur.fetchall()
            elif(table=="carrier"):
                cur.execute(command8)
                default = cur.fetchall()
            elif(table=="purchasing_organization"):
                cur.execute(command9)
                default = cur.fetchall()
            elif(table=="appointment"):
                cur.execute(command10)
                default = cur.fetchall()
            elif(table=="requests"):
                cur.execute(command11)
                default = cur.fetchall()
            return render_template('update.html', data = {"user": user, "id": id, "table": table, "default": default, "tid": tid})
        else:
            if(table == "appointment"):
                command1 = "select appointment_id,d_name, d_id, license_plate, proposed_date, status, d_contact, carrier_id from appointment where carrier_id = {} and appointment_id = {};".format(id, tid)
                cur.execute(command1)
                default = cur.fetchall()
            elif(table == "carrier"):
                command2 = "select carrier_id,c_name,c_street,c_city,c_state from carrier where carrier_id = {};".format(id)
                cur.execute(command2)
                default = cur.fetchall()
            elif(table == "carrier_c_contact"):
                command3 = "select carrier_id,c_contact from carrier_c_contact where carrier_id = {} and c_contact = '{}';".format(id, tid.split(";")[1])
                cur.execute(command3)
                default = cur.fetchall()
            return render_template('update.html', data = {"user": user, "id": id, "table": table, "default": default, "tid": tid})
    elif(op == "delete"):
        try:
            if(table == "product"):
                command = "delete from {} where product_id = {}".format(table, tid)
                cur.execute(command)
                conn.commit()
                return redirect(url_for("select", data = {"user": user, "id": id}))
    
            elif(table == "items"):
                command = "delete from {} where item_id = {}".format(table, tid)
                cur.execute(command)
                conn.commit()
                return redirect(url_for("select", data = {"user": user, "id": id}))

            elif(table == "orders"):
                command = "delete from {} where order_id = {}".format(table, tid)
                cur.execute(command)
                conn.commit()
                return redirect(url_for("select", data = {"user": user, "id": id}))

            elif(table == "location"):
                command = "delete from {} where location_id = {}".format(table, tid)
                cur.execute(command)
                conn.commit()
                return redirect(url_for("select", data = {"user": user, "id": id}))
            
            elif(table == "appointment"):
                try:
                    command = "delete from {} where appointment_id = {}".format(table, tid)
                    cur.execute(command)
                    conn.commit()
                    return redirect(url_for("select", data = {"user": user, "id": id}))
                except:
                    return render_template('error.html', data = {"message": "Cannot delete that entry!"})
            elif(table == "carrier"):
                try:
                    command = "delete from {} where carrier_id = {}".format(table, tid)
                    cur.execute(command)
                    conn.commit()
                    return redirect(url_for("select", data = {"user": user, "id": id}))
                except:
                    return render_template('error.html', data = {"message": "Cannot delete that entry!"})
            elif(table == "carrier_c_contact"):
                try:
                    command = "delete from {} where carrier_id = {} and c_contact = '{}'".format(table, tid.split(";")[0], tid.split(";")[1])
                    print(command)
                    cur.execute(command)
                    conn.commit()
                    return redirect(url_for("select", data = {"user": user, "id": id}))
                except:
                    return render_template('error.html', data = {"message": "Cannot delete that entry!"})
            elif(table == "purchasing_organization_po_contact"):
                try:
                    command = "delete from {} where po_id = {} and po_contact = '{}'".format(table, id, tid)
                    print(command)
                    cur.execute(command)
                    conn.commit()
                    return redirect(url_for("select", data = {"user": user, "id": id}))
                except:
                    return render_template('error.html', data = {"message": "Cannot delete that entry!"})
            elif(table == "location_l_contact"):
                try:
                    command = "delete from {} where location_id = {} and l_contact = '{}'".format(table, tid.split(";")[0], tid.split(";")[1])
                    print(command)
                    cur.execute(command)
                    conn.commit()
                    return redirect(url_for("select", data = {"user": user, "id": id}))
                except Exception as e:
                    print(e)
                    return render_template('error.html', data = {"message": "Cannot delete that entry!"})
        
        except:
            return render_template('error.html', data = {"message": "Cannot delete that entry!"})
    else:
        try:
            print(table, tid, id)
            return render_template('update.html', data = {"user": user, "id": id, "table": table, "default": [], "tid": tid})
        except Exception as e:
            print(e)
            return render_template('error.html', data = {"message": "Cannot insert that entry!"})
    
@app.route('/save/<op>/<table>/<tid>', methods = ["POST", "GET"])
def save(op, table, tid):
    global user
    global cur
    global conn
    global id
    
    if(op == "update"):
        try:
            tid, tid2, _ = tid.split(";")
        except:
            tid, tid2 = tid.split(";")
        try:
            if(table == "product"):
                command = "update {} set product_id = {}, product_name = '{}' where product_id = {}".format(table, request.form.get("product_id"), request.form.get("product_name"), tid)
                print(command)
                cur.execute(command)
                conn.commit()
            elif(table == "items"):
                command = "update {} set item_id = {}, product_id = {}, quantity = {}, weight = {}, dangerous_good = {}, order_id = {} where item_id = {}".format(table, request.form.get("item_id"), request.form.get("product_id"), request.form.get("quantity"), request.form.get("weight"), request.form.get("dangerous_good"), request.form.get("order_id"), tid)
                print(command)
                cur.execute(command)
                conn.commit()
            elif(table=="orders"):
                command = "update {} set order_id = {}, alloted_date = '{}', dock = {}, total_quantity = {}, special_instrs = '{}', carrier_id = {}, location_id = {} where order_id = {}".format(table, request.form.get("order_id"), request.form.get("alloted_date"), request.form.get("dock"), request.form.get("total_quantity"), request.form.get("special_instructions"), request.form.get("carrier_id"), request.form.get("location_id"), tid)
                cur.execute(command)
                conn.commit()
            elif(table=="purchasing_organization_po_contact"):
                command = "update {} set po_contact = '{}' where po_id = {} and po_contact = '{}'".format(table, request.form.get("po_contact"),id, tid)
                print(command)
                cur.execute(command)
                conn.commit()
            elif(table=="carrier_c_contact"):
                command = "update {} set c_contact = '{}' where carrier_id = {} and c_contact = '{}'".format(table, request.form.get("carrier_contact"),id, tid2)
                print(command)
                cur.execute(command)
                conn.commit()
            elif(table=="appointment"):
                command = "update {} set appointment_id = {}, d_name = '{}', d_id = {}, license_plate = '{}', proposed_date = '{}', status = {}, d_contact = {}, carrier_id = {} where appointment_id = {}".format(table, request.form.get("appointment_id"), request.form.get("d_name"), request.form.get("d_id"), request.form.get("license_plate"), request.form.get("proposed_date"), request.form.get("status"), request.form.get("d_contact"), request.form.get("carrier_id"), tid)
                print(command)
                cur.execute(command)
                conn.commit()
            elif(table=="requests"):
                command = "update {} set carrier_id = {}, deadline = '{}' where po_id = {}".format(table, request.form.get("carrier_id"), request.form.get("deadline"), id)
                cur.execute(command)
                conn.commit()
            elif(table=="purchasing_organization"):
                command = "update {} set po_id = {}, po_name = '{}',  po_street = '{}', po_city = '{}', po_state = '{}' where po_id = {}".format(table, request.form.get("po_id"), request.form.get("po_name"), request.form.get("po_street"), request.form.get("po_city"), request.form.get("po_state"), id)
                print(command)
                cur.execute(command)
                conn.commit()
            elif(table=="location"):
                command = "update {} set location_id = {}, l_street = '{}',  l_city = '{}', l_state = '{}', type = '{}' where location_id = {} ".format(table, request.form.get("location_id"), request.form.get("location_street"), request.form.get("location_city"), request.form.get("location_state"), request.form.get("location_type"), tid)
                print(command)
                cur.execute(command)
                conn.commit()
            elif(table=="location_l_contact"):
                command = "update {} set location_id={} , l_contact = '{}' where location_id = {} and l_contact = '{}'".format(table, request.form.get("location_id"), request.form.get("location_contact"), tid, tid2)
                print(command)
                cur.execute(command)
                conn.commit() 
            return redirect(url_for("select", data = {"user": user, "id": id}))
        except Exception as e:
            print(e)
            return render_template('error.html', data = {"message": "Cannot Update that entry!"})
    elif(op == "insert"):
        try:
            if(table == "product"):
                command = "insert into {} values({},'{}',{})".format(table, request.form.get("product_id"), request.form.get("product_name"), id)
                print(command)
                cur.execute(command)
                conn.commit()
            elif(table == "items"):
                if(request.form.get("order_id") == ""):
                    order_id = "NULL"
                else:
                    order_id = request.form.get("order_id")
                command = "insert into {} values({},{},{},{},{},{})".format(table, request.form.get("item_id"), request.form.get("dangerous_good"), request.form.get("quantity"), request.form.get("weight"), order_id, request.form.get("product_id"))
                print(command)
                cur.execute(command)
                conn.commit()
            elif(table=="orders"):
                if(request.form.get("special_instructions") == ""):
                    sp_in = "NULL"
                else:
                    sp_in = request.form.get("special_instructions")
                command = "insert into {} values({},'{}',{},{},{},{},{},{})".format(table, request.form.get("order_id"), request.form.get("alloted_date"), request.form.get("dock"), request.form.get("total_quantity"), sp_in, id, request.form.get("carrier_id"), request.form.get("location_id"))
                cur.execute(command)
                conn.commit()
            elif(table=="purchasing_organization_po_contact"):
                command = "insert into {} values('{}',{})".format(table, request.form.get("po_contact"),id)
                print(command)
                cur.execute(command)
                conn.commit()
            elif(table=="appointment"):
                command = "insert into {} values({},'{}',{},'{}','{}',{},{},{},{})".format(table, request.form.get("appointment_id"), request.form.get("d_name"), request.form.get("d_id"), request.form.get("license_plate"), request.form.get("proposed_date"), request.form.get("status"), request.form.get("d_contact"), id, request.form.get("po_id"))
                print(command)
                cur.execute(command)
                conn.commit()
            elif(table=="requests"):
                command = "insert into {} values('{}',{},{})".format(table, request.form.get("deadline"), id, request.form.get("carrier_id"))
                cur.execute(command)
                conn.commit()
            elif(table=="purchasing_organization"):
                command = "insert into {} values('{}','{}','{}',{},'{}')".format(table, request.form.get("po_street"), request.form.get("po_state"), request.form.get("po_city"), id, request.form.get("po_name"))
                print(command)
                cur.execute(command)
                conn.commit()
            elif(table=="location"):
                command = "insert into {} values('{}','{}','{}','{}',{},{})".format(table, request.form.get("location_street"), request.form.get("location_city"), request.form.get("location_state"), request.form.get("location_type"), request.form.get("location_id"), id)
                print(command)
                cur.execute(command)
                conn.commit()
            elif(table=="location_l_contact"):
                command = "insert into {} values({},{})".format(table, request.form.get("location_contact"), request.form.get("location_id"))
                print(command)
                cur.execute(command)
                conn.commit() 
            elif(table=="carrier"):
                command = "insert into {} values({},{},{},{},{})".format(table, id, request.form.get("c_name"), request.form.get("c_street"), request.form.get("c_city"), request.form.get("c_state"))
                print(command)
                cur.execute(command)
                conn.commit() 
            elif(table=="carrier_c_contact"):
                print(id)
                command = "insert into {} values({},{})".format(table, request.form.get("carrier_contact"), id)
                print(command)
                cur.execute(command)
                conn.commit() 
            return redirect(url_for("select", data = {"user": user, "id": id}))
        except Exception as e:
            print(e)
            return render_template('error.html', data = {"message": "Cannot Insert that entry!"})


if __name__ == '__main__':
    app.run(debug=True)
