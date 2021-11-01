# import pymysql, os, json,csv
# from users.models import State1,Country,City


# file='countries.json'
# json_data=open(file).read()
# json_obj = json.loads(json_data)

# # do validation and checks before insert
# def validate_string(val):
#    if val is not None:
#         if type(val) is int:
#             #for x in val:
#             #   print(x)
#             return str(val).encode('utf-8')
#         else:
#             return val

# con = pymysql.connect(host = 'localhost',user = 'root', password = 'root',database = 'work', port=3306)
# cursor = con.cursor()    

# # parse json data to SQL insert
# for i, item in enumerate(json_obj):
#     country_code=validate_string(item.get("country_code",None))
#     name=validate_string(item.get("name",None))
#     phonecode=validate_string(item.get("phonecode",None))

#     cursor.execute("INSERT INTO users_country (country_code,name ,phonecode) VALUES (%s,%s,%s)", (country_code,name,phonecode))

# con.commit()
# con.close()



# #states
# # file='states.json'
# # json_data=open(file,encoding="utf8").read()
# # json_obj = json.loads(json_data)

# # # do validation and checks before insert
# # def validate_string(val):
# #    if val is not None:
# #         if type(val) is int:
# #             #for x in val:
# #             #   print(x)
# #             return str(val).encode('utf-8')
# #         else:
# #             return val

# # con = py.connect(host = 'localhost',user = 'root', password = 'root',database = 'latest', port=3306)
# # cursor = con.cursor()    

# # # parse json data to SQL insert
# # for i, item in enumerate(json_obj):
# #     state_id=validate_string(item.get("state_id",None))
# #     name=validate_string(item.get("name",None))
# #     country_id=validate_string(item.get("country_id",None))
# #     country_code=validate_string(item.get("country_code",None))
# #     state_code=validate_string(item.get("state",None))
# #     # type=a.get("type",None))
# #     latitude=validate_string(item.get("latitude",None))
# #     longitude=validate_string(item.get("longitude",None))


# #     cursor.execute("INSERT INTO worldapp_state1 (state_id,name,country_id,country_code,state_code,latitude,longitude) VALUES (%s,	%s , %s, %s, %s, %s,%s)", (state_id,name,country_id,country_code,state_code,latitude,longitude))

# # con.commit()    
# # con.close()



# # cities
# # file='cities.json'
# # json_data=open(file).read()
# # json_obj = json.loads(json_data)
# # csvFilePath = r"cities.csv"


# # # # do validation and checks before insert

# # data=[]

# # with open(csvFilePath,encoding='utf-8') as csvFile:
# #     csvReader=csv.DictReader(csvFile)
    
# #     for rows in csvReader:
# #         data.append(rows)
        
# # con = pymysql.connect(host = 'localhost',user = 'root', password = 'root',database = 'latest', port=3306)
# # cursor = con.cursor()    

# # # parse json data to SQL insert


# # for a in data:
# #     name=a.get("name",None)
# #     state_id=a.get("state_id",None)
# #     state_code=a.get("state_code",None)
# #     country_id=a.get("country_id",None)
# #     country_code=a.get("country_code",None)
# #     latitude=a.get("latitude",None)
# #     longitude=a.get("longitude",None)
# #     wikiDataId=a.get("wikiDataId",None)
# #     City.objects.create(state_id = state_id,state_code=state-code,name=name,country_id = country_id,country_code=country_code,latitude=latitude,longitude=longitude,wikidataId=wikidataId)

# #     cursor.execute("INSERT INTO worldapp_city (name,state_id,state_code,country_id,country_code,latitude,longitude,wikiDataId) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (name,state_id,state_code,country_id,country_code,latitude,longitude,wikiDataId))

# # con.commit()    
# # con.close()







# # import pandas as pd
# # from sqlalchemy import create_engine

# # # df = pd.read_csv('cities.csv',encoding='utf-8')
# # # print(df.to_string())


# # column_names=['id','name','state_id','state_code','country_id','country_code','latitude','longitude','wikiDataId']

# # df = pd.read_csv('cities1.csv', header = None,names=column_names)
# # print(df)

# # df = pd.read_csv('cities1.csv', header = 0)
# # # print(df)

# # engine = create_engine('mysql://root:root@localhost:3306/latest')    #mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
# # with engine.connect() as conn, conn.begin():
# #     df.to_sql('worldapp_city', conn, if_exists='append', index=False)



    
    
