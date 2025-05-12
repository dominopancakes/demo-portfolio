sudo dnf install httpd wget php php-mysqlnd -y
sudo systemctl start httpd
cd /var/www/html
sudo wget https://wordpress.org/latest.tar.gz
sudo tar xvzf latest.tar.gz
sudo sed -i 's|DocumentRoot "/var/www/html"|DocumentRoot "/var/www/html/wordpress"|' /etc/httpd/conf/httpd.conf
sudo systemctl restart httpd
sudo chown -Rf apache:apache ./wordpress/
cd
sudo chmod -Rf 775 ./wordpress/
echo '<VirtualHost *:80>
    ServerAdmin root@localhost
    DocumentRoot /var/www/html/wordpress
    <Directory "/var/www/html/wordpress">
        Options Indexes FollowSymLinks
        AllowOverride all
        Require all granted
    </Directory>
    ErrorLog /var/log/httpd/wordpress_error.log
    CustomLog /var/log/httpd/wordpress_access.log common
</VirtualHost>' | sudo tee /etc/httpd/conf.d/wordpress.conf
sudo systemctl restart httpd
echo "WordPress installation and configuration completed."
