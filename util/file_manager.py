import pandas as pd
import os

class CSVFileManager:
  def __init__(self, path: str):
    self.path = path
  def read(self) -> str:
    return pd.read_csv(self.path)  
  
  def write(self,dataFrame):
    ## dataFrame.to_csv(self.path, index=False) v1, me sustitía el fichero - pero es funcional
    ## dataFrame.to_csv(self.path, index=False, mode='a') V2. hacía append pero claro, me hace append del header también
    archivo_existe = os.path.exists(self.path) ## v3 y final
    dataFrame.to_csv(self.path,
                     index=False, ## evita que salga el rowid
                     mode='a', ## que sea append
                     header=not archivo_existe ## condicional para devolver true or false en función de si existe el archivo
                     )


  
