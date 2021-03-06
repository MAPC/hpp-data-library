# Housing Units by Year Built
sql = "SELECT * FROM tabular.b25127_hu_tenure_year_built_units_acs_m WHERE acs_year = '2011-15'"
dataset = DataGrid(batch, sql, [])
chart = Chart(batch,dataset,"YearBuilt")

def munging(self):
  df = self.data()
  cols = ['h10','h0009','h8099','h6079','h4059','h39']
  headings = ['2010 or later', '2000-09', '1980-99', '1960-1979', '1940-59', 'Under 1939']
  df = df[df['muni_id'].isin(self.subregional_munis["MUNI_ID"])]
  muncipalities = df['municipal']
  transpose_df = df[cols].transpose()
  self.munged = df[cols]
  self.munged.columns = headings
  self.munged.insert(0, "Municipality", muncipalities)

dataset.munge(munging)
chart.generate(type="column", subtype="percent_stacked")

chart.chart.set_title({
  'name': 'Housing Units by Year Built'
})
