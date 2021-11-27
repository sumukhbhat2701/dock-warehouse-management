# Dock-warehouse Management
Dock warehouse management in-short manages distribution of products from shipper and carrier to destined stops. Shippers or Purchasing Organizations store the products in the warehouse in the form of storage units. Warehouses have a certain number of docks to load the trucks of carriers.

### Problem statement:
A Shipper or Purchasing Organization needs to transport goods that are produced by the manufacturing unit to the customers. Shipper notifies the carrier about the amount of goods to be transmitted and its respective destination. Carrier sets up an appointment and is acknowledged by the shipper. 
SU₁,SU₂,...SUₙ are the different storage units inside the warehouse. D₁,D₂,...Dₘ are the docks which facilitate the movement of goods from storage units to the trucks. The number of docks available are less than the number of storage units present that is mn.Therefore a total of m trucks, T₁, T₂,...Tₘ, owned by different or same carriers can be scheduled at a time leaving behind trucks Tₘ₊₁, Tₘ₊₂... waiting to access the docks. There usually exist only 2 gates to enter the storage facility, entry point, G₁ and exit point, G₂. This increases the need for scheduling the trucks, so as to avoid unwanted queues, waits and traffic in and around the facility of purchasing organization. Stopping points S₁, S₂, S₃...Sₖ are generally far from each other and also the warehouse, so we need to track them.
The problem lies in coordinating operations between storage units, the items stored and dock stations. In the same way, synchronize access slots of the docks with appointments by the carrier. 

