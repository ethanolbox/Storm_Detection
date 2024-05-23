year = 2022

# first export just to get table to work in ArcGIS
arcpy.conversion.ExportTable(
    in_table="stormproc" + str(year) + ".csv",
    out_table=r"C:\Users\ew0045\OneDrive - Princeton University\Desktop\Data\MyProject\MyProject.gdb\storm" + str(year) + "",
    where_clause="",
    use_field_alias_as_name="NOT_USE_ALIAS",
    field_mapping='# "EVENT_ID" false true true 0 Long 0 0,First,#,stormproc' + str(year) + '.csv,# EVENT_ID,-1,-1;STATE_FIPS "STATE_FIPS" true true false 4 Long 0 0,First,#,stormproc' + str(year) + '.csv,STATE_FIPS,-1,-1;CZ_FIPS "CZ_FIPS" true true false 4 Long 0 0,First,#,stormproc' + str(year) + '.csv,CZ_FIPS,-1,-1;CZ_TYPE "CZ_TYPE" true true false 255 Text 0 0,First,#,stormproc' + str(year) + '.csv,CZ_TYPE,0,8000;EVENT_TYPE "EVENT_TYPE" true true false 8000 Text 0 0,First,#,stormproc' + str(year) + '.csv,EVENT_TYPE,0,8000;BEGIN_YEARMONTH "BEGIN_YEARMONTH" true true false 4 Long 0 0,First,#,stormproc' + str(year) + '.csv,BEGIN_YEARMONTH,-1,-1;BEGIN_DAY "BEGIN_DAY" true true false 4 Long 0 0,First,#,stormproc' + str(year) + '.csv,BEGIN_DAY,-1,-1;END_YEARMONTH "END_YEARMONTH" true true false 4 Long 0 0,First,#,stormproc' + str(year) + '.csv,END_YEARMONTH,-1,-1;END_DAY "END_DAY" true true false 4 Long 0 0,First,#,stormproc' + str(year) + '.csv,END_DAY,-1,-1;LATITUDE "LATITUDE" true true false 8000 Text 0 0,First,#,stormproc' + str(year) + '.csv,LATITUDE,0,8000;LONGITUDE "LONGITUDE" true true false 8000 Text 0 0,First,#,stormproc' + str(year) + '.csv,LONGITUDE,0,8000;beg_datetime "datetime" true true false 8 Date 0 0,First,#,stormproc' + str(year) + '.csv,beg_datetime,-1,-1;days "days" true true false 255 Text 0 0,First,#,stormproc' + str(year) + '.csv,days,-1,-1',
    sort_field=None
)

# select by attribute for nans (for some reason, some files have an extra space in front of the nans, so you won't be able to just run a loop. 
# This is insanely frustrating, but I ended up manually checking if this selected things correctly by year and then you can run the rest, 
# adjusting the other selection step based on space or no space in front of the nans.)
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="storm" + str(year) + "",
    selection_type="NEW_SELECTION",
    where_clause="LONGITUDE = ' nan'",
    invert_where_clause=None
)

# export for noloc
arcpy.conversion.ExportTable(
    in_table="storm" + str(year) + "",
    out_table=r"C:\Users\ew0045\OneDrive - Princeton University\Desktop\Data\MyProject\MyProject.gdb\storm" + str(year) + "_noloc",
    where_clause="",
    use_field_alias_as_name="NOT_USE_ALIAS",
    field_mapping='F_ "EVENT_ID" true true false 4 Long 0 0,First,#,storm' + str(year) + ',F_,-1,-1;STATE_FIPS "STATE_FIPS" true true false 4 Long 0 0,First,#,storm' + str(year) + ',STATE_FIPS,-1,-1;CZ_FIPS "CZ_FIPS" true true false 4 Long 0 0,First,#,storm' + str(year) + ',CZ_FIPS,-1,-1;CZ_TYPE "CZ_TYPE" true true false 255 Text 0 0,First,#,storm' + str(year) + ',CZ_TYPE,0,255;EVENT_TYPE "EVENT_TYPE" true true false 8000 Text 0 0,First,#,storm' + str(year) + ',EVENT_TYPE,0,8000;BEGIN_YEARMONTH "BEGIN_YEARMONTH" true true false 4 Long 0 0,First,#,storm' + str(year) + ',BEGIN_YEARMONTH,-1,-1;BEGIN_DAY "BEGIN_DAY" true true false 4 Long 0 0,First,#,storm' + str(year) + ',BEGIN_DAY,-1,-1;END_YEARMONTH "END_YEARMONTH" true true false 4 Long 0 0,First,#,storm' + str(year) + ',END_YEARMONTH,-1,-1;END_DAY "END_DAY" true true false 4 Long 0 0,First,#,storm' + str(year) + ',END_DAY,-1,-1;LATITUDE "LATITUDE" true true false 8000 Text 0 0,First,#,storm' + str(year) + ',LATITUDE,0,8000;LONGITUDE "LONGITUDE" true true false 8000 Text 0 0,First,#,storm' + str(year) + ',LONGITUDE,0,8000;beg_datetime "datetime" true true false 8 Date 0 0,First,#,storm' + str(year) + ',beg_datetime,-1,-1;days "days" true true false 255 Text 0 0,First,#,storm' + str(year) + ',days,0,255',
    sort_field=None
)

