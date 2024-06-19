USE foodApp;
DROP TABLE `User`;
DROP TABLE `Menu`;
DROP TABLE `Food`;
DROP TABLE `Feedback`;
DROP TABLE `Notification`;
DROP TABLE `Notificationtype`;
DROP TABLE `RecommendedFood`;
drop TABLE `Vote`;

CREATE TABLE User(
    user_id VARCHAR(30),
    user_name VARCHAR(30),
    password VARCHAR(18),
    role VARCHAR(10),
    PRIMARY KEY(user_id)
)


CREATE TABLE Menu (
    menu_id INT PRIMARY KEY,
    menu_name VARCHAR(100) NOT NULL,
    Timestamp DATETIME NOT NULL
);

CREATE TABLE Food (
    food_name VARCHAR(100)  PRIMARY KEY NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    availability_status BOOLEAN NOT NULL,
    avg_rating DECIMAL(3, 2) NOT NULL,
    avg_sentiment VARCHAR(10) DEFAULT 'Neutral',
    food_type VARCHAR(100) NOT NULL,
    menu_id INT,
    FOREIGN KEY (menu_id) REFERENCES Menu(menu_id)
);


CREATE TABLE Vote (
    user_id VARCHAR(30),
    have_voted BOOLEAN,
    food_name VARCHAR(30),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (food_name) REFERENCES Food(food_name)
);

CREATE TABLE RecommendedFood (
    food_name VARCHAR(100),
    total_vote INT,
    FOREIGN KEY (food_name) REFERENCES Food(food_name)
);

CREATE TABLE Feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(300) NOT NULL,
    rating FLOAT NOT NULL,
    sentiment VARCHAR(300),
    user_id VARCHAR(30),
    food_name VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (food_name) REFERENCES Food(food_name),
    UNIQUE (user_id, food_name) 
);


CREATE TABLE Notificationtype (
    notification_type_id INT PRIMARY KEY,
    notification_type VARCHAR(100) NOT NULL
);

CREATE TABLE Notification (
    notification_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(30),
    notification_type_id INT,
    Timestamp DATETIME NOT NULL,
    food_name VARCHAR(100) NOT NULL,
    FOREIGN KEY (notification_type_id) REFERENCES Notificationtype(notification_type_id),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (food_name) REFERENCES Food(food_name)
);