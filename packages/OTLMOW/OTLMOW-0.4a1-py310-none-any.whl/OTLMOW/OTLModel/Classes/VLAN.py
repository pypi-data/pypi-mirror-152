# coding=utf-8
from OTLMOW.OTLModel.Classes.NaampadObject import NaampadObject
from OTLMOW.GeometrieArtefact.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VLAN(NaampadObject, GeenGeometrie):
    """Binnen de L2 access structuur vormt de VLAN een specifieke virtuele LAN. De toepassingen zijn verbonden met een specifieke VLAN.   Rechtstreekse communicatie tussen toepassingen is enkel mogelijk indien deze zijn verbonden met dezelfde VLAN."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VLAN'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        NaampadObject.__init__(self)
        GeenGeometrie.__init__(self)
