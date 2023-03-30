#!/bin/bash

#load vars
source ./vars.sh


resources=("passes" "visitors" "employees" "subdivisions" "users")

if [ $1 == 'delete' ]
then
  if [ $2 == 'all' ]
  then
    for res in "${resources[@]}"
    do
      echo "---------"
      echo $res
      curl $API_SERVER_ADDRESS/$res -X DELETE
    done
  else
    START=$3
    END=$4
    for (( i=$START; i<=$END; i++ ))
    do
      curl $API_SERVER_ADDRESS/$2/$i -X DELETE
    done
  fi
elif [ $1 == 'get' ]
then
  if [ $2 == 'all' ]
  then
    for res in "${resources[@]}"
    do
      echo "---------"
      echo $res
      curl $API_SERVER_ADDRESS/$res -X GET
    done
  else
    res=$2
    id=$3
    curl $API_SERVER_ADDRESS/$res/$id -X GET
  fi
elif [ $1 == 'post' ]
then
  source ./full_db.sh
elif [ $1 == 'patch' ]
then
  curl $API_SERVER_ADDRESS/subdivisions/1 \
          -X PATCH \
          -H "Content-Type: application/json" \
          -d '{"title":"New_title"}' -I
   
  curl $API_SERVER_ADDRESS/visitors/1 \
                -X PATCH \
                -H "Content-Type: application/json" \
                -d '{"s_name":"Прокофьев"}'

  curl $API_SERVER_ADDRESS/employees/1 \
          -X PATCH \
          -H "Content-Type: application/json" \
          -d '{"f_name":"Георгий"}'

  curl $API_SERVER_ADDRESS/passes/1 \
                -X PATCH \
                -H "Content-Type: application/json" \
                -d '{"visit_purpose":"prosto tak"}'
fi


