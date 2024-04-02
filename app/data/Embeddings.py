import pandas as pd
import Split as split

class Embeddings:
    
    def __inti__(self, documentos, chunkSize, chunkOverlap):
        self.documentos = documentos
        self.chunkSize = chunkSize
        self.chunkOverlap = chunkOverlap
        split = split(documentos)

     
        

        
        