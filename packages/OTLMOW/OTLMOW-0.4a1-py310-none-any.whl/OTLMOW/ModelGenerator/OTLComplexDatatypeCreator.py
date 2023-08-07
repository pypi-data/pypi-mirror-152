import logging

from OTLMOW.ModelGenerator.AbstractDatatypeCreator import AbstractDatatypeCreator
from OTLMOW.ModelGenerator.OSLOCollector import OSLOCollector
from OTLMOW.ModelGenerator.OSLODatatypeComplex import OSLODatatypeComplex


class OTLComplexDatatypeCreator(AbstractDatatypeCreator):
    def __init__(self, osloCollector: OSLOCollector):
        super().__init__(osloCollector)
        logging.info("Created an instance of OTLComplexDatatypeCreator")

    def CreateBlockToWriteFromComplexTypes(self, osloDatatypeComplex: OSLODatatypeComplex):
        if not isinstance(osloDatatypeComplex, OSLODatatypeComplex):
            raise ValueError(f"Input is not a OSLODatatypeComplex")

        if osloDatatypeComplex.objectUri == '' or not (osloDatatypeComplex.objectUri == 'https://schema.org/ContactPoint' or
                                                       osloDatatypeComplex.objectUri == 'https://schema.org/OpeningHoursSpecification' or
                                                       (osloDatatypeComplex.objectUri.startswith(
                                                           'https://wegenenverkeer.data.vlaanderen.be/ns/') and 'Dtc' in osloDatatypeComplex.objectUri)):
            raise ValueError(f"OSLODatatypeComplex.objectUri is invalid. Value = '{osloDatatypeComplex.objectUri}'")

        if osloDatatypeComplex.name == '':
            raise ValueError(f"OSLODatatypeComplex.name is invalid. Value = '{osloDatatypeComplex.name}'")

        if osloDatatypeComplex.objectUri.startswith(
                'https://wegenenverkeer.data.vlaanderen.be/ns/') and 'Dtc' in osloDatatypeComplex.objectUri:
            return self.CreateBlockToWriteFromComplexPrimitiveOrUnionTypes(osloDatatypeComplex, typeField='Complex')
        elif osloDatatypeComplex.objectUri.startswith('https://schema.org/'):
            return self.CreateBlockToWriteFromComplexPrimitiveOrUnionTypes(osloDatatypeComplex, typeField='Complex')
        else:
            raise NotImplementedError

    @staticmethod
    def getEenheidFromConstraints(constraints: str):
        if constraints == '':
            raise ValueError
        split_text = constraints.split('"')
        return split_text[1]