# switch selection for non-nans
arcpy.management.SelectLayerByAttribute(
    in_layer_or_view="storm" + str(year) + "",
    selection_type="NEW_SELECTION",
    where_clause="LATITUDE <> ' nan'",
    invert_where_clause=None
)

# export for withloc
arcpy.conversion.ExportTable(
    in_table="storm" + str(year) + "",
    out_table=r"C:\Users\ew0045\OneDrive - Princeton University\Desktop\Data\MyProject\MyProject.gdb\storm" + str(year) + "_withloc",
    where_clause="",
    use_field_alias_as_name="NOT_USE_ALIAS",
    field_mapping='F_ "EVENT_ID" true true false 4 Long 0 0,First,#,storm' + str(year) + ',F_,-1,-1;STATE_FIPS "STATE_FIPS" true true false 4 Long 0 0,First,#,storm' + str(year) + ',STATE_FIPS,-1,-1;CZ_FIPS "CZ_FIPS" true true false 4 Long 0 0,First,#,storm' + str(year) + ',CZ_FIPS,-1,-1;CZ_TYPE "CZ_TYPE" true true false 255 Text 0 0,First,#,storm' + str(year) + ',CZ_TYPE,0,255;EVENT_TYPE "EVENT_TYPE" true true false 8000 Text 0 0,First,#,storm' + str(year) + ',EVENT_TYPE,0,8000;BEGIN_YEARMONTH "BEGIN_YEARMONTH" true true false 4 Long 0 0,First,#,storm' + str(year) + ',BEGIN_YEARMONTH,-1,-1;BEGIN_DAY "BEGIN_DAY" true true false 4 Long 0 0,First,#,storm' + str(year) + ',BEGIN_DAY,-1,-1;END_YEARMONTH "END_YEARMONTH" true true false 4 Long 0 0,First,#,storm' + str(year) + ',END_YEARMONTH,-1,-1;END_DAY "END_DAY" true true false 4 Long 0 0,First,#,storm' + str(year) + ',END_DAY,-1,-1;LATITUDE "LATITUDE" true true false 8000 Text 0 0,First,#,storm' + str(year) + ',LATITUDE,0,8000;LONGITUDE "LONGITUDE" true true false 8000 Text 0 0,First,#,storm' + str(year) + ',LONGITUDE,0,8000;beg_datetime "datetime" true true false 8 Date 0 0,First,#,storm' + str(year) + ',beg_datetime,-1,-1;days "days" true true false 255 Text 0 0,First,#,storm' + str(year) + ',days,0,255',
    sort_field=None
)

