#!/usr/bin/env bash

ssh ${DEPLOY_UESR}@${DEPLOY_HOST_BASTION}
become ${APP_NAME_ON_TOOLFORGE}
source /data/project/google-drive-photos-to-commons/www/python/venv/bin/activate
cd /data/project/google-drive-photos-to-commons/www/python/src
git pull origin master
webservice --backend=kubernetes python3.5 stop
pip install -r requirements-deploy.txt
python manage.py collectstatic  --noinput
python manage.py migrate  --noinput
webservice --backend=kubernetes python3.5 start
echo "Deploy finished"
