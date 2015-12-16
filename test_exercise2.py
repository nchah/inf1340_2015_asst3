#!/usr/bin/env python3

""" Module to test papers.py  """

__author__ = "Kei'ichiro Yamamoto, Albert Tai, Niel Chah"
__email__ = "keiichiro.yamamoto@mail.utoronto.ca, albert.tai@mail.utoronto.ca, niel.chah@mail.utoronto.ca"
__copyright__ = "2015 Kei'ichiro Yamamoto, Albert Tai, Niel Chah"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import pytest
import os
from exercise2 import decide, is_more_than_x_years_ago, valid_passport_format, valid_visa_format, valid_date_format

if os.name == 'nt':
    DIR = "test_json\\" # Windows
else:
    DIR = "test_jsons/" # other (unix)

# DIR = "test_jsons/"
os.chdir(DIR)


def test_returning():
    """
    Travellers are returning to KAN.
    """
    assert decide("test_returning_citizen.json", "countries.json") ==\
        ["Accept", "Accept", "Quarantine"]

def test_correct_date_format():
	"""
	Test to see if different dates are accepted.
	"""
	try:
		assert valid_date_format("2015-02-22") 
	except True:
		return True

	try:	
		assert valid_date_format("2012-30-40")
	except False:
		return True

	try:
		assert valid_date_format(2015-02-22)
	except TypeError:
		return True	

def test_correct__visa_format():
	"""
	Test to see if the visa is accepted
	"""
	
	try:
		assert correct__visa_format("CFR6X-XSMVA")
	except True:
		return True

	try:
		assert correct__visa_format(99999-9999)
	except TypeError:
		return True