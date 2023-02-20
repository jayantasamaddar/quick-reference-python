class Person:
    def __init__(self, dictionary):
        # Check if argument passed is a dictionary
        if not(isinstance(dictionary, dict)):
            raise TypeError('Unexpected Type: Dictionary expected')

        # Helper dictionaries to verify type
        ## Mandatory attributes
        mandatory_attr = {
            'fname': str,
            'lname': str,
            'age': int
        }.items()
        ## Optional attributes
        optional_attr = {
            'is_student': bool
        }.items()

        # Loop to validate and set mandatory attributes
        for key, value in mandatory_attr:
            # Validation 1: Check if key is in the dictionary
            if key not in dictionary:
                raise KeyError(f"Expected Mandatory keys: {', '.join(mandatory_attr.keys())}")

            # Set instance attribute
            setattr(self, key, value(dictionary[key]))

        # Loop to set optional attributes (if any)
        for key, value in optional_attr:
            # Continue running through the optional attributes
            if key not in dictionary: continue

            # Set instance attribute
            setattr(self, key, value(dictionary[key]))