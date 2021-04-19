#!/usr/bin/python
def localidad_cercana(lat,lon):
    localidades = {
    "Arica":(-18.478333,-70.321111),
    "Putre":(-18.196389,-69.559167),
    "Iquique":(-20.212279,-70.135187),
    "Tocopilla":(-22.087792,-70.189611),
    "Calama":(-22.462500,-68.927222),
    "Mejillones":(-23.100559,-70.450375),
    "Antofagasta":(-23.616881,-70.386486),
    "Taltal":(-25.408154,-70.481137),
    "Chañaral":(-26.344727,-70.618381),
    "Caldera":(-27.067388,-70.819515),
    "Copiapó":(-27.366389,-70.332222),
    "Vallenar":(-28.575000,-70.761667),
    "Huasco":(-28.466300,-71.219100),
    "Coquimbo":(-29.969392,-71.333944),
    "Ovalle":(-30.603056,-71.203056),
    "Illapel":(-31.635725,-71.166411),
    "Los Vilos":(-31.970000,-71.503370),
    "San Felipe":(-32.750833,-70.725000),
    "Valparaíso":(-33.040331,-71.584006),
    "Santiago":(-33.450707,-70.656249),
    "Rancagua":(-34.165278,-70.739722),
    "San Fernando":(-34.583333,-70.966667),
    "Pichilemu":(-34.385888,-72.008799),
    "Curicó":(-34.983333,-71.233333),
    "Constitución":(-35.335426,-72.412391),
    "Talca":(-35.426667,-71.666111),
    "Linares":(-35.850000,-71.600000),
    "Chillán":(-36.606667,-72.103333),
    "Concepción":(-36.827222,-73.050278),
    "Los Ángeles":(-37.466667,-72.350000),
    "Temuco":(-38.750000,-72.666667),
    "Angol":(-37.798889,-72.708611),
    "Valdivia":(-39.800000,-73.233333),
    "La Unión":(-40.283333,-73.083333),
    "Puerto Montt":(-41.366667,-72.933333),
    "Osorno":(-40.566667,-73.150000),
    "Castro":(-42.482500,-73.764167),
    "Chaitén":(-42.919444,-72.708889),
    "Coyhaique":(-45.566667,-72.066667),
    "Puerto Aysén":(-45.400000,-72.683333),
    "Chile Chico":(-46.550000,-71.733333),
    "Cochrane":(-47.266667,-72.550000),
    "Puerto Natales":(-51.723611,-72.487500),
    "Punta Arenas":(-53.150000,-70.916667),
    "Porvenir":(-53.300000,-70.366667),
    "Puerto Williams":(-54.933333,-67.616667),
    "Colchane":(-19.2760613,-68.6405225),
    "Ollagüe":(-21.2245495,-68.2551806),
    "Mejillones":(23.1028944,-70.4517438),
    "San Pedro de Atacama":(-22.9139942,-68.2074409),
    "Mina Escondida":(-24.298159485571414,-69.03364704027321),
    "El Salvador":(-26.195978353373505,-69.65437456624666),
    "Combarbalá":(-31.129250270327883,-71.01118605252822),
    "San Antonio":(-33.54699629270259,-71.5550092769822),
    "Iloca":(-34.87792567366137,-72.20320262284591),
    "Cauquenes":(-35.93898237765952,-72.25264110721962),
    "Lebu":(-37.593444350624,-73.65889108610826),
    "Tirúa":(-38.295211560232104, -73.47761668070142),
    "Villarrica":(-39.2374589120438, -72.27461380337017),
    "La Junta":(-43.94230123296015, -72.39546344166793),
    "Mendoza, Argentina":(-32.79292458750816, -68.78645449617022),
    "San Juan, Argentina":(-31.425023494605583, -68.57771426981755),
    "Jujuy, Argentina":(-24.152639190086717, -65.20127150801987),
    "Salta":(-24.782042450546353, -65.4213608859298)
    }
    
    dist = 10000000
    nombre = ""
    for nombre in localidades:
        tupla = localidades[nombre]
        dist_lat = lat - tupla[0]
        dist_lon = lon - tupla[1]
        dist_km = 111.0*math.sqrt(dist_lat**2.0 + dist_lon**2.0)
        if dist_km < dist:
            dist = dist_km
            if abs(dist_lat) >= 3.0*abs(dist_lon):
                direccion = "Norte" if dist_lat>=0 else "Sur"
            elif abs(dist_lon) >= 3.0*abs(dist_lat):
                direccion = "Este" if dist_lon>=0 else "Oeste"
            else:
                prefijo = "Nor" if dist_lat>=0 else "Sur"
                sufijo = "este" if dist_lon>=0 else "oeste"
                direccion = prefijo + sufijo
            localidad_cercana_evento = "al " + direccion + " de " + nombre
    texto = "%.1f km %s" % (dist,localidad_cercana_evento)
    return texto
