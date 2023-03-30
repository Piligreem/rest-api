#!/bin/bash

psql -h localhost -p 5433 -U postgres -d worldskills -f ../db/db.sql


#subdivision
curl $API_SERVER_ADDRESS/subdivisions \
          -X POST \
          -H "Content-Type: application/json"\
          -d '{"title":"Main_subd"}'
curl $API_SERVER_ADDRESS/subdivisions \
          -X POST \
          -H "Content-Type: application/json"\
          -d '{"title":"Sub_subd"}'


# employees
curl $API_SERVER_ADDRESS/employees \
          -X POST \
          -H "Content-Type: application/json"\
          -d '{"subdivision_id":"1", "f_name":"Иван", "s_name":"Иванов", "surname":"Иванович", "department":"dep1"}'
curl $API_SERVER_ADDRESS/employees \
          -X POST \
          -H "Content-Type: application/json"\
          -d '{"subdivision_id":"2", "f_name":"Петр", "s_name":"Петров", "surname":"Петрович", "department":"dep1"}'


# visitors
curl $API_SERVER_ADDRESS/visitors \
          -X POST \
          -H "Content-Type: application/json"\
          -d '{"subdivision_id":"1", "f_name":"Николай", "s_name":"Николаев", "surname":"Николаевич", "phone_num":"88005553535", "email":"example@mail.com", "organization":"Org1", "notes":"", "birthday":"01.01.2001", "passport_data":"2218901728", "appointment":"", "group_id":""}'

# pass
curl $API_SERVER_ADDRESS/passes \
          -X POST \
          -H "Content-Type: application/json"\
          -d '{"visit_purpose":"learning", "date_start":"01.01.2023", "date_end":"03.01.2023", "employee_id":"1", "visitor_id":"1", "subdivision_id":"1"}'





