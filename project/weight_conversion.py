class WeightConverter:
    def __init__(self):
        self.conversion_rates = {
            "Kilogram (kg)": {
                "Kilogram (kg)": 1,
                "Gram (g)": 1000,
                "Pound (lbs)": 2.20462,
                "Ounce (oz)": 35.27396,
                "Ton (t)": 0.001,
            },
            "Gram (g)": {
                "Kilogram (kg)": 0.001,
                "Gram (g)": 1,
                "Pound (lbs)": 0.00220462,
                "Ounce (oz)": 0.03527396,
                "Ton (t)": 0.000001,
            },
            "Pound (lbs)": {
                "Kilogram (kg)": 0.453592,
                "Gram (g)": 453.592,
                "Pound (lbs)": 1,
                "Ounce (oz)": 16,
                "Ton (t)": 0.000453592,
            },
            "Ounce (oz)": {
                "Kilogram (kg)": 0.0283495,
                "Gram (g)": 28.3495,
                "Pound (lbs)": 0.0625,
                "Ounce (oz)": 1,
                "Ton (t)": 0.0000283495,
            },
            "Ton (t)": {
                "Kilogram (kg)": 1000,
                "Gram (g)": 1000000,
                "Pound (lbs)": 2204.62,
                "Ounce (oz)": 35273.96,
                "Ton (t)": 1,
            },
        }

    def convert_weight(self, input_weight, convert_from, convert_to):
        converted_weight = (
            input_weight * self.conversion_rates[convert_from][convert_to]
        )

        return converted_weight