# export the noloc file to the research file
arcpy.conversion.ExportTable(
    in_table="storm" + str(year) + "_noloc",
    out_table=r"C:\Users\ew0045\Research Code\Storm_Detection\storm_noloc\storm" + str(year) + "_noloc.csv",
    where_clause="",
    use_field_alias_as_name="NOT_USE_ALIAS",
    field_mapping='F_ "EVENT_ID" true true false 4 Long 0 0,First,#,storm' + str(year) + '_noloc,F_,-1,-1;STATE_FIPS "STATE_FIPS" true true false 4 Long 0 0,First,#,storm' + str(year) + '_noloc,STATE_FIPS,-1,-1;CZ_FIPS "CZ_FIPS" true true false 4 Long 0 0,First,#,storm' + str(year) + '_noloc,CZ_FIPS,-1,-1;CZ_TYPE "CZ_TYPE" true true false 255 Text 0 0,First,#,storm' + str(year) + '_noloc,CZ_TYPE,0,255;EVENT_TYPE "EVENT_TYPE" true true false 8000 Text 0 0,First,#,storm' + str(year) + '_noloc,EVENT_TYPE,0,8000;BEGIN_YEARMONTH "BEGIN_YEARMONTH" true true false 4 Long 0 0,First,#,storm' + str(year) + '_noloc,BEGIN_YEARMONTH,-1,-1;BEGIN_DAY "BEGIN_DAY" true true false 4 Long 0 0,First,#,storm' + str(year) + '_noloc,BEGIN_DAY,-1,-1;END_YEARMONTH "END_YEARMONTH" true true false 4 Long 0 0,First,#,storm' + str(year) + '_noloc,END_YEARMONTH,-1,-1;END_DAY "END_DAY" true true false 4 Long 0 0,First,#,storm' + str(year) + '_noloc,END_DAY,-1,-1;LATITUDE "LATITUDE" true true false 8000 Text 0 0,First,#,storm' + str(year) + '_noloc,LATITUDE,0,8000;LONGITUDE "LONGITUDE" true true false 8000 Text 0 0,First,#,storm' + str(year) + '_noloc,LONGITUDE,0,8000;beg_datetime "datetime" true true false 8 Date 0 0,First,#,storm' + str(year) + '_noloc,beg_datetime,-1,-1;days "days" true true false 255 Text 0 0,First,#,storm' + str(year) + '_noloc,days,0,255',
    sort_field=None
)

