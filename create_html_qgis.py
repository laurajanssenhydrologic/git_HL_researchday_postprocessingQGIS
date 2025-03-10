#%%
import geopandas as gpd

#%% define paths

peilgebied=gpd.read_file(r"D:\work\P23006\GIS\peilen\Peilgebied_2d_fixed.shp")
waterloop=gpd.read_file(r"D:\work\P23006\GIS\HYDAMO\HDSR_28.gpkg",layer="waterloop")
kpi=gpd.read_file(r"D:\work\P23006\Figuren_output\gpkg28\V2022\performance_indicators_wl_compleet.gpkg")
output_path=r"D:\work\P23006\Figuren_output\QGIS_html\V2022\geopackages/"

#%% KPI
col_in_table = ['CODE', 'NAAM','MAE', 'RMSE', 'NSE','KGE']
list_header = ''.join([f'<th style="background-color:#f2f2f2; text-align:left;">{col}</th>' for col in col_in_table])
html_table_str = ['<table border="1" cellpadding="5" cellspacing="0" style="width:100%; border-collapse: collapse; border: 1px solid black;"><tr>'+\
    list_header + '</tr><tr>' +\
    '<td>'+r['CODE']+'</td>'+\
        '<td>'+r['NAAM']+'</td>'+\
            '<td>'+str(r['MAE'])+'</td>'+\
                '<td>'+str(r['RMSE'])+'</td>'+\
                    '<td>'+str(r['NSE'])+'</td>'+\
                        '<td>'+str(r['KGE'])+'</td>'+\
    '</tr></table>' for n, r in kpi.iterrows()]
kpi['html_table'] = html_table_str
#kpi["html_fig_path"] = '<img src="file:///'+image_path+kpi["CODE"]+".png\""+ ' width=300 height=300 >'
kpi["html_fig_path"] = '<img src="images/'+kpi["CODE"]+".png\"" + ' width=300 height=300 >'

#kpi_def=kpi[["RMSE","html_table","html_fig_path","geometry"]]
kpi.to_file(output_path+"KPI.gpkg",index=False)

# %% peilgebieden
col_in_table = ['CODE', 'VASTPEIL','WINTERPEIL', 'ZOMERPEIL', 'FLEXIBEL_B','FLEXIBEL_O']
list_header = ''.join([f'<th style="background-color:#f2f2f2; text-align:left;">{col}</th>' for col in col_in_table])
#list_values = ''.join([f'<td>kpi[col]</td>' for col in col_in_table])
html_table_str = ['<table border="1" cellpadding="5" cellspacing="0" style="width:100%; border-collapse: collapse; border: 1px solid black;"><tr>'+\
    list_header + '</tr><tr>' +\
    '<td>'+r['CODE']+'</td>'+\
        '<td>'+str(r['VASTPEIL'])+'</td>'+\
            '<td>'+str(r['WINTERPEIL'])+'</td>'+\
                '<td>'+str(r['ZOMERPEIL'])+'</td>'+\
                    '<td>'+str(r['FLEXIBEL_B'])+'</td>'+\
                        '<td>'+str(r['FLEXIBEL_O'])+'</td>'+\
    '</tr></table>' for n, r in peilgebied.iterrows()]

peilgebied['html_table'] = html_table_str

peilgebied_def=peilgebied[["html_table","geometry"]]
peilgebied_def.to_file(output_path+ "peilgebied.gpkg",index=False)

#%% waterlopen
waterloop_def=waterloop[["code","geometry"]]
waterloop_def.to_file(output_path+ "waterloop.gpkg",index=False)

# %%
