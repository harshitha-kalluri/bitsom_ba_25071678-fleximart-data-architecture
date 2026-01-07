---DIM_DATE
USE fleximart_dw;

INSERT INTO dim_date VALUES
(20240101,'2024-01-01','Monday',1,1,'January','Q1',2024,0),
(20240102,'2024-01-02','Tuesday',2,1,'January','Q1',2024,0),
(20240103,'2024-01-03','Wednesday',3,1,'January','Q1',2024,0),
(20240104,'2024-01-04','Thursday',4,1,'January','Q1',2024,0),
(20240105,'2024-01-05','Friday',5,1,'January','Q1',2024,0),
(20240106,'2024-01-06','Saturday',6,1,'January','Q1',2024,1),
(20240107,'2024-01-07','Sunday',7,1,'January','Q1',2024,1),
(20240108,'2024-01-08','Monday',8,1,'January','Q1',2024,0),
(20240109,'2024-01-09','Tuesday',9,1,'January','Q1',2024,0),
(20240110,'2024-01-10','Wednesday',10,1,'January','Q1',2024,0),
(20240111,'2024-01-11','Thursday',11,1,'January','Q1',2024,0),
(20240112,'2024-01-12','Friday',12,1,'January','Q1',2024,0),
(20240113,'2024-01-13','Saturday',13,1,'January','Q1',2024,1),
(20240114,'2024-01-14','Sunday',14,1,'January','Q1',2024,1),
(20240115,'2024-01-15','Monday',15,1,'January','Q1',2024,0),
(20240116,'2024-01-16','Tuesday',16,1,'January','Q1',2024,0),
(20240117,'2024-01-17','Wednesday',17,1,'January','Q1',2024,0),
(20240118,'2024-01-18','Thursday',18,1,'January','Q1',2024,0),
(20240119,'2024-01-19','Friday',19,1,'January','Q1',2024,0),
(20240120,'2024-01-20','Saturday',20,1,'January','Q1',2024,1),
(20240201,'2024-02-01','Thursday',1,2,'February','Q1',2024,0),
(20240202,'2024-02-02','Friday',2,2,'February','Q1',2024,0),
(20240203,'2024-02-03','Saturday',3,2,'February','Q1',2024,1),
(20240204,'2024-02-04','Sunday',4,2,'February','Q1',2024,1),
(20240205,'2024-02-05','Monday',5,2,'February','Q1',2024,0),
(20240206,'2024-02-06','Tuesday',6,2,'February','Q1',2024,0),
(20240207,'2024-02-07','Wednesday',7,2,'February','Q1',2024,0),
(20240208,'2024-02-08','Thursday',8,2,'February','Q1',2024,0),
(20240209,'2024-02-09','Friday',9,2,'February','Q1',2024,0),
(20240210,'2024-02-10','Saturday',10,2,'February','Q1',2024,1);

--DIM_PRODUCT (15 products, 3 categories)
INSERT INTO dim_product (product_id, product_name, category, subcategory, unit_price) VALUES
('P001','Laptop Pro','Electronics','Computing',75000),
('P002','Smartphone X','Electronics','Mobile',45000),
('P003','Bluetooth Speaker','Electronics','Audio',8000),
('P004','Wireless Mouse','Electronics','Accessories',1500),
('P005','LED TV','Electronics','Home Entertainment',55000),

('P006','Running Shoes','Fashion','Footwear',5000),
('P007','Leather Jacket','Fashion','Clothing',12000),
('P008','Jeans','Fashion','Clothing',3000),
('P009','Handbag','Fashion','Accessories',7000),
('P010','Sports Watch','Fashion','Wearables',9500),

('P011','Office Chair','Furniture','Office',15000),
('P012','Dining Table','Furniture','Home',40000),
('P013','Bookshelf','Furniture','Storage',8000),
('P014','Sofa Set','Furniture','Living Room',90000),
('P015','Bed Frame','Furniture','Bedroom',60000);

--DIM_CUSTOMER (12 customers, 4 cities)

INSERT INTO dim_customer (customer_id, customer_name, city, state, customer_segment) VALUES
('C001','Rahul Sharma','Mumbai','Maharashtra','Premium'),
('C002','Anita Verma','Delhi','Delhi','Regular'),
('C003','Suresh Reddy','Hyderabad','Telangana','Premium'),
('C004','Neha Singh','Bangalore','Karnataka','Regular'),
('C005','Amit Patel','Mumbai','Maharashtra','Corporate'),
('C006','Kiran Rao','Hyderabad','Telangana','Regular'),
('C007','Pooja Mehta','Delhi','Delhi','Premium'),
('C008','Rohit Jain','Bangalore','Karnataka','Corporate'),
('C009','Sneha Kulkarni','Mumbai','Maharashtra','Regular'),
('C010','Arjun Nair','Bangalore','Karnataka','Premium'),
('C011','Manish Gupta','Delhi','Delhi','Regular'),
('C012','Divya Iyer','Hyderabad','Telangana','Corporate');

--FACT_SALES (40 transactions, realistic patterns)

INSERT INTO fact_sales
(date_key, product_key, customer_key, quantity_sold, unit_price, discount_amount, total_amount)
VALUES
(20240106,1,1,2,75000,5000,145000),
(20240107,2,2,1,45000,0,45000),
(20240113,3,3,3,8000,500,23500),
(20240114,4,4,2,1500,0,3000),
(20240120,5,5,1,55000,2000,53000),

(20240203,6,6,2,5000,0,10000),
(20240204,7,7,1,12000,1000,11000),
(20240210,8,8,3,3000,0,9000),
(20240210,9,9,1,7000,500,6500),
(20240210,10,10,2,9500,0,19000),

(20240105,11,11,1,15000,0,15000),
(20240106,12,12,1,40000,5000,35000),
(20240107,13,1,2,8000,0,16000),
(20240113,14,2,1,90000,10000,80000),
(20240114,15,3,1,60000,0,60000),

(20240115,1,4,1,75000,0,75000),
(20240116,2,5,2,45000,2000,88000),
(20240117,3,6,1,8000,0,8000),
(20240118,4,7,3,1500,0,4500),
(20240119,5,8,1,55000,3000,52000),

(20240120,6,9,2,5000,0,10000),
(20240120,7,10,1,12000,0,12000),
(20240203,8,11,2,3000,0,6000),
(20240203,9,12,1,7000,500,6500),
(20240204,10,1,1,9500,0,9500),

(20240205,11,2,1,15000,0,15000),
(20240206,12,3,1,40000,4000,36000),
(20240207,13,4,2,8000,0,16000),
(20240208,14,5,1,90000,15000,75000),
(20240209,15,6,1,60000,0,60000),

(20240210,1,7,2,75000,5000,145000),
(20240210,2,8,1,45000,0,45000),
(20240210,3,9,3,8000,500,23500),
(20240210,4,10,2,1500,0,3000),
(20240210,5,11,1,55000,2000,53000),
(20240210,6,12,2,5000,0,10000),
(20240210,7,1,1,12000,1000,11000),
(20240210,8,2,3,3000,0,9000),
(20240210,9,3,1,7000,500,6500),
(20240210,10,4,2,9500,0,19000);