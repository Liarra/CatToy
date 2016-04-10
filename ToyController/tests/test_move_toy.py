from unittest import TestCase


class test_move_toy(TestCase):
    def test_move_toy_late_command(self):
        from ToyController.executables import toy_controller

        toy_controller.last_request_number = 100

        result = toy_controller.move_toy(3, 99)
        self.assertEquals(result, toy_controller.LATE_REQUEST)

        result = toy_controller.move_toy(2, 0)
        self.assertEquals(result, toy_controller.LATE_REQUEST)
