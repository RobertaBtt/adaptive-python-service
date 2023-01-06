import json


class SerializeJSON:

    @staticmethod
    def convert(input_data: list):
        return json.dumps(input_data)

    @staticmethod
    def from_str_to_list(input_str):
        return input_str.strip('][').replace("'", "").split(', ')
