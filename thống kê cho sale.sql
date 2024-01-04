-- số đơn trong ngày
SELECT seller_id, count(orders.id), sum(orders.total_fee), date_format(orders.created,"%d-%m-%Y") as dmY
FROM fplatform.orders join fplatform.user on partner_id = user.id
group by dmY, partner_id order by orders.id desc;

-- số đơn seller lên trong ngày
SELECT count(id), sum(total_fee), date_format(orders.created,"%d-%m-%Y") as dmY
FROM fplatform.orders group by dmY order by id desc;

-- số group tích trong ngày
SELECT count(id), date_format(order_group.group_done_at,"%d-%m-%Y") as dmY
FROM fplatform.order_group group by dmY order by id desc;

-- số đơn thuộc group tích trong ngày
SELECT count(orders.id), date_format(order_group.group_done_at,"%d-%m-%Y") as dmY
FROM fplatform.order_group join fplatform.orders on order_group_id = order_group.id
group by dmY having dmY is not null order by order_group.id desc;

-- số đơn trong group chưa tích
SELECT count(orders.id) 
FROM fplatform.order_group join fplatform.orders on order_group_id = order_group.id
where group_done_at is null and order_group.product_type = "SHIRT" and order_group.created >= CURDATE()
and orders.status != "HOLD" and orders.status != "REJECTED" and orders.status != "REJECT_REQUESTED";

-- số áo, số file trong group chưa tích
SELECT sum(quantity), sum(pdf) 
from (SELECT order_product.quantity, if (front_print_url is not null && back_print_url is not null, 2*order_product.quantity, order_product.quantity) as pdf
FROM fplatform.order_group join fplatform.orders on order_group_id = order_group.id
join fplatform.order_product on order_id = orders.id
where group_done_at is null and order_group.product_type = "SHIRT" and order_group.created >= CURDATE()
and orders.status != "HOLD" and orders.status != "REJECTED" and orders.status != "REJECT_REQUESTED"
group by order_id, line_id) a;