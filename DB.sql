USE foodApp;
DROP TABLE `User`;
DROP TABLE `Menu`;
DROP TABLE `Food`;
DROP TABLE `Feedback`;
DROP TABLE `Notification`;
DROP TABLE `Notificationtype`;
DROP TABLE `RecommendedFood`;
drop TABLE `Vote`;

DROP TABLE `LoginAttempts`;

DROP TABLE `DiscardedFood`;


CREATE TABLE User(
    user_id VARCHAR(30),
    user_name VARCHAR(30),
    password VARCHAR(18),
    role VARCHAR(10),
    spice_level VARCHAR(100) NULL,
    tooth_type VARCHAR(100) NULL,
    foodie_type VARCHAR(100) NULL,
    preffered_type VARCHAR(100) NULL,
    PRIMARY KEY(user_id)
)


CREATE TABLE Menu (
    menu_id INT PRIMARY KEY,
    menu_name VARCHAR(100) NOT NULL,
    Timestamp DATETIME NOT NULL
);
INSERT INTO Menu (menu_id, menu_name, Timestamp) VALUES
(1, "MainMenu", NOW());

CREATE TABLE Food (
    food_name VARCHAR(100)  PRIMARY KEY NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    availability_status BOOLEAN NOT NULL,
    avg_rating DECIMAL(3, 2) NOT NULL,
    avg_sentiment VARCHAR(10) DEFAULT 'Neutral',
    food_type VARCHAR(100) NOT NULL,
    menu_id INT,
    spice_level VARCHAR(30) NOT NULL,
    is_sweet BOOLEAN NOT NULL,
    region VARCHAR(30) NOT NULL,
    FOREIGN KEY (menu_id) REFERENCES Menu(menu_id)
);


CREATE TABLE Vote (
    user_id VARCHAR(30),
    have_voted BOOLEAN,
    food_name VARCHAR(30),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (food_name) REFERENCES Food(food_name) ON DELETE CASCADE
);

CREATE TABLE RecommendedFood (
    food_name VARCHAR(100),
    total_vote INT,
    FOREIGN KEY (food_name) REFERENCES Food(food_name) ON DELETE CASCADE
);

CREATE TABLE Feedback (
    feedback_id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(300) NOT NULL,
    rating FLOAT NOT NULL,
    sentiment VARCHAR(300),
    user_id VARCHAR(30),
    food_name VARCHAR(100),
    FOREIGN KEY (user_id) REFERENCES User(user_id),
    FOREIGN KEY (food_name) REFERENCES Food(food_name) ON DELETE CASCADE,
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
    FOREIGN KEY (food_name) REFERENCES Food(food_name) ON DELETE CASCADE
);

CREATE TABLE LoginAttempts (
    login_attemp_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(30),
    attempt_type VARCHAR(10) NOT NULL,
    status BOOLEAN NOT NULL,
    Timestamp DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES User(user_id)
);

CREATE TABLE DiscardedFood (
    food_name VARCHAR(100),
    avg_rating DECIMAL(3, 2) NOT NULL,
    avg_sentiment VARCHAR(10) DEFAULT 'Neutral',
    FOREIGN KEY (food_name) REFERENCES Food(food_name) ON DELETE CASCADE
);

CREATE TABLE AuditFeedback (
    user_id VARCHAR(30),
    food_name VARCHAR(100),
    didnt_liked VARCHAR(250) NOT NULL,
    like_to_taste VARCHAR(600) NOT NULL,
    recipe VARCHAR(600) NOT NULL,
    FOREIGN KEY (food_name) REFERENCES Food(food_name) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES User(user_id) ON DELETE CASCADE
);

INSERT INTO Food (food_name, price, availability_status, avg_rating, food_type, menu_id, spice_level, is_sweet, region) VALUES 
('Pancakes', 50, TRUE, 0, 'Veg', 1, "Low", False, "other"),
('Omelette', 20, TRUE, 0, 'Egg', 1, "Medium", False, "other"),
('French Toast', 50, TRUE, 0, 'Veg', 1, "Low", False, "other"),
('Chicken Burger', 100, TRUE, 0, 'Non Veg', 1, "Medium", False, "other"),
('Caesar Salad', 30, TRUE, 0, 'Veg', 1, "Low", False, "other"),
('Chicken Sandwich', 60, TRUE, 0, 'Non Veg', 1, "Medium", False, "other"),
('Steak', 150, FALSE, 0,'Non Veg', 1, "Medium", False, "other"),
('Grilled Salmon', 150, TRUE, 0, 'Non Veg', 1, "Medium", False, "other"),
('Pasta Carbonara', 200, TRUE, 0, 'Veg', 1, "Medium", False, "other"),
('Tiramisu', 180, TRUE, 0, 'Egg', 1, "Low", True, "other"),
('Kadhai Panner', 250, TRUE, 0, 'Veg', 1, "High", False, "North Indian"),
('Kadhai Chicken', 270, TRUE, 0, 'Veg', 1, "High", False, "North Indian"),
('Mysore Dosa', 90, TRUE, 0, 'Veg', 1, "High", False, "South Indian");

INSERT INTO User (user_id, user_name, password, role) VALUES 
(1, 'Pablo', 'pablo_admin', 'Admin'),
(2, 'Ankit', 'ankit_chef', 'Chef'),
(3, 'Tarak', 'tarak_employee', 'Employee'),
(4, 'Priyanka', 'priyanka_employee', 'Employee'),
(5, 'Ravi', 'ravi_employee', 'Employee'),
(6, 'David', 'david_employee', 'Employee'),
(7, 'Venkat', 'venkat_employee', 'Employee'),
(8, 'Harshita', 'harshita_employee', 'Employee'),
(9, 'Kader', 'kader_employee', 'Employee');

INSERT INTO Notificationtype (notification_type_id, notification_type) VALUES
(1, "ADD_ITEM"),
(2, "REMOVE_ITEM"),
(3, "FOOD_AVAILABILITY_CHANGED"),
(4, "FOOD_AUDIT");

