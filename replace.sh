#!/bin/bash

echo -n "Please set the domain, e.g localhost (replaces <DOMAIN>): "
read domain
echo -n "Please set the app-name e.g chieftest (replaces <APP_NAME>): "
read appname


find . -type f -exec sed -i "s/<APP_NAME>/$appname/g" {} \;
find . -type f -exec sed -i "s/<DOMAIN>/$domain/g" {} \;
