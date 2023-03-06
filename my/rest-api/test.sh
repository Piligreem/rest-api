#!/bin/bash


resources=("passes" "visitors" "employees" "subdivisions")

if [ $1 == 'delete' ]
then
  if [ $2 == 'ALL' ]
  then
    for res in "${resources[@]}"
    do
      echo "---------"
      echo $res
      curl http://localhost:5000/$res -X DELETE
    done
  else
    START=$3
    END=$4
    for (( i=$START; i<=$END; i++ ))
    do
      curl http://localhost:5000/$2/$i -X DELETE
    done
  fi
elif [ $1 == 'get' ]
then
  if [ $2 == 'ALL' ]
  then
    for res in "${resources[@]}"
    do
      echo "---------"
      echo $res
      curl http://localhost:5000/$res -X GET
    done
  else
    res=$2
    id=$3
    curl http://localhost:5000/$res/$id -X GET
  fi
elif [ $1 == 'post' ]
then
  source ./full_db.sh
fi


