## SQL - Introduction

This was my first SQL project at Alx School where I began working with SQL and relational databases. It covered data definition, data manipulation language, subqueries, and using functions.

## Usage :dolphin:

* For scripts [3-list_tables.sql](./3-list_tables.sql) onward, specify the database to query using MySQL command line.

```
$ cat 3-list_tables.sql | mysql -h localhost -u root -p mysql
```

* Tasks 101-103 query from the database [temperatures.sql](./temperatures.sql).

## Tasks :page_with_curl:

* **0. List databases**: Lists all databases. [0-list_databases.sql](./0-list_databases.sql)

* **1. Create a database**: Creates the database `hbtn_0c_0`. [1-create_database.sql](./1-create_database.sql)

* **2. Delete a database**: Deletes the database `hbtn_0c_0`. [2-remove_databases.sql](./2-remove_databases.sql)

* **3. List tables**: Lists all tables. [3-list_tables.sql](./3-list_tables.sql)

* **4. First table**: Creates a table `first_table` with `id` and `name` columns. [4-first_table.sql](./4-first_table.sql)

* **5. Full description**: Prints full description of `first_table`. [5-full_table.sql](./5-full_table.sql)

* **6. List all in table**: Lists all rows of `first_table`. [6-list_values.sql](./6-list_values.sql)

* **7. First add**: Inserts a new row in `first_table`. [7-insert_value.sql](./7-insert_value.sql)

* **8. Count 89**: Displays the number of records with `id = 89` in `first_table`. [8-count_89.sql](./8-count_89.sql)

* **9. Full creation**: Creates and fills `second_table` with sample records. [9-full_creation.sql](./9-full_creation.sql)

* **10. List by best**: Lists `score` and `name` of all records of `second_table` in descending order of `score`. [10-top_score.sql](./10-top_score.sql)

* **11. Select the best**: Lists `score` and `name` of records with `score >= 10` in `second_table` in descending order of `score`. [11-best_score.sql](./11-best_score.sql)

* **12. Cheating is bad**: Updates Bob's score to 10 in `second_table`. [12-no_cheating.sql](./12-no_cheating.sql)

* **13. Score too low**: Removes records with `score <= 5` in `second_table`. [13-change_class.sql](./13-change_class.sql)

* **14. Average**: Computes the average `score` of all records in `second_table`. [14-average.sql](./14-average.sql)

* **15. Number by score**: Lists `score` and number of records with the same score in `second_table` in descending order of count. [15-groups.sql](./15-groups.sql)

* **16. Say my name**: Lists `score` and `name` of all records in `second_table` in descending order of `score`, excluding rows without a `name` value. [16-no_link.sql](./16-no_link.sql)

* **17. Go to UTF8**: Converts the `hbtn_0c_0` database to UTF8. [100-move_to_utf8.sql](./100-move_to_utf8.sql)

* **18. Temperatures #0**: Displays average temperature (Fahrenheit) by city in descending order. [101-avg_temperatures.sql](./101-avg_temperatures.sql)

* **19. Temperatures #1**: Displays three cities with the highest average temperature from July to August in descending order. [102-top_city.sql](./102-top_city.sql)

* **20. Temperature #2**: Displays max temperature of each state in order of state name. [103-max_state.sql](./103-max_state.sql)
