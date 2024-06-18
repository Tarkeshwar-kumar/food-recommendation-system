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

INSERT INTO User (user_id, user_name, password, role) VALUES 
(7, 'Venkat', 'venkat_employee', 'Employee'),
(8, 'Harshita', 'harshita_employee', 'Employee'),
(9, 'Kader', 'kader_employee', 'Employee');

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
    avg_sentiment VARCHAR(10) NOT NULL,
    food_type VARCHAR(100) NOT NULL,
    menu_id INT,
    FOREIGN KEY (menu_id) REFERENCES Menu(menu_id)
);

INSERT INTO Food (food_name, price, availability_status, avg_rating, avg_sentiment, food_type, menu_id) VALUES 
('Pancakes', 5.99, TRUE, 0, "OK", 'Breakfast', 1),
('Omelette', 6.99, TRUE, 0, "OK", 'Breakfast', 1),
('French Toast', 7.49, TRUE, 0,"OK", 'Breakfast', 1),
('Burger', 8.99, TRUE, 0,"OK", 'Lunch', 1),
('Caesar Salad', 7.99, TRUE, 0,"OK", 'Lunch', 1),
('Chicken Sandwich', 9.49, TRUE, 0,"OK", 'Lunch', 1),
('Steak', 14.99, FALSE, 0, "OK",'Dinner', 1),
('Grilled Salmon', 16.99, TRUE, 0, "OK",'Dinner', 1),
('Pasta Carbonara', 13.99, TRUE, 0,"OK", 'Dinner', 1),
('Tiramisu', 6.49, TRUE, 0, "OK",'Dessert', 1);


CREATE TABLE Vote (
    user_id VARCHAR(30),
    have_voted BOOLEAN,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE RecommendedFood (
    food_name VARCHAR(100),
    total_vote INT,
    FOREIGN KEY (food_name) REFERENCES Food(food_name)
);

CREATE TABLE Feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(300) NOT NULL,
    rating INT NOT NULL,
    sentiment VARCHAR(300),
    user_id VARCHAR(30),
    food_name VARCHAR(100),
    FOREIGN KEY (userfin_id) REFERENCES User(user_id),
    FOREIGN KEY (food_name) REFERENCES Food(food_name)
);



CREATE TABLE Notificationtype (
    notification_type_id INT PRIMARY KEY,
    notification_type VARCHAR(100) NOT NULL
);
INSERT INTO Notificationtype (notification_type_id, notification_type) VALUES
(1, "ADD_ITEM"),
(2, "REMOVE_ITEM"),
(3, "FOOD_AVAILABLE"),
(4, "FOOD_UNAVAILABLE");

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