USE foodApp;


CREATE TABLE User(
    user_id VARCHAR(30),
    password VARCHAR(18),
    role VARCHAR(10),
    PRIMARY KEY(user_id)
)