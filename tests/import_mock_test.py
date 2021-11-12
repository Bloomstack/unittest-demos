import unittest
from unittest.mock import MagicMock, patch
from complex import IamComplex

class TestComplex(unittest.TestCase):

    @patch.object(IamComplex, "method1", MagicMock(return_value="Some other value"))
    def test_complex_method1_unexpected_value(self):
        # This demonstrates how to patch a method in the IamComplex class so it returns
        # something unexpected to how the method should have worked

        obj = IamComplex()

        self.assertFalse(obj.method1() == "I am method 1", "Got an unexpected value!")

    def test_complex_method1_expected_value(self):
        # This demonstrates a simple function return check

        obj = IamComplex()

        self.assertTrue(obj.method1() == "I am method 1", "Got an unexpected value!")

    def test_complex_fetch_doc_success(self):
        # This demonstrates a method doing work on a doctype and returning True
        # if that processing is correct
        # NOTE: This is not a pure unit test! we are allowing frappe.get_doc to run!

        obj = IamComplex()

        self.assertTrue(obj.fetch_some_doc_and_do_work(), "Fetching doc was not successfull")

    @patch("complex.get_doc", MagicMock(return_value={}))
    def test_complex_fetch_doc_fail(self):
        # Same as above, except we are testing by providing bad data to frappe.get_doc
        obj = IamComplex()

        self.assertFalse(obj.fetch_some_doc_and_do_work(), "Did not detect bad data!")
        
    def test_counting_results_success(self):
        # This demonstrates a method that counts results returned by get_all
        # NOTE: this is not a pure unit test! we are allowing frappe.get_all to run!

        obj = IamComplex()

        self.assertTrue(obj.fetch_and_count_data() == 10, "Did not return 10 results")

    @patch("complex.get_all", MagicMock(return_value=[]))
    def test_counting_results_fail(self):
        # This demonstrates the oposite as above by returning empty result from get_all

        obj = IamComplex()

        self.assertFalse(obj.fetch_and_count_data() == 10, "Returned 10 results, a failure was expected...")
