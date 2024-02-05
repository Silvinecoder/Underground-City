#!/bin/bash

# ------------------------------------------
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null && pwd )"
# ------------------------------------------
cd "${DIR}"

cd ${DIR}/../app/generators
python db-generator > ${DIR}/seed
if [[ $? -ne 0 ]]; then
  echo "Failed to generate DB schema"
  exit 1
fi

cd ${DIR}
cat [0-9]*.inserts.*.sql > inserts.sql
mv seed seed.sql
grep "CREATE TABLE" ./seed.sql | awk '{print "DROP TABLE IF EXISTS "$3";"}' > drop.sql
echo "

-- Inserts
" >> ./seed.sql
cat ./inserts.sql >> ./seed.sql
rm ./inserts.sql

echo "
