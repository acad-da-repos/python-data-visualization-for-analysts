
import unittest
import pandas as pd
import matplotlib.pyplot as plt
from assignment import create_line_plot, create_histogram, create_scatter_plot

class TestDataVisualization(unittest.TestCase):
    def setUp(self):
        # Create a sample dataframe
        self.df = pd.DataFrame({
            'Date': pd.to_datetime(['2023-01-01', '2023-01-02', '2023-01-03']),
            'Value': [10, 20, 15],
            'Value1': [1, 2, 3],
            'Value2': [4, 5, 6]
        })

    def test_create_line_plot(self):
        # This is a visual test, so we just check if the function runs without errors
        try:
            create_line_plot(self.df)
            plt.close()
        except Exception as e:
            self.fail(f"create_line_plot raised an exception: {e}")

    def test_create_histogram(self):
        # This is a visual test, so we just check if the function runs without errors
        try:
            create_histogram(self.df)
            plt.close()
        except Exception as e:
            self.fail(f"create_histogram raised an exception: {e}")

    def test_create_scatter_plot(self):
        # This is a visual test, so we just check if the function runs without errors
        try:
            create_scatter_plot(self.df)
            plt.close()
        except Exception as e:
            self.fail(f"create_scatter_plot raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
