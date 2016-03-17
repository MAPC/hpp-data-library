# Building Permits by Type
sql = "SELECT * FROM tabular.hous_building_permits_m WHERE bp_year = '2013'"
dataset = generate.DataGrid(batch, sql, [])
chart = generate.Chart(batch,dataset,"building_permits_type")

def munging(self):
  df = self.data()
  
  cols = ['municipal', 'sf_units', 'mf_units']
  headings = ['Municipality', 'Single-Family Permits', 'Multi-Family Permits']
  self.munged = df.sort_values(by="tot_units", ascending=False)[cols][df['muni_id'].isin(self.subregional_munis["MUNI_ID"])]
  self.munged.columns = headings

dataset.munge(munging)
chart.generate(type="column", subtype="stacked")
