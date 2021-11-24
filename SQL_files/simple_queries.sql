\c dockwarehouse_mgt;

select count(*) from orders where po_id = 1 and orders.alloted_date = '2020-10-01';

select count(*) from orders where po_id = 1 and orders.alloted_date = '2020-10-01' group by po_id;

select po_id, appointment_id from appointment where carrier_id = 33 and status = 1;

select po_id, appointment_id from appointment where carrier_id = 33 and status = 0;

select product_id, count(*) from items group by product_id;

select l_street, l_city, l_state from location where po_id = 2;

select item_id, product_id from items where dangerous_good = 1;

select quantity/weight as unit_weight from items where item_id = 211;
