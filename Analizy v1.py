import numpy as np
import pandas as pd

#wczytanie dataframe z CSV
df = pd.read_csv("data/3 ZMIANA_czyste.csv", sep=';')

#czyszczenie df jesli nie jest czyste
#zmiana przecinków na kropki
df = df.apply(lambda x: x.str.replace(',','.'))
#zmiana wartosci ze str na float
df.iloc[:,2:] = df.iloc[:,2:].astype(float)

osoba = str.upper(input("Dla jakiej osoby utworzyc analize? "))
lista_osob = "ABCDEFGHIJ"
numerosoby = lista_osob.find(osoba)

# stworzenie df z odpowiedziami jednej osoby na wszystkie miesiące
df_osoba = df.loc[df.iloc[:, 1] == lista_osob[numerosoby]]

# na ile miesięcy odpowiedziała OB? stworzenie listy z miesiącami
lista_miesiecy = list(df_osoba.iloc[:,0])
print(lista_miesiecy)

# stworzenie pliku dla SocNetV
nazwapliku = "Analiza_" + osoba + ".graphml"
plik = open(nazwapliku, "w+")

# zapis wartości domyślnych
plik.write("""<?xml version="1.0" encoding="UTF-8"?> 
 <!-- Created by SocNetV 2.5 --> 
<graphml xmlns="http://graphml.graphdrawing.org/xmlns"       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance "       xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns       http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">
  <key id="d0" for="node" attr.name="label" attr.type="string"> 
    <default></default> 
  </key> 
  <key id="d1" for="node" attr.name="x_coordinate" attr.type="double"> 
    <default>0.0</default> 
  </key> 
  <key id="d2" for="node" attr.name="y_coordinate" attr.type="double"> 
    <default>0.0</default> 
  </key> 
  <key id="d3" for="node" attr.name="size" attr.type="double"> 
    <default>7</default> 
  </key> 
  <key id="d4" for="node" attr.name="color" attr.type="string"> 
    <default>red</default> 
  </key> 
  <key id="d5" for="node" attr.name="shape" attr.type="string"> 
    <default>circle</default> 
  </key> 
  <key id="d6" for="node" attr.name="label.color" attr.type="string"> 
    <default>#8d8d8d</default> 
  </key> 
  <key id="d7" for="node" attr.name="label.size" attr.type="string"> 
    <default>8</default> 
  </key> 
  <key id="d8" for="edge" attr.name="weight" attr.type="double"> 
    <default>1.0</default> 
  </key> 
  <key id="d9" for="edge" attr.name="color" attr.type="string"> 
    <default>#666666</default> 
  </key> 
  <key id="d10" for="edge" attr.name="label" attr.type="string"> 
    <default></default> 
  </key> """)

#zapis dla poszczegolnym miesiecy
for miesiac in lista_miesiecy:
    print("Zapisuje dla: ", miesiac)

    #stworzenie grafu
    plik.write("""
  <graph id="%s" edgedefault="undirected">""" % (miesiac))

    #zapis kropek
    plik.write("""
    <node id="1"> 
      <data key="d0">A</data>
      <data key="d1">0.782303</data>
      <data key="d2">0.5</data>
      <data key="d5">circle</data>
    </node>
    <node id="2"> 
      <data key="d0">B</data>
      <data key="d1">0.728388</data>
      <data key="d2">0.773483</data>
      <data key="d5">circle</data>
    </node>
    <node id="3"> 
      <data key="d0">C</data>
      <data key="d1">0.587237</data>
      <data key="d2">0.942505</data>
      <data key="d5">circle</data>
    </node>
    <node id="4"> 
      <data key="d0">D</data>
      <data key="d1">0.412763</data>
      <data key="d2">0.942505</data>
      <data key="d5">circle</data>
    </node>
    <node id="5"> 
      <data key="d0">E</data>
      <data key="d1">0.271612</data>
      <data key="d2">0.773483</data>
      <data key="d5">circle</data>
    </node>
    <node id="6"> 
      <data key="d0">F</data>
      <data key="d1">0.217697</data>
      <data key="d2">0.5</data>
      <data key="d5">circle</data>
    </node>
    <node id="7"> 
      <data key="d0">G</data>
      <data key="d1">0.271612</data>
      <data key="d2">0.226517</data>
      <data key="d5">circle</data>
    </node>
    <node id="8"> 
      <data key="d0">H</data>
      <data key="d1">0.412763</data>
      <data key="d2">0.0574945</data>
      <data key="d5">circle</data>
    </node>
    <node id="9"> 
      <data key="d0">I</data>
      <data key="d1">0.587237</data>
      <data key="d2">0.0574945</data>
      <data key="d5">circle</data>
    </node>
    <node id="10"> 
      <data key="d0">J</data>
      <data key="d1">0.728388</data>
      <data key="d2">0.226517</data>
      <data key="d5">circle</data>
    </node>""")

    czy_miesiac = df_osoba["Kolumna1"] == miesiac
    df_osoba_miesiac = df_osoba[czy_miesiac]
    print(df_osoba_miesiac.iloc[0,2])

    #zapis relacji
    id_relacji = 1
    for x in range (1, 11):
        for y in range (x, 10):
            if df_osoba_miesiac.iloc[0, id_relacji+1] < 2:
                kolor = "#BDBDBD"
            elif df_osoba_miesiac.iloc[0, id_relacji+1] < 8:
                kolor = "#6E6E6E"
            else:
                kolor = "#000000"
            plik.write("""
    <edge id="e%d" directed="false" source="%d" target="%d">
      <data key="d8">%s</data> 
      <data key="d9">%s</data> 
    </edge>""" % (id_relacji, x, y+1, df_osoba_miesiac.iloc[0,id_relacji+1], kolor))
            id_relacji += 1
    plik.write("""
  </graph>""")
plik.write("""
</graphml>""")

plik.close()

#koniec skryptu
