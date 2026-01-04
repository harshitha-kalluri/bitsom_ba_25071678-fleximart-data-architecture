# NoSQL Database Analysis – FlexiMart

## Section A: Limitations of Relational Databases (RDBMS)

Relational databases are designed with a fixed schema, which makes them less suitable for handling highly diverse product data. In an e-commerce platform like FlexiMart, different product categories often require different attributes. For example, laptops may have specifications such as RAM, processor, and storage, while shoes require size, color, and material. In a relational database, accommodating these differences typically requires creating many nullable columns or multiple related tables, which increases complexity and reduces clarity.

Frequent schema changes are another challenge. When new product types are introduced, altering table structures in an RDBMS involves schema migrations that can be time-consuming and risky, especially in production environments. These changes may also affect existing applications and queries.

Additionally, storing customer reviews as nested data is not straightforward in relational databases. Reviews usually require separate tables and multiple joins to retrieve complete product information. This leads to more complex queries and can impact performance, especially when dealing with large volumes of data.

---

## Section B: Benefits of MongoDB (NoSQL)

MongoDB addresses these challenges through its flexible, document-based data model. Each product can be stored as a separate document with its own structure, allowing different attributes for different product categories without enforcing a fixed schema. This makes it easy to add new product types without modifying existing data structures.

MongoDB also supports embedded documents, which allows related data such as customer reviews to be stored directly within the product document. This reduces the need for joins and simplifies data retrieval, as all relevant information for a product can be accessed in a single query.

Another key advantage is horizontal scalability. MongoDB is designed to scale across multiple servers using sharding, making it suitable for applications with growing data volumes and high read/write demands. This scalability, combined with schema flexibility, makes MongoDB well-suited for managing a dynamic and evolving product catalog like that of FlexiMart.

---

## Section C: Trade-offs of Using MongoDB

One disadvantage of using MongoDB instead of MySQL is the lack of strong relational constraints such as foreign keys. This places more responsibility on the application layer to maintain data consistency and integrity.

Another trade-off is that complex analytical queries can be more challenging in MongoDB compared to relational databases. While MongoDB supports aggregation pipelines, certain multi-table analytical operations are often easier and more efficient to express using SQL in a relational data warehouse.
