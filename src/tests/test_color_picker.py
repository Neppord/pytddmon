import unittest
from pytddmon import ColorPicker

class test_pulse(unittest.TestCase):

	def setUp(self):
		self.color_picker = ColorPicker()

	def test_starts_with_light_color(self):
		(light, color) = self.color_picker.pick()
		self.assertTrue(light)
		
	def test_dark_after_pulse(self):
		self.color_picker.pulse()
		(light, color) = self.color_picker.pick()
		self.assertFalse(light)
		
	def test_no_failing_test_picks_green(self):
		self.color_picker.set_result(1, 1)
		(light, color) = self.color_picker.pick()
		self.assertEqual(color, 'green')
		
	def test_one_failing_test_picks_red(self):
		self.color_picker.set_result(1, 2)
		(light, color) = self.color_picker.pick()
		self.assertEqual(color, 'red')
		
	def test_two_failing_tests_picks_gray(self):
		self.color_picker.set_result(1, 3)
		(light, color) = self.color_picker.pick()
		self.assertEqual(color, 'gray')
		
	def test_changing_color_resets_pulse(self):
		self.color_picker.set_result(1,1)
		self.color_picker.pulse()
		self.color_picker.set_result(1,2)
		(light, color) = self.color_picker.pick()
		self.assertTrue(light)
		
	def test_default_color_is_green(self):
		self.color_picker = ColorPicker()
		(light, color) = self.color_picker.pick()
		self.assertEqual('green', color)
		
	def test_no_tests_means_green(self):
		self.color_picker.set_result(0,0)
		(light, color) = self.color_picker.pick()
		self.assertEqual('green', color)
		
	def test_pulse_is_not_reset_if_colors_stays_same(self):
		self.color_picker.pulse()
		self.color_picker.set_result(1,1)
		self.color_picker.set_result(1,1)
		(light, color) = self.color_picker.pick()
		self.assertFalse(light)

