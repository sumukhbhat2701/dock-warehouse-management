create user po_shipment_mgr with password 'po@123';

create user po_products_mgr with password 'po@789';

create user carrier_shipment_mgr with password 'car@456';

grant select, update, insert, delete on requests to carrier_shipment_mgr;

grant insert, update, select, delete on requests to po_shipment_mgr;

grant select, update on appointment to po_shipment_mgr;

grant insert, update, select, delete on appointment to carrier_shipment_mgr;

grant insert, update, select, delete on orders to po_shipment_mgr;

grant select on orders to carrier_shipment_mgr;

grant select on items to po_shipment_mgr;

grant select on product to po_shipment_mgr;

grant select, update, insert, delete on product to po_products_mgr;

grant select, update, insert, delete on items to po_products_mgr;

grant select on carrier_c_contact to po_shipment_mgr;

grant select, insert, update, delete on carrier_c_contact to carrier_shipment_mgr;

grant select, insert, update, delete on purchasing_organization_po_contact to po_shipment_mgr;

grant select, insert, update, delete on purchasing_organization_po_contact to po_products_mgr;

grant select on purchasing_organization_po_contact to carrier_shipment_mgr;

grant select, insert, update, delete on location to po_shipment_mgr;

grant select, insert, update, delete on location to po_products_mgr;

grant select on location to carrier_shipment_mgr;

grant select, insert, update, delete on location_l_contact to po_shipment_mgr;

grant select, insert, update, delete on location_l_contact to po_products_mgr;

grant select on location_l_contact to carrier_shipment_mgr;

grant select on carrier to po_shipment_mgr;

grant select on carrier to po_products_mgr;

grant select, update, insert, delete on carrier to carrier_shipment_mgr;

grant select, update, insert, delete on purchasing_organization to po_shipment_mgr;

grant select, update, insert, delete on purchasing_organization to po_products_mgr;

grant select on purchasing_organization to carrier_shipment_mgr;


