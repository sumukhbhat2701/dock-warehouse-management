create or replace function insert_order()
returns trigger
language plpgsql
as 
$$
begin
insert into orders values((SELECT MAX(order_id)+1 FROM orders), old.proposed_date, 9999, 9999, NULL, old.po_id, old.carrier_id, (select max(location_id) from location)); 
return old;
end; 
$$;

create trigger new_order
after update of status on appointment
for each row
when(new.status = 1)
execute procedure insert_order();

