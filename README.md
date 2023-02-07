# SQLite Gui Api


this is a ****flask**** api that receives json data and creates an sqlite database for you quickly. its part of a bigger project which is a a web app to make the creation of an sqlite database fast and easy.

### JSON Format

***{
    "db_name":"databasename",\
  "tables":[\
    {
      "tablename":"Student",\
      "columns":[\
        {"fullname":"text",\
        "age":"integer",\
        "pin":"integer"}
        ]
    },
    ]\
}***
