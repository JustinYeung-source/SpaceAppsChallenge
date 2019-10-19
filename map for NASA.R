library(leaflet)
labels = c("DAWS",
           "FSIM",
           "FSMI",
           "GILL",
           "MCMU",
           "RANK",
           "TALO",
           "WGRY",
           "BRD",
           "CBB",
           "FCC",
           "IQA",
           "MEA",
           "OTT",
           "RES",
           "STJ",
           "VIC")

leaflet() %>%
  addTiles() %>%
  addMarkers(lng=-139.11, lat=64.05, label="DAWS") %>%
  addCircles(lng=-121.23, lat=61.76, radius = 10, fill = TRUE)%>%
  addMarkers(lng=-121.23, lat=61.76, label="FSIM") %>%
  addMarkers(lng=-111.95, lat=60.02, label='FSMI') %>%
  addMarkers(lng=-94.64,  lat=56.38, label='GILL') %>%
  addMarkers(lng=-111.21, lat=56.66, label='MCMU') %>%
  addMarkers(lng=-92.11,  lat=62.82, label='RANK') %>%
  addMarkers(lng=-93.55,  lat=69.54, label='TALO') %>%
  addMarkers(lng=-120.03,	lat=51.88, label='WGRY') %>%
  addMarkers(lng=-99.97,  lat=49.87, label='BRD') %>%
  addMarkers(lng=-105.03, lat=69.12, label='CBB') %>%
  addMarkers(lng=-94.09,  lat=58.76, label='FCC') %>%
  addMarkers(lng=-68.52,  lat=63.75, label='IQA') %>%
  addMarkers(lng=-113.35, lat=54.62, label='MEA') %>%
  addMarkers(lng=-75.55,  lat=45.4,  label='OTT') %>%
  addMarkers(lng=-94.89,  lat=74.69, label='RES') %>%
  addMarkers(lng=-52.68,  lat=47.6,  label='STJ') %>%
  addMarkers(lng=-123.42, lat=48.52, label='VIC')
