set -x
password="$SA_PASSWORD"
# Wait to be sure that SQL Server came up
echo "************************** waiting for db 1"
while ! /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P "$password" -d master -Q 'SELECT 1'; do
  echo "Waiting sqlserver to start"
done

echo "************************** executing init script"
/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P "$password" -d master -i /usr/src/scripts/setup.sql

echo "************************** init script executed"
