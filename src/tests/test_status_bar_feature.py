﻿# coding: utf-8
import unittest

import mock

import pytddmon


class TestStatusBarFeature(unittest.TestCase):

    def _test_gui_should_contain_a_status_bar(self):
        # This test creates an X error in a running pytddmon session
        gui = pytddmon.TkGUI(mock.Mock())
        self.assertTrue(hasattr(gui, 'status_bar'))

    def test_pytddmon_should_have_get_status_message_function(self):
        self.assertTrue(hasattr(pytddmon.Pytddmon, 'get_status_message'))


if __name__ == '__main__':
    unittest.main()
