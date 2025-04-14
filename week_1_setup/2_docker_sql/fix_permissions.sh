echo '#!/bin/bash' > fix_permissions.sh
echo 'sudo chmod -R 744 /workspaces/Zoomcamp2025/week_1_setup/2_docker_sql/ny_taxi_potgres_data' >> fix_permissions.sh
chmod +x fix_permissions.sh