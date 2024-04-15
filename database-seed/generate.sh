#!/bin/bash

# ------------------------------------------
CURRENT_DIR=$(pwd)
SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" >/dev/null && pwd )"
# ------------------------------------------

# Change directory to the generators folder
cd "${DIR}/../app/generators" || exit 1

# Generate the schema
python db_generator.py > "${DIR}/seed"
if [[ $? -ne 0 ]]; then
  echo "Failed to generate DB schema"
  exit 1
fi

# Change directory to the seed folder
cd "${DIR}" || exit 1

# Combine SQL files in the correct order
ls -1 [0-9]*.inserts.*.sql | sort -V | xargs cat > inserts.sql
mv seed seed.sql

# Generate drop statements
grep "CREATE TABLE" ./seed.sql | awk '{print "DROP TABLE IF EXISTS "$3";"}' > drop.sql
echo "

-- Inserts
" >> ./seed.sql
cat ./inserts.sql >> ./seed.sql
rm ./inserts.sql

echo ""