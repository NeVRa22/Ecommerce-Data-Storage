import database as db

# Driver code
if __name__ == "__main__":
    """
    Please enter the necessary information related to the DB at this place. 
    Please change PW and ROOT based on the configuration of your own system. 
    """
    PW = "Bi@tches4822"  # IMPORTANT! Put your MySQL Terminal password here.
    ROOT = "root"
    DB = "ecommerce_record"  # This is the name of the database we will create in the next step - call it whatever
    # you like.
    LOCALHOST = "localhost"
    connection = db.create_server_connection(LOCALHOST, ROOT, PW)

    # creating the schema in the DB
    db.create_and_switch_database(connection, DB, DB)
    Database = """
    CREATE DATABASE ecommerce_record
    """
    orders_table = """
    CREATE TABLE orders;
    INSERT INTO orders VALUES
    (101, 23455, 3, 250, '5', '12'),
    (102, 34556, 2, 0, '2', '14'),
    (103, 45512, 4, 150, '3', '16'),
    (104, 55123, 2, 50, '4', '18'),
    (105, 53456, 1, 350, '1', '17')
    """
    db.create_insert_query(connection, orders_table)

    print("details of all orders: ")
    p1 = """
    SELECT * FROM orders;
    """
    order_details = db.select_query(connection, p1)
    for result in order_details:
        print(result)

    p2 = """
    SELECT * FROM orders
    WHERE total_value = (select MIN (total_value)
    from orders);
    """
    min_order_detail = db.select_query(connection.p2)
    print(" lowest Order value is: ")
    print(min_order_detail)

    p3 = """
        SELECT * FROM orders
        WHERE total_value = (select MAX (total_value)
        from orders);
        """
    max_order_detail = db.select_query(connection.p3)
    print(" lowest Order value is: ")
    print(max_order_detail)

    p4 = """
    SELECT * FROM orders WHERE total_value>(select AVG(total_value)
    FROM orders)
    """
    high_order_value = db.select_query(connection.p4)
    for result in high_order_value:
        print(result)

    p5 = """
    SELECT o.customer_id, MAX(o.total_value) as MAX_Value, c.user_name, c.user_email
    FROM ecommerce_record.users c ON o.customer_id=c.user_id
    GROUP BY o.customer_id;
    """
    highest_purchase_per_customer = db.select_query(connection.p5)
    for result in highest_purchase_per_customer:
        print(result)

    # Start implementing your task as mentioned in the problem statement
    # Implement all the test cases and test them by running this file
