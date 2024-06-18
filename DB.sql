USE foodApp;
DROP TABLE `User`;
DROP TABLE `Menu`;
DROP TABLE `Food`;
DROP TABLE `Feedback`;
DROP TABLE `Notification`;
DROP TABLE `Notificationtype`;
DROP TABLE `RecommendedFood`;

CREATE TABLE User(
    user_id VARCHAR(30),
    user_name VARCHAR(30),
    password VARCHAR(18),
    role VARCHAR(10),
    PRIMARY KEY(user_id)
)

INSERT INTO User (user_id, user_name, password, role) VALUES 
(1, 'Pablo', 'pablo_admin', 'Admin'),
(2, 'Tarak', 'tarak_employee', 'Employee'),
(3, 'Ankit', 'ankit_chef', 'Chef');

CREATE TABLE Menu (
    menu_id INT PRIMARY KEY,
    menu_name VARCHAR(100) NOT NULL,
    Timestamp DATETIME NOT NULL
);
INSERT INTO Menu (menu_id, menu_name, Timestamp) VALUES 
(2, 'RecommendedMenu', NOW());
CREATE TABLE Food (
    food_name VARCHAR(100)  PRIMARY KEY NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    availability_status BOOLEAN NOT NULL,
    avg_rating DECIMAL(3, 2) NOT NULL,
    food_type VARCHAR(100) NOT NULL,
    menu_id INT,
    FOREIGN KEY (menu_id) REFERENCES Menu(menu_id)
);
INSERT INTO Food (food_name, price, availability_status, avg_rating, food_type, menu_id) VALUES 
('Pancakes', 5.99, TRUE, 0, 'Breakfast', 1),
('Omelette', 6.99, TRUE, 0, 'Breakfast', 1),
('French Toast', 7.49, TRUE, 0, 'Breakfast', 1),
('Burger', 8.99, TRUE, 0, 'Lunch', 1),
('Caesar Salad', 7.99, TRUE, 0, 'Lunch', 1),
('Chicken Sandwich', 9.49, TRUE, 0, 'Lunch', 1),
('Steak', 14.99, FALSE, 0, 'Dinner', 1),
('Grilled Salmon', 16.99, TRUE, 0, 'Dinner', 1),
('Pasta Carbonara', 13.99, TRUE, 0, 'Dinner', 1),
('Tiramisu', 6.49, TRUE, 0, 'Dessert', 1);

INSERT INTO Menu (menu_id, menu_name, Timestamp) VALUES 
(1, 'RecommendedMenu', NOW());

CREATE TABLE Vote (
    user_id VARCHAR(30) PRIMARY KEY,
    have_voted BOOLEAN 
);

CREATE TABLE RecommendedFood (
    food_name VARCHAR(100) PRIMARY KEY,
    total_vote INT
);

CREATE TABLE Feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(300) NOT NULL,
    rating INT NOT NULL,
    sentiment VARCHAR(300),
    is_liked BOOLEAN,
    user_id VARCHAR(30),
    food_name VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (food_name) REFERENCES Food(food_name)
);



CREATE TABLE Notificationtype (
    notification_type_id INT PRIMARY KEY,
    notification_type VARCHAR(100) NOT NULL
);


CREATE TABLE Notification (
    notification_id INT PRIMARY KEY,
    notification_message TEXT NOT NULL,
    notification_type_id INT,
    Timestamp DATETIME NOT NULL,
    FOREIGN KEY (notification_type_id) REFERENCES Notificationtype(notification_type_id)
);