WEB_SERVICE_ADDRESS='http://localhost:5000'


case $1 in

  reg)
    curl $WEB_SERVICE_ADDRESS/registration \
          -X POST \
          -H 'Content-Type: application/json' \
          -d '{"email":"somemail@yandex.ru", "password":"loSD$#%123REqd"}'
    ;;

  login)
    curl $WEB_SERVICE_ADDRESS/login \
          -X POST \
          -H 'Content-Type: application/json' \
          -d '{"email":"somemail@yandex.ru", "password":"loSD$#%123REqd"}'
    ;;

  reg_per_req)
    curl $WEB_SERVICE_ADDRESS/registr_personal_request \
          -X POST \
          -H 'Content-Type: application/json' \
          -d '{"req_type":"personal", "subdivision_id":"2", "req_date":"2023-06-23", "req_time":"15:00:00", "req_status":"in work", "req_status_description":"check docs", "user_id":"somemail@yandex.ru"}'
    ;;

  req_list)
    curl $WEB_SERVICE_ADDRESS/requests_list \
          -X POST \
          -H 'Content-Type: application/json' \
          -d '{"user_id" : "somemail@yandex.ru"}'
    ;;

  *)
    echo -n 'unknown command!'
    ;;
esac


