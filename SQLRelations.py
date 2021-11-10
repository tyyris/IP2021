from sqlalchemy import declarative_base, Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()

class Main(Base):
     __tablename__ = 'Main_table'

     id = Column(Integer, primary_key=True)
     patient = Column(Integer, ForeignKey('Patient.id'))  #PatientId
     Study = Column(Integer, ForeignKey('Study.id'))    #StudyId
     Series = Column(Integer, ForeignKey('Series.id'))   #SeriesId
     Image = Column(Integer, ForeignKey('Image.id'))    #imageId
     Equipment = Column(Integer, ForeignKey('Equipment.id'))#EquipmentId
     Features = Column(Integer, ForeignKey('Annotation.tissue_classes')) #FeatureBody



class Patient(Base):
     __tablename__ = 'Patient'

     id = Column(Integer, primary_key=True)
     name = Column(String)
     DateOfBirth = Column(Integer)

class Study(Base):
    __tablename__ = 'Study'

    id = Column(Integer, primary_key=True)
    diagnosis = Column(String)
    notes = Column(String)
    timestamp = Column(String)


class Series(Base):
     __tablename__ = 'Series'

     id = Column(Integer, primary_key=True)
     acquisition_type = Column(String)
     environment = Column(String)
     light_intensity = Column(String)
     magnification = Column(String)
     focal_length = Column(Integer)
     
class Image(Base):
     __tablename__ = 'Image'

     id = Column(Integer, primary_key=True)
     reference = Column(String)
     data_size = Column(Integer)
     resolution = Column(String)
     bands = Column(Integer)
     bandpass_range = Column(Integer)
     frames = Column(Integer)
     annotion = Column(Integer, ForeignKey('Annotation.id'))


class Equipment(Base):
     __tablename__ = 'Equipment'

     id = Column(Integer, primary_key=True)
     HSI_camera = Column(String)
     system_name = Column(String)
     HSI_adapter = Column(String)
     software = Column(String)
     software_version = Column(String)
     HSI_sequence_name = Column(String)
     HSI_sequence_version = Column(String)


class Annotation(Base):
     __tablename__ = 'Annotation'

     id = Column(Integer, primary_key=True)
     reference = Column(String)
     file_type = Column(String)
     label_library_version = Column(String)
     tissue_classes = Column(Integer)
     class_features = Column(Integer)
     annotation_rate = Column(Integer)
     notes = Column(String)
