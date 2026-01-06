// Select database
use fleximart_nosql;

/*
Operation 1: Load Data
The product data is loaded into MongoDB using MongoDB Compass
from the file products_catalog.json.
*/


/*
Operation 2: Basic Query
Find all products in the Electronics category
with price less than 50000.
Return only name, price, and stock.
*/
db.products.find(
  { category: "Electronics", price: { $lt: 50000 } },
  { name: 1, price: 1, stock: 1, _id: 0 }
);


/*
Operation 3: Review Analysis
Find products with an average rating of 4.0 or higher.
*/
db.products.aggregate([
  { $unwind: "$reviews" },
  {
    $group: {
      _id: "$name",
      average_rating: { $avg: "$reviews.rating" }
    }
  },
  { $match: { average_rating: { $gte: 4 } } }
]);


/*
Operation 4: Update Operation
Add a new review to the product with product_id ELEC001.
*/
db.products.updateOne(
  { product_id: "ELEC001" },
  {
    $push: {
      reviews: {
        user: "U999",
        rating: 4,
        comment: "Good value",
        date: ISODate()
      }
    }
  }
);


/*
Operation 5: Complex Aggregation
Calculate the average price and product count by category.
Sort the result by average price in descending order.
*/
db.products.aggregate([
  {
    $group: {
      _id: "$category",
      avg_price: { $avg: "$price" },
      product_count: { $sum: 1 }
    }
  },
  { $sort: { avg_price: -1 } }
]);
