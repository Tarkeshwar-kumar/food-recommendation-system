USE foodApp;
DROP TABLE `User`;
DROP TABLE `Menu`;
DROP TABLE `Food`;
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
(1, 'MainMenu', NOW());
CREATE TABLE Food (
    food_id INT PRIMARY KEY,
    food_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    availability_status BOOLEAN NOT NULL,
    avg_rating DECIMAL(3, 2) NOT NULL,
    food_type VARCHAR(100) NOT NULL,
    menu_id INT,
    FOREIGN KEY (menu_id) REFERENCES Menu(menu_id)
);
INSERT INTO Food (food_id, food_name, price, availability_status, avg_rating, food_type, menu_id) VALUES 
(1, 'Pancakes', 5.99, TRUE, 0, 'Breakfast', 1),
(2, 'Omelette', 6.99, TRUE, 0, 'Breakfast', 1),
(3, 'French Toast', 7.49, TRUE, 0, 'Breakfast', 1),
(4, 'Burger', 8.99, TRUE, 0, 'Lunch', 1),
(5, 'Caesar Salad', 7.99, TRUE, 0, 'Lunch', 1),
(6, 'Chicken Sandwich', 9.49, TRUE, 0, 'Lunch', 1),
(7, 'Steak', 14.99, FALSE, 0, 'Dinner', 1),
(8, 'Grilled Salmon', 16.99, TRUE, 0, 'Dinner', 1),
(9, 'Pasta Carbonara', 13.99, TRUE, 0, 'Dinner', 1),
(10, 'Tiramisu', 6.49, TRUE, 0, 'Dessert', 1);


CREATE TABLE Feedback (
    FeedbackID INT PRIMARY KEY,
    FeedbackMessage TEXT NOT NULL,
    UserID INT,
    Timestamp DATETIME NOT NULL,
    MenuID INT,
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (MenuID) REFERENCES Menu(MenuID)
);


CREATE TABLE Notificationtype (
    NotificationTypeID INT PRIMARY KEY,
    NotificationTypeName VARCHAR(100) NOT NULL
);


CREATE TABLE Notification (
    NotificationID INT PRIMARY KEY,
    NotificationMessage TEXT NOT NULL,
    UserID INT,
    NotificationTypeID INT,
    Timestamp DATETIME NOT NULL,
    FOREIGN KEY (UserID) REFERENCES User(UserID),
    FOREIGN KEY (NotificationTypeID) REFERENCES Notificationtype(NotificationTypeID)
);


CREATE TABLE RecommendedMenu (
    RecommendedMenuID INT PRIMARY KEY,
    MenuID INT,
    UserID INT,
    FOREIGN KEY (MenuID) REFERENCES Menu(MenuID),
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);


CREATE TABLE RecommendedFood (
    RecommendedFoodID INT PRIMARY KEY,
    FoodID INT,
    UserID INT,
    FOREIGN KEY (FoodID) REFERENCES Food(FoodID),
    FOREIGN KEY (UserID) REFERENCES User(UserID)
);