# calculate fields for lat and long
arcpy.management.CalculateField(
    in_table="storm" + str(year) + "_withloc",
    field="Latitude1",
    expression="!LATITUDE!",
    expression_type="PYTHON3",
    code_block="",
    field_type="Double",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

arcpy.management.CalculateField(
    in_table="storm" + str(year) + "_withloc",
    field="Longitude1",
    expression="!LONGITUDE!",
    expression_type="PYTHON3",
    code_block="",
    field_type="Double",
    enforce_domains="NO_ENFORCE_DOMAINS"
)

# XY Table to point
arcpy.management.XYTableToPoint(
    in_table="storm" + str(year) + "_withloc",
    out_feature_class="storm" + str(year) + "_withloc_XYTableToPoint",
    x_field="Longitude1",
    y_field="Latitude1",
    z_field=None,
    coordinate_system='GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision'
)

# Add spatial join
arcpy.management.AddSpatialJoin(
    target_features="storm" + str(year) + "_withloc_XYTableToPoint",
    join_features="cb_2020_us_zcta520_500k",
    join_operation="JOIN_ONE_TO_ONE",
    join_type="KEEP_ALL",
    field_mapping=r'ZCTA5CE20 "ZCTA5CE20" true true false 5 Text 0 0,First,#,C:\Users\ew0045\OneDrive - Princeton University\Desktop\Data\zipcodes\cb_2020_us_zcta520_500k.shp,ZCTA5CE20,0,5;AFFGEOID20 "AFFGEOID20" true true false 14 Text 0 0,First,#,C:\Users\ew0045\OneDrive - Princeton University\Desktop\Data\zipcodes\cb_2020_us_zcta520_500k.shp,AFFGEOID20,0,14;GEOID20 "GEOID20" true true false 5 Text 0 0,First,#,C:\Users\ew0045\OneDrive - Princeton University\Desktop\Data\zipcodes\cb_2020_us_zcta520_500k.shp,GEOID20,0,5;NAME20 "NAME20" true true false 100 Text 0 0,First,#,C:\Users\ew0045\OneDrive - Princeton University\Desktop\Data\zipcodes\cb_2020_us_zcta520_500k.shp,NAME20,0,100;LSAD20 "LSAD20" true true false 2 Text 0 0,First,#,C:\Users\ew0045\OneDrive - Princeton University\Desktop\Data\zipcodes\cb_2020_us_zcta520_500k.shp,LSAD20,0,2;ALAND20 "ALAND20" true true false 14 Double 0 14,First,#,C:\Users\ew0045\OneDrive - Princeton University\Desktop\Data\zipcodes\cb_2020_us_zcta520_500k.shp,ALAND20,-1,-1;AWATER20 "AWATER20" true true false 14 Double 0 14,First,#,C:\Users\ew0045\OneDrive - Princeton University\Desktop\Data\zipcodes\cb_2020_us_zcta520_500k.shp,AWATER20,-1,-1',
    match_option="INTERSECT",
    search_radius=None,
    distance_field_name=""
)

# C:\Users\ew0045\OneDrive - Princeton University\Desktop\Data\MyProject\MyProject.gdb\storm' + str(year) + '_withloc_XYTableToPoint

# export
arcpy.conversion.ExportTable(
    in_table="storm" + str(year) + "_withloc_XYTableToPoint",
    out_table=r"C:\Users\ew0045\Research Code\Storm_Detection\storm_withloc_zips\storm" + str(year) + "_withloc_zips.csv",
    where_clause="",
    use_field_alias_as_name="NOT_USE_ALIAS",
    field_mapping='F_ "EVENT_ID" true true false 4 Long 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint.F_,-1,-1;STATE_FIPS "STATE_FIPS" true true false 4 Long 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint.STATE_FIPS,-1,-1;CZ_FIPS "CZ_FIPS" true true false 4 Long 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint.CZ_FIPS,-1,-1;CZ_TYPE "CZ_TYPE" true true false 255 Text 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint.CZ_TYPE,0,255;EVENT_TYPE "EVENT_TYPE" true true false 8000 Text 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint.EVENT_TYPE,0,8000;BEGIN_YEARMONTH "BEGIN_YEARMONTH" true true false 4 Long 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint.BEGIN_YEARMONTH,-1,-1;BEGIN_DAY "BEGIN_DAY" true true false 4 Long 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint.BEGIN_DAY,-1,-1;END_YEARMONTH "END_YEARMONTH" true true false 4 Long 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint.END_YEARMONTH,-1,-1;END_DAY "END_DAY" true true false 4 Long 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint.END_DAY,-1,-1;LATITUDE "LATITUDE" true true false 8000 Text 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint.LATITUDE,0,8000;LONGITUDE "LONGITUDE" true true false 8000 Text 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint.LONGITUDE,0,8000;beg_datetime "datetime" true true false 8 Date 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint.beg_datetime,-1,-1;days "days" true true false 255 Text 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint.days,0,255;Latitude1 "Latitude1" true true false 8 Double 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint.Latitude1,-1,-1;Longitude1 "Longitude1" true true false 8 Double 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint.Longitude1,-1,-1;OBJECTID "OBJECTID" false true false 4 Long 0 9,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint_AddSpatialJoin.OBJECTID,-1,-1;Join_Count "Join_Count" true true false 4 Long 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint_AddSpatialJoin.Join_Count,-1,-1;TARGET_FID "TARGET_FID" true true false 4 Long 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint_AddSpatialJoin.TARGET_FID,-1,-1;ZCTA5CE20 "ZCTA5CE20" true true false 5 Text 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint_AddSpatialJoin.ZCTA5CE20,0,5;AFFGEOID20 "AFFGEOID20" true true false 14 Text 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint_AddSpatialJoin.AFFGEOID20,0,14;GEOID20 "GEOID20" true true false 5 Text 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint_AddSpatialJoin.GEOID20,0,5;NAME20 "NAME20" true true false 100 Text 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint_AddSpatialJoin.NAME20,0,100;LSAD20 "LSAD20" true true false 2 Text 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint_AddSpatialJoin.LSAD20,0,2;ALAND20 "ALAND20" true true false 8 Double 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint_AddSpatialJoin.ALAND20,-1,-1;AWATER20 "AWATER20" true true false 8 Double 0 0,First,#,storm' + str(year) + '_withloc_XYTableToPoint,storm' + str(year) + '_withloc_XYTableToPoint_AddSpatialJoin.AWATER20,-1,-1',
    sort_field=None
)