import connAMPM
from fastapi import FastAPI, Query, HTTPException
import queries
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

class GuiasItem(BaseModel):
    GuiaId: str
    ClienteId: int
    LocationType: str
    Latitud: float
    Longitud: float
    TipoMovimientoOperativoId: int
    TipoCodigoPostal: int
    
class Item(BaseModel):
    GUIAS: list[GuiasItem]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*']
)


@app.get("/")
def read_root():
    return {"AMPM": "API Mapas."}

#def getAvanceTotal(campo: str = "Pendiente", orden: str = "ASC"):
#Avance Total.
@app.get("/getAvanceTotal")
def getAvanceTotal(campo: str = "Pendiente", orden: str = "ASC"):
   
   if campo in ["Total", "Avance", "Pendiente", "[%Avance]", "[%Pendiente]", "FPrimero", "FUltimo", "[Tiempo(min)]", "Tiempo", "Rutas", "Clientes"]:
      if orden in ["ASC", "DESC"]:
         
         #Validados ambos campos realiza query.
         resultado = connAMPM.doAvanceTotal()
         return resultado
      else:
         raise HTTPException(status_code=403, detail="Valor para variable 'orden' inválido. Solo puedes usar los valores 'DESC' y 'ASC' para ordenamiento.")
   else:
      raise HTTPException(status_code=403, detail="Valor para variable 'campo' inválido. Valores válidos: 'Total', 'Avance', 'Pendiente', '[%Avance]', '[%Pendiente]', 'FPrimero', 'FUltimo', '[Tiempo(min)]', 'Tiempo', 'Rutas', 'Clientes' ")

@app.post("/items")
def create_item(item: Item):
    total_sum = 0
    for totales_item in item.GUIAS:
        total_sum += totales_item.Latitud

    # Process the total_sum and other data as needed

    # Return the processed item
    return total_sum