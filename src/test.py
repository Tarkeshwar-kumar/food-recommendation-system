import unittest
from unittest.mock import Mock, patch


class TestHandlers(unittest.TestCase):

    def test_handle_add_item_to_menu_success(self, mock_add_item_to_menu, MockAddItemNotification, mock_food_exists_in_menu):
        
        mock_food_exists_in_menu.return_value = False
        mock_notification = MockAddItemNotification.return_value
        user = Mock()

        json_data = {
            "food_name": "Pizza",
            "price": 9.99,
            "food_type": "Italian"
        }

        
        response = handle_add_item_to_menu(user, json_data)

        mock_add_item_to_menu.assert_called_once()
        mock_notification.send_notification.assert_called_once_with("Pizza")
        self.assertEqual(response, {"status": "success"})

    def test_handle_add_item_to_menu_food_already_exists(self, mock_food_exists_in_menu):

        mock_food_exists_in_menu.return_value = True
        user = Mock()

        json_data = {
            "food_name": "Pizza",
            "price": 9.99,
            "food_type": "Italian"
        }

        
        response = handle_add_item_to_menu(user, json_data)

        # Assert
        self.assertEqual(response, {"status": "error", "message": "Pizza already exists"})

    def test_handle_add_item_to_menu_missing_field(self):
        user = Mock()
        json_data = {
            "price": 9.99,
            "food_type": "Italian"
        }

        response = handle_add_item_to_menu(user, json_data)

        self.assertEqual(response, {"status": "error", "message": "Missing required field: 'food_name'"})

    def test_handle_add_item_to_menu_invalid_price(self):

        user = Mock()
        json_data = {
            "food_name": "Pizza",
            "price": "invalid_price",
            "food_type": "Italian"
        }

       
        response = handle_add_item_to_menu(user, json_data)

        # Assert
        self.assertTrue("Invalid value" in response["message"])


    def test_handle_request_add_item_to_menu_success(self, mock_handle_add_item_to_menu):

        mock_handle_add_item_to_menu.return_value = {"status": "success"}
        user = Mock()
        json_data = {
            "request_type": "add_item_to_menu",
            "food_name": "Pizza",
            "price": 9.99,
            "food_type": "Italian"
        }

        response = handle_request(user, json_data)

        mock_handle_add_item_to_menu.assert_called_once_with(user, json_data)
        self.assertEqual(response, {"status": "success"})

    
    def test_handle_request_invalid_request_type(self, mock_handle_add_item_to_menu):

        user = Mock()
        json_data = {
            "request_type": "invalid_request_type"
        }

       
        response = handle_request(user, json_data)

        mock_handle_add_item_to_menu.assert_not_called()
        self.assertEqual(response, {"status": "error", "message": "Invalid request type"})

if __name__ == '__main__':
    unittest.main()
