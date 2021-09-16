SELECT users.id ,
users.username , 
products.id ,
products.name , 
categories.id ,
categories.name ,
products.price,
sales.price ,
sales.quantity ,
(products.quantity - sales.quantity ),
sales.updated_at 
FROM users  
JOIN sales  ON users.id = sales.user_id
JOIN products  ON products.id = sales.product_id
JOIN categories  ON categories.id = products.category_id