#1 import unittest and surfshop
import unittest
import surfshop
import datetime

#2 add a class which contain all of tests
class TestSurfShop(unittest.TestCase):
  #3 add setup fixture that runs before every test
  def setUp(self):
    self.cart = surfshop.ShoppingCart()

  #4 testing add_surfboards method to ensure it adds the correct number of surfboards and returns the expected message
  def test_add_surfboards(self):
    
    #10 parameterized the test so that is runs 3 times, passing 2, 3, and 4 as the arguments
    for param in [2, 3, 4]:
      with self.subTest(param=param):
        self.assertEqual(self.cart.add_surfboards(param), f'Successfully added {param} surfboards to cart!')
        self.cart = surfshop.ShoppingCart()
       
  # version without parameterization
  def test_add_surfboards_with_two_boards(self):
    self.assertEqual(self.cart.add_surfboards(2), 'Successfully added 2 surfboards to cart!')
    self.cart = surfshop.ShoppingCart()

  #first method for skipping
  @unittest.skip('This test is skipped when is off season')
  def test_add_to_many_boards_error(self):
    #9 test skipped when is off season
    off_season = True
    
    #second method for skipping is without unittest.skip decorator and with next two code lines
    #if off_season:
    #  self.skipTest('This test is skipped when is off season')
    #6 when is season this test is running
    self.assertRaises(surfshop.TooManyBoardsError, self.cart.add_surfboards, 5)

  #8 While I wait for dev team to fix this bug, I don't want it to cause my tests to fail and I mark this test as an expected failure.
  #@unittest.expectedFailure 
  #7 testing that when is called apply_locals_discount is sets locals_discount to true
  def test_apply_locals_discount(self):
    self.cart.apply_locals_discount()
    self.assertTrue(self.cart.locals_discount)

  def tearDown(self):
    self.cart = None

  #13 testing that program raises Checkout Date Error if date is not in the future
  def test_checkout_date_error(self):
    today_date = datetime.datetime.now()
    self.assertRaises(surfshop.CheckoutDateError, self.cart.set_checkout_date, today_date)

unittest.main()

  
