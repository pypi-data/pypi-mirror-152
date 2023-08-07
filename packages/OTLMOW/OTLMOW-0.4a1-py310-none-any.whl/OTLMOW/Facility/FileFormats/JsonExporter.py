﻿from OTLMOW.ModelGenerator.OtlAssetJSONEncoder import OtlAssetJSONEncoder


class JsonExporter:
    def __init__(self, settings=None):
        self.encoder = OtlAssetJSONEncoder(indent=4, settings=settings)

    def export_objects_to_json_file(self, list_of_objects, file_path):
        encoded_json = self.encoder.encode(list_of_objects)
        self.encoder.write_json_to_file(encoded_json, file_path)
