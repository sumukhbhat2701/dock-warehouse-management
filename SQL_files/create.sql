DROP DATABASE dockwarehouse_mgt;

CREATE DATABASE dockwarehouse_mgt;

\c dockwarehouse_mgt;

CREATE TABLE purchasing_organization
(
  po_street VARCHAR(20) ,
  po_state VARCHAR(20),
  po_city VARCHAR(20),
  po_id INT,
  po_name VARCHAR(20) NOT NULL,
  PRIMARY KEY (po_id)
);

CREATE TABLE carrier
(
  carrier_id INT,
  c_name VARCHAR(20) NOT NULL,
  c_street VARCHAR(20),
  c_city VARCHAR(20),
  c_state VARCHAR(20),
  PRIMARY KEY (carrier_id)
);

CREATE TABLE location
(
  l_street VARCHAR(20),
  l_city VARCHAR(20),
  l_state VARCHAR(20),
  type VARCHAR(1) NOT NULL,
  location_id INT,
  po_id INT,
  PRIMARY KEY (location_id),
  FOREIGN KEY (po_id) REFERENCES purchasing_organization(po_id)
);

CREATE TABLE appointment
(
  appointment_id INT,
  d_name VARCHAR(20) NOT NULL,
  d_id INT NOT NULL,
  license_plate VARCHAR(10) NOT NULL,
  proposed_date DATE NOT NULL,
  status INT NOT NULL,
  d_contact VARCHAR(10),
  carrier_id INT NOT NULL,
  po_id INT NOT NULL,
  PRIMARY KEY (appointment_id),
  FOREIGN KEY (carrier_id) REFERENCES carrier(carrier_id),
  FOREIGN KEY (po_id) REFERENCES purchasing_organization(po_id)
);

CREATE TABLE product
(
  product_id INT,
  product_name VARCHAR(30) NOT NULL,
  po_id INT NOT NULL,
  PRIMARY KEY (product_id),
  FOREIGN KEY (po_id) REFERENCES purchasing_organization(po_id)
);

CREATE TABLE requests
(
  deadline DATE,
  po_id INT,
  carrier_id INT,
  PRIMARY KEY (po_id, carrier_id),
  FOREIGN KEY (po_id) REFERENCES purchasing_organization(po_id),
  FOREIGN KEY (carrier_id) REFERENCES carrier(carrier_id)
);

CREATE TABLE purchasing_organization_po_contact
(
  po_contact VARCHAR(10),
  po_id INT,
  PRIMARY KEY (po_contact, po_id),
  FOREIGN KEY (po_id) REFERENCES purchasing_organization(po_id)
);

CREATE TABLE carrier_c_contact
(
  c_contact VARCHAR(10),
  carrier_id INT,
  PRIMARY KEY (c_contact, carrier_id),
  FOREIGN KEY (carrier_id) REFERENCES carrier(carrier_id)
);

CREATE TABLE location_l_contact
(
  l_contact VARCHAR(10),
  location_id INT,
  PRIMARY KEY (l_contact, location_id),
  FOREIGN KEY (location_id) REFERENCES location(location_id)
);

CREATE TABLE orders
(
  order_id INT,
  alloted_date DATE NOT NULL,
  dock INT NOT NULL,
  total_quantity INT NOT NULL,
  special_instrs VARCHAR(100),
  po_id INT NOT NULL,
  carrier_id INT NOT NULL,
  location_id INT NOT NULL,
  PRIMARY KEY (order_id),
  FOREIGN KEY (po_id) REFERENCES purchasing_organization(po_id),
  FOREIGN KEY (carrier_id) REFERENCES carrier(carrier_id),
  FOREIGN KEY (location_id) REFERENCES location(location_id)
);

CREATE TABLE items
(
  item_id INT,
  dangerous_good INT,
  quantity INT NOT NULL,
  weight FLOAT NOT NULL,
  order_id INT,
  product_id INT NOT NULL,
  PRIMARY KEY (item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES product(product_id)
);
