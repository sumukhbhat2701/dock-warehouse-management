\c dockwarehouse_mgt;

select c_name from carrier natural join (select carrier_id from (select carrier_id, count(*) from orders group by carrier_id) as y  where count = (select min(count) from (select carrier_id, count(*) from orders group by carrier_id) as x)) as z; 

select sum(quantity) as Total_Quantity from product natural join items natural join purchasing_organization where po_name = 'Nestle';

select product_name, quantity from product natural join items where quantity = (select min(quantity) from items natural join product where po_id = 1);

select order_id, po_name, po_street from purchasing_organization as p, orders as o, location as l, carrier as c where p.po_id = o.po_id and o.location_id = l.location_id and c.carrier_id = o.carrier_id and type = 's' and l_city = 'Bangalore';

select l_city from location where location_id in (select location_id from (select l.location_id, count(*) from location as l, orders as o where l.location_id = o.location_id group by l.location_id) as y where count = (select max(count) from (select l.location_id, count(*) from location as l, orders as o where l.location_id = o.location_id group by l.location_id) as x));

select order_id, count(*) from carrier natural join orders natural join items where dangerous_good = 1 and carrier_id = 22 group by order_id;

select po_name, product_name from (select product_name, po_id from (select product_id from (select product_id, count(*) from orders natural join product group by product_id) as x where x.count = (select max(count) from (select product_id, count(*) from orders natural join product group by product_id) as y)) as z natural join product) as t natural join purchasing_organization;
