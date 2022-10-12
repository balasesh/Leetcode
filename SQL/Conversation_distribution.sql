We have a table that represents the total number of messages sent between two users by date on messenger.

What are some insights that could be derived from this table?

What do you think the distribution of the number of conversations created by each user per day looks like?

Write a query to get the distribution of the number of conversations created by each user by day in the year 2020.

Example:

Input:

messages table

Column	Type
id	INTEGER
date	DATETIME
user1	INTEGER
user2	INTEGER
msg_count	INTEGER

Output:

Column	Type
num_conversations	INTEGER
frequency	INTEGER