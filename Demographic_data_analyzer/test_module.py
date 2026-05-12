import unittest
from demographic_data_analyzer import calculate_demographic_data


class DemographicAnalyzerTestCase(unittest.TestCase):
    def setUp(self):
        self.result = calculate_demographic_data(print_data=False)

    def test_returns_dictionary(self):
        self.assertIsInstance(self.result, dict)

    def test_has_race_count(self):
        self.assertIn("race_count", self.result)

    def test_has_average_age_men(self):
        self.assertIn("average_age_men", self.result)

    def test_has_percentage_bachelors(self):
        self.assertIn("percentage_bachelors", self.result)

    def test_has_higher_education_rich(self):
        self.assertIn("higher_education_rich", self.result)

    def test_has_lower_education_rich(self):
        self.assertIn("lower_education_rich", self.result)

    def test_has_min_work_hours(self):
        self.assertIn("min_work_hours", self.result)

    def test_has_rich_percentage(self):
        self.assertIn("rich_percentage", self.result)

    def test_has_highest_earning_country(self):
        self.assertIn("highest_earning_country", self.result)

    def test_has_highest_earning_country_percentage(self):
        self.assertIn("highest_earning_country_percentage", self.result)

    def test_has_top_IN_occupation(self):
        self.assertIn("top_IN_occupation", self.result)


if __name__ == "__main__":
    unittest.main()
