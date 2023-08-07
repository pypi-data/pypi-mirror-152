from csv import reader

from OTLMOW.Facility.FileFormats.EMInfraImporter import EMInfraImporter
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.OTLModel.Classes.Camera import Camera
from OTLMOW.OTLModel.Classes.Netwerkpoort import Netwerkpoort
from OTLMOW.OTLModel.Classes.Sturing import Sturing

if __name__ == '__main__':
    otl_facility = OTLFacility(logfile=r'C:\temp\pythonLogging\pythonlog.txt',
                               settings_path="C:\\resources\\settings_OTLMOW.json",
                               enable_relation_features=True)

    uuid_file_path = 'C:\\resources\\202204262158_sturingsrelaties_netwerkpoorten.csv'

    relaties = []

    with open(uuid_file_path, 'r') as uuidfile:
        csv_reader = reader(uuidfile, delimiter='\t')
        for row in csv_reader:
            if row[0] == 'column1':
                continue
            if row[1] == '' or row[3] == '':
                continue
            camera = Camera()
            camera.assetId.identificator = EMInfraImporter.get_asset_id_from_uuid_and_typeURI(row[3], Camera.typeURI)
            poort = Netwerkpoort()
            poort.assetId.identificator = EMInfraImporter.get_asset_id_from_uuid_and_typeURI(row[1], Netwerkpoort.typeURI)

            sturingsrelatie = otl_facility.relatie_creator.create_relation(bron=poort, doel=camera, relatie=Sturing)
            relaties.append(sturingsrelatie)

    otl_facility.jsonExporter.export_objects_to_json_file(relaties, 'C:\\resources\\sturingsrelaties_poort_camera.json')

