Given a table of bank transactions with columns id, transaction_value, and created_at representing the date and time for each transaction, write a query to get the last transaction for each day.
The output should include the id of the transaction, datetime of the transaction, and the transaction amount. Order the transactions by datetime.

Example:

Input:

bank_transactions table

Column	Type
id	INTEGER
created_at	DATETIME
transaction_value	FLOAT
Output:

Column	Type
created_at	DATETIME
transaction_value	FLOAT
id	INTEGER

-------------------------------------------------------------------
with last_daily_transaction AS (
    Select
        DATE(created_at) as date_of_transaction,
        MAX(created_at) as transaction_time
    from
        bank_transactions
    GROUP BY
        DATE(created_at)
)
select
    created_at,
    transaction_value,
    id
from
    bank_transactions
where
    transaction_time = created_at
order by
    1 desc


------------------------------------------------------------------------------------------
with last_daily_transaction AS (
    select
        dense_rank() over (
            partition by date(created_at)
            order by
                created_at desc
        ) last_transation_rank,
        -- date(created_at) as date_of_transaction,
        *
    from
        bank_transactions
)
select
    created_at,
    transaction_value,
    id
from
    last_daily_transaction
where
    last_transation_rank = 1
    