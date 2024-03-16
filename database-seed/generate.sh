#!/bin/bash

# ------------------------------------------
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do
  DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE"
done
DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null && pwd )"
# ------------------------------------------

cd "${DIR}/../app/generators" || exit 1
python db_generator.py > "${DIR}/seed"
if [[ $? -ne 0 ]]; then
  echo "Failed to generate DB schema"
  exit 1
fi

cd "${DIR}" || exit 1
cat [0-9]*.inserts.*.sql > inserts.sql
mv seed seed.sql
grep "CREATE TABLE" ./seed.sql | awk '{print "DROP TABLE IF EXISTS "$3";"}' > drop.sql
echo "

-- Inserts
" >> ./seed.sql
cat ./inserts.sql >> ./seed.sql
rm ./inserts.sql

echo ""