import unittest
from dates import Dates


class DatesTestCase(unittest.TestCase):

    def test_dates_init(self):
        test_date = dates.Dates.Date(1, "2021-04-01")
        assert test_date.date_id == 1
        assert test_date.date == "2021-04-01"

    def test_get_dates(self):
        pass

    def test_set_date(self):
        Dates.input.day = lambda _: "2021-04-01"




if __name__ == '__main__':
    unittest.main()
