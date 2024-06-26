#Création de l'image pour le conteneur flask
docker build -t flask:1.1 flask/.

#Installation des conteneurs Mysql, flask et adminer
docker compose up -d
echo "Démarrage des conteneurs..."
sleep 10

echo "Récupération de l'IP du conteneur MariaDB et insertion de la table Utilisateurs..."
host=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' mariadb)

echo "Création et insertion de la base de donnée..."
mysql -u root -p'foo' -h $host < ~/SAE61_WEB/SQL/table.sql

echo "OK !"