![alt ps](https://github.com/sumukhbhat2701/dock-warehouse-management/blob/main/dbms.jpg.jpg)

### Challenges to tackle:
- Scheduling access to different docks which are less than the number of carriers which try to access them.
- Reducing carrier traffic and ambiguity in timings.
- Tracking of orders.
- Agreement between Shipper and Carriers.
- Management of multiple stop points.
- Intractability may cause substantial financial losses.

### Mini-world description:
Dock warehouse management system aims at optimization of dock scheduling to facilitate smooth transport operations. Purchasing organization refers to companies or organizations which produce goods or buy goods from various manufacturing units set up by them in different places. Many purchasing organizations primarily focus on manufacturing items and seek help in transportation of these goods to its customers. This is where the carrier comes into picture. Carrier aims at transportation of these goods to the destination location.
A purchasing organization produces numerous products. After a particular product is created it classifies them into different orders according to the needs of its customers. The orders are stored in a warehouse which consists of numerous storage units. Warehouse consists of various docks wherein the trucks pickup the orders from the storage units. Purchasing organization requests the carrier to transport the orders by specifying the location where the order has to be dropped. Scheduling this dock is very important because inefficient scheduling will lead to high traffic inside the warehouse boundary. This will lead to high waiting time and corresponding waiting charges which is not what the purchasing organization wants.
Carriers can only deliver goods of some threshold weight. It looks into the request message which contains the weight and quantity of the order and decides whether or not to deliver that particular order. If yes then it schedules an appointment which contains details about the planned pickup date, license plate of the vehicle along with driver information and so on.
Purchasing organization goes through the appointment and sends out an acknowledgement to the carrier stating if it has accepted the appointment or not. If yes then a vehicle belonging to the carrier will come to pick up the order on the scheduled date and time.  The order is picked up from the dock and delivered to the desired location.

### Requirements Analysis:
The database is organised into purchasing organisation(purchasing_organisation) and each purchasing organisation has a unique name (po_name) and can have multiple contact (po_contact), address (po_address) that has street name(po_street), city name(po_city), state name(po_state). Each and every purchasing organisation stores it’s product in at least one location(location) which acts like a storage unit. Each location has a unique ID (location_id), a type of the location(type) that indicates whether the location is store point or stop point for a carrier(discussed later), can have multiple contacts(l_contact) and address as (l_address) that has street name(l_street), city name(l_city), state name(l_state). 

Purchasing Organisation can create many orders(orders) that have a unique ID(order_id), dock number(dock), total no of items in the order(total_quantity), date allotted for pick up(alloted_date), special instructions(special_instrs) pertaining to the delivery of that specific order. Each order must have one or more items(items) that has a unique ID(item_id), weight(weight), number of items(quantity) in the order and whether the item is dangerous or not(dangerous_good) as a precaution while delivering. Each and every order should be taken by a carrier(carrier) to deliver it and the carrier has a unique ID(carrier_id), can have many contact numbers(c_contact), a name(c_name) and address(c_address) that has street name(c_street), city name(c_city) and state name(c_state).

Purchasing Organisation can approve one or many appointments(appointment) that has a unique ID(appointment_id), whether approved or rejected (status), date proposed by carrier(proposed_date), driver information(driver_info) that holds driver name(d_name), driver ID(driver_id), license plate number(license_plate) and contact(d_contact). Each and every appointment should be made by a carrier. Each and every appointment must be approved by a purchasing organisation.

Each purchasing organisation must produce one or many products(product) that has a unique ID(product_id) and a product name(product_name). Each product must contain one or many items. Each and every order must be dropped at one location(location, with same attributes as described before) which is now considered as a stop point with contrast to location with regards to purchasing organization, where it was considered as storing units.

### ER Diagram: 
![alt erd](https://github.com/sumukhbhat2701/dock-warehouse-management/blob/main/final_er.drawio.png)

### Assumptions made:
- A purchasing organization can approve multiple appointments, but an appointment has to be approved by only a specific purchasing organization. If an appointment exists, then it has to be approved by a purchasing organization, but the other way may not hold true.
- A purchasing organization can request any carrier for transportation and a carrier can be requested by many purchasing organizations. A carrier may or may not have a purchasing organization that requests for its services and a purchasing organization may not have requested a carrier as well.
- A purchasing organization can create one or more orders, but an order should be created by only one purchasing organization. Every purchasing organization may or may not have created an order, but every order has to be created by a purchasing organization.
- A purchasing organization produces multiple products, but a product is created by a unique purchasing organization. A purchasing organization will produce some or other product and a product is produced by some or the other purchasing organization.
- A purchasing organization can store its goods in multiple locations, but a location is dedicated to a specific purchasing organization. Every purchasing organization must have at least one location, but a location may not be a storage unit for a purchasing organization, as we have normalized stop points for carrier's location as well.
- A product contains multiple items, but an item is contained by only one product. Every product should have at least one item and every item should be contained by at least one product.
- An order can have one or more items, but an item will be present only in a single order. Every item may not be in some or the other order, but an order will have some or the other items.
- A carrier can take multiple orders, but an order has to be taken by only one carrier. A carrier may not take an order at all, but every order has to be eventually taken up by a carrier.
- An order should be dropped at only one location, but the location can act like a stop point for multiple orders. Every order should have a dropping location, but every location may not be a stop point as it may be a purchasing organization’s storage unit(As mentioned before, stop points for carriers and storage units for purchasing organization is merged as a single entity called location)
- A carrier can make multiple appointments, but one appointment can be made by only one carrier. A carrier may not have an appointment, but if an appointment exists, then it is certainly mapped to a carrier.

### Relational Schema:
![alt rschema](https://github.com/sumukhbhat2701/dock-warehouse-management/blob/main/schema.png)

### Tech Stack/Dependencies:
- Python and Flask for backend
- HTML, CSS and Bootstrap(v5.0) for frontend
- Postgresql as RDBMS server
- Psycopg2 as database adapter for the Python backend

### Command to run the web application on localhost:
```python3 app.py```

### TO DO:
- Automate the process of schedule conflict resolution using the graph theory concept of vertex coloring
- Dockerize the web application

(Part of 5th semester Mini-Project for the course Database Management Systems at PES University, Bangalore)
