class LengthConverter:
    def __init__(self):
        self.conversion_rates = {
            "Kilometer (km)": {
                "Kilometer (km)": 1,
                "Meter (m)": 1000,
                "Centimeter (cm)": 100000,
                "Inch (in)": 39370.1,
                "Foot (ft)": 3280.84,
            },
            "Meter (m)": {
                "Kilometer (km)": 0.001,
                "Meter (m)": 1,
                "Centimeter (cm)": 100,
                "Inch (in)": 39.3701,
                "Foot (ft)": 3.28084,
            },
            "Centimeter (cm)": {
                "Kilometer (km)": 0.00001,
                "Meter (m)": 0.01,
                "Centimeter (cm)": 1,
                "Inch (in)": 0.393701,
                "Foot (ft)": 0.0328084,
            },
            "Inch (in)": {
                "Kilometer (km)": 0.0000254,
                "Meter (m)": 0.0254,
                "Centimeter (cm)": 2.54,
                "Inch (in)": 1,
                "Foot (ft)": 0.0833333,
            },
            "Foot (ft)": {
                "Kilometer (km)": 0.0003048,
                "Meter (m)": 0.3048,
                "Centimeter (cm)": 30.48,
                "Inch (in)": 12,
                "Foot (ft)": 1,
            },
        }

    def convert_length(self, input_length, convert_from_2, convert_to_2):
        converted_length = (
            input_length * self.conversion_rates[convert_from_2][convert_to_2]
        )

        return converted_length
